"""
#Linear Search
def search(a, n, key):
    for i in range(0, n):
        if (a[i] == key):
            return i
    return -1

#Main code
l=int(input("Enter the length of the list"))
print("Enter the no. in list:") 
a=[]
for i in range(l):
  num=int(input())
  a.append(num)
print("Entered list is","\n",a)
key=int(input("Enter the key to be searched"))
n = len(a)
result = search(a, n, key)
if(result == -1):
    print(key,"is not present in array")
else:
    print(key,"is present at index", result)
print("Utsav", 222010308053)
"""
"""
#Binary Search
l=int(input("Enter the length of the list"))
print("Enter the no. in list:") 
a=[]
for i in range(l):
  num=int(input())
  a.append(num)
b=a.sort()
print("Entered list is","\n",a)
low=0
high=len(a)
key=int(input("Enter the key to be searched"))
while low!=high:
  mid=(low+high)//2
  if a[mid]==key:
    print(key,"found at index",mid)
    break
  elif a[mid]>key:
    high=mid-1
  elif a[mid]<key:
    low=mid+1
else:
  print(key,"not found")
print("Utsav", 222010308053)
"""