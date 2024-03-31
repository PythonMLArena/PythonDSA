# Linearly From 1 to n ( BackTrack )

N=10

def print1ton_backtrack(i,N):
    if i<1:
        return
    print1ton_backtrack(i-1,N)
    print(i)
    
print1ton_backtrack(N,N)







# Print N to 1 BackTrack

N=10

def printNto1_backtrack(i,N):
    if i>N:
        return
    printNto1_backtrack(i+1,N)
    print(i)

    
printNto1_backtrack(1,N)