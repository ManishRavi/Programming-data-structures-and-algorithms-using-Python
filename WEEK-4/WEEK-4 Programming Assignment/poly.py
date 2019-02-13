QUESTION

Let us consider polynomials in a single variable x with integer coefficients: for instance, 3x4 - 17x2 - 3x + 5. 
Each term of the polynomial can be represented as a pair of integers (coefficient,exponent). 
The polynomial itself is then a list of such pairs.

We have the following constraints to guarantee that each polynomial has a unique representation:

a)  Terms are sorted in descending order of exponent
b)  No term has a zero cofficient
c)  No two terms have the same exponent
d)  Exponents are always nonnegative

For example, the polynomial introduced earlier is represented as

  [(3,4),(-17,2),(-3,1),(5,0)]
  
The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.

Write Python functions for the following operations:

  
  addpoly(p1,p2)
  multpoly(p1,p2)
  
that add and multiply two polynomials, respectively.

You may assume that the inputs to these functions follow the representation given above. Correspondingly, 
the outputs from these functions should also obey the same constraints.

Hint: You are not restricted to writing just the two functions asked for. You can write auxiliary functions to "clean up" polynomials 
– e.g., remove zero coefficient terms, combine like terms, sort by exponent etc. Build a library of functions that can be combined 
to achieve the desired format.

You may also want to convert the list representation to a dictionary representation and manipulate the dictionary representation,
and then convert back.

Some examples:

  >>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
  [(2, 1),(3, 0)]
Explanation: (4x3 + 3) + (-4x3 + 2x) = 2x + 3

  >>> addpoly([(2,1)],[(-2,1)])
  []
Explanation: 2x + (-2x) = 0

  >>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
  [(1, 3),(-1, 0)]
Explanation: (x - 1) * (x2 + x + 1) = x3 - 1

PROGRAM/SOLUTION

def addpoly(p1, p2):
    t1,t2,t3,t4=[],[],[],[]
    d1=dict(p1)
    d2=dict(p2)
    for k1,v1 in d1.items():
        for k2,v2 in d2.items():
            if v1==v2:
                t1.append((k1+k2,v1))
                break
            elif v1!=v2:
                t2.append((k1,v1))
                t2.append((k2,v2))
                break
        break
    t3=t1+t2
    t3.sort()
    d3=dict(t3)
    for k1,v1 in d3.items():
        if k1==0:
            continue
        else:
            t4.append((k1,v1))
    
    return t4
  
def multpoly(p1, p2):
    coff,exp,t1,t2,t3,t4=[],[],[],[],[],[]
    for i in range(len(p1)):
        for j in range(len(p2)):
            coff=p1[i][0]*p2[j][0]
            exp=p1[i][1]+p2[j][1]
            t1.append((coff,exp))
    for i in range(len(t1)):
        x = t1[i][1]
        for j in range(i+1,len(t1)):
            count=0
            if x == t1[j][1]:
                t2.append((t1[i][0]+t1[j][0],t1[i][1]))
                t3.append((t1[i][0], t1[i][1]))
                t3.append((t1[j][0], t1[j][1]))
    t4= [x for x in t1 if x not in t3]
    t4+=t2
    t3.clear()
    for i in range(len(t4)):
        if t4[i][0]!=0:
            t3.append((t4[i][0], t4[i][1]))
    return t3
    
    
