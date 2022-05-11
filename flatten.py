l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
lFlatten = []



def flatten(n) :
  for e in n :
    if isinstance(e, list):
      flatten(e)
    else : 
      lFlatten.append(e)
  
flatten(l)
print(lFlatten)

