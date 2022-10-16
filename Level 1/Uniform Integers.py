# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here
    count=0

    a_length= len(list(str(A)))
    b_length= len(list(str(B)))
    count=0
    for n in range(a_length, b_length+1):
        o_count= ''
        for p in range(n):
            o_count+='1'
        for q in range(1,10):
            el= int(o_count)*q
            if el in range(A,(B+1)):
                count+=1
    return count