QUESTION

A list of integers is said to be a valley if it consists of a sequence of strictly decreasing values followed by a sequence of strictly
increasing values. The decreasing and increasing sequences must be of length at least 2. The last value of the decreasing 
sequence is the first value of the increasing sequence.

Write a Python function valley(l) that takes a list of integers and returns True if l is a valley and False otherwise.

Here are some examples to show how your function should work.

  >>> valley([3,2,1,2,3])
  True

  >>> valley([3,2,1])
  False

  >>> valley([3,3,2,1,2])
  False
  
  PROGRAM/SOLUTION
  
  def valley(l):
    val1 = False
    val2 = False
    last = 0
    if l == []:
        return True
    if len(l) == 1:
        return False
    for i in range(0,len(l)-1):
        if l[i] > l[i + 1]:
            val1 = True
            last = i
        elif l[i] == l[i + 1]:
            val1 = False
            break
    for j in range(last, len(l) - 1):
        if l[j] < l[j + 1]:
            val2 = True
        elif l[j] == l[j + 1] :
            val2 = False
            break
    if val1 == val2:
        return val1
    else:
        return False
        
        
