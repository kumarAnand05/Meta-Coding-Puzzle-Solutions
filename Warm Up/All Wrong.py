# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  out= ''
  for n in range(N):
    if C[n]== 'A':
      out+='B'
    else:
      out+='A'
  return out
