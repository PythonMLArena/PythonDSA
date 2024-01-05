arr = [1,2,4,7,7,5]

# FInd Second Largest Element


# Brute Force Solution 1

arr.sort(reverse=True) # O(nlogn) Merge Sort
largest = arr[0]

for i in arr: # O(n)
    if i!=largest:
        print(i)
        break

# Final Complexity = O(nlogn) + O(n)
    
# Brute Force Solution 2
    
largest = arr[0]

for i in arr :
    if i>=largest:
        largest = i

print("Largest",largest)

second_largest = 0

for i in arr :
    if i!=largest and i> second_largest:
        second_largest = i

print("Second",second_largest)

# Final Complexity = O(n) + O(n)