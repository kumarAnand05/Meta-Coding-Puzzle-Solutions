from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  count=0
  for n in range(R):
    a=G[n]
    count+= a.count(1) 
  out= (count)/(R*C)
  return out
