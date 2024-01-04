# Everything Right is a smaller 

arr= [10,22,12,3,0,6]

# last element is a leader


# Brute Force Solution1
leaders = []
for i in range(len(arr)-1):
    if max(arr[i+1:])> arr[i]:
        continue
    else:
        leaders.append(arr[i])
leaders.append(arr[-1])

print(leaders)
# Brute Force Solution2
leaders = []
for i in range(len(arr)):
    k=True
    for j in range(i+1,len(arr)):
        if arr[j]> arr[i]:
            k=False
            break
    if k==True:
        leaders.append(arr[i])

print(leaders)
# Time Complexity O(n^2) (Near about)
# Space Complexity O(n) 