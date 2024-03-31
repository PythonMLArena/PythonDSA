# function calls itself its called Recursion 
# Program stop until specified condition is met


# Print Names n times 

user=10
def PrintNames(i,n):
    print("Name")
    if i>=n:
        return
    PrintNames(i+1,n)
    
    
#PrintNames(1,user)

# Print Linearly from 1 to N

N= 3
def Print1toN(i,n):
    print(i)
    if i>=n:
        return 
    Print1toN(i+1,n)
    
Print1toN(1,N)

# Print from N to 1

N= 3
def PrintNto1(N,i):
    if N<1:
        return 
    print(N)
    PrintNto1(N-1,i)
    
PrintNto1(N,N)