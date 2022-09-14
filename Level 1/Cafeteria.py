from typing import List


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  S.sort()
  initial_diff= S[0]-1          # To find out number of seats available on extreme left
  seats= initial_diff//(K+1)    # This gives number of seats that can be occupied in left extreme according to rule.
  final_diff= N-S[-1]           # To find out number of seats available on extreme right
  seats+= final_diff//(K+1)     # This gives number of seats that can be occupied in right extreme according to rule.
  
  for n in range((len(S)-1)):   # Looping through list of already occupied seats('S') till len(S)-1
    D= S[n+1]-S[n]-1            # Number of seats available between current occupied seat and next occupied seat
    if D>2*K:                   # As minimum number of seats required for 1 sitting between two persons is 2K+1
      seats+= (D-K)//(K+1)      # Gives number of seats that can be occupied between two persons with varying number of seats

  return seats