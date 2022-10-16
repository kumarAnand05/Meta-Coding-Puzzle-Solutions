from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  count=0
  initial=1
  for p in range(M):
    a= C[p]
    diff1= abs(a-initial)
    other= abs(N-diff1)
    if diff1>=other:
      count+=other
    else:
      count+=diff1
    initial= C[p]
      
  return count
