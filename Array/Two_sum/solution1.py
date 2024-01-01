arr = [2,6,5,8,11]

target= 14

# Variety 1
# Yes or no if two value sum equal to target
k=False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] == target:
            k = True
            print("yes")
if not k:
    print("No")


# Variety 2
# return indexes of value sum equal to target
indexes= []
k=False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] == target:
            indexes.extend([i,j])
print(indexes)
