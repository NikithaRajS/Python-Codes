
n = int(input())
arr = map(int, input().split())
array=set(arr)
narray=list(array)
narray.sort()
no=len(narray)
print(narray[no-2])

