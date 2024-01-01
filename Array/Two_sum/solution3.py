# Two Pointers Approach Greedy Approach

arr = [2,6,5,8,11]

target= 91

arr.sort()
print(arr)
left ,right = 0 ,len(arr)-1
k=False
while left < right:
    if arr[left] + arr[right] > target:
        right-=1
    elif arr[left] + arr[right] < target:
        left+=1
    else:
        k=True
        print("yes",left,right)
        break


if not k:
    print("No")

