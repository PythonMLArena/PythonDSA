arr = [1,2,4,7,7,5]

# Find Second Largest Element
largest = arr[0]
second_largest = -1
for i in arr[1:]:
    if i>largest:
        second_largest = largest
        largest = i
    elif i< largest and i>second_largest:
        second_largest=i

print(largest, second_largest)