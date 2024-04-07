arr=[1,2,3,4,5,6]

# Recursion
l=0
r=len(arr)-1

def func(l,r):
    if l>r:
        return 
    arr[l],arr[r]=arr[r],arr[l]
    func(l+1,r-1)
func(l,r)
print("final",arr)
    