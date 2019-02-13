QUESTION

Define a Python function descending(l) that returns True if each element in its input list is at most as big as the one before it. 
For instance:

  >>> descending([])
  True

  >>> descending([4,4,3])
  True

  >>> descending([19,17,18,7])
  False
  
  PROGRAM/SOLUTION
  
  def descending(l):
    val = False
    if l == []:
        return True
    for i in range(len(l) - 1):
        if l[i] >= l[i + 1]:
            val = True
        else:
            val = False
            break
    return val
