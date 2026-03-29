lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k=3
b=[]
c=[]
for i in range(k,len(lst)):
    b.append(lst[i])
for i in range(0,k):
    b.append(lst[i])
print(f"Left {b}")
for i in range(len(lst)-1,len(lst)-k-1,-1):
    c.append(lst[i])
for i in range(0,len(lst)-k):
    c.append(lst[i])
print(f"right{c}")