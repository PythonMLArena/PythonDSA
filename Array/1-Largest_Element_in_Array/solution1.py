# If arrya define globally all values initalize as 0 else garbage values
# 10^6 Maximum array can be defined ( if array define locally )
# if array declare globally then maximum value will be 10^7

# Largest of an array  
arr= [3,2,1,5,2]

# Brute Force 

arr.sort()

maxi=arr[-1]

print(maxi)


# Optimal Solution
arr= [3,2,1,5,2]

maxi=arr[0]

for i in arr :
    if i >= maxi:
        maxi = i

print(maxi)