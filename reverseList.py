l = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(n) : 
  lReverse = l[::-1]
  for i in range(len(lReverse)) : 
    (lReverse[i]) = (lReverse[i])[::-1]
  print(lReverse)

reverse(l)
