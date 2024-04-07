# Parameter way
N=3
sum1=0
def sumParameter(i,sum1):
    if i < 1:
        return sum1
    sumParameter(i-1,sum1+i)


sumParameter(N,sum1)






# Functional way

N=3
# Backtracking
def sumN(N):
    if N==1:
        return 1
    sum1=N+ sumN(N-1)
    return sum1
    
output=sumN(N)
print(output)
    
    