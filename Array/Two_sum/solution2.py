# Let do Hashing 

arr = [2,6,5,8,11]

target= 16

HashMap={}
indexes= []
for i in range(len(arr)):
    search= abs(arr[i]-target)
    if search in HashMap:
        indexes.extend([HashMap[search],i])
    else:
        HashMap[arr[i]] = i

print(indexes)