# FInding max while Moving ahead from backward

arr= [10,22,12,3,0,6]
max=0
leaders=[]


for i in range(len(arr)-1,0,-1):
    if arr[i]>max:
        max=arr[i]
        leaders.append(max)

print(len(leaders),leaders)