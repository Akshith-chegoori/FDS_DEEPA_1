lst = [1, 2, 3, 4, 5] 
k=2
b=[]
for i in range(len(lst)-1,-1,-1):
    val=lst.pop(i)
    lst.insert(i-2,val)
print(lst)