arr = [1,2,3,5]


N=5

# Brute Force Solution

for i in range(1,N+1):
    if i in arr:
        continue
    else:
        print(i)

# Hasing (Better Solution)
        
Hash_Array = [0]*N 

for  i in range(1,N+1):
    if i in arr:
        Hash_Array[i-1] = 1

print(Hash_Array)
index=0
for i in Hash_Array:
    if i == 0:
        print(index+1) 
        break   
    index += 1    