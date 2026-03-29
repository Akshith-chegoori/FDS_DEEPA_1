a = [1, 3, 5, 7] 
b = [2, 4, 6, 8]
c=[]
z=len(a+b)
k=0
j=0
for i in range (0,z):
    if i%2==0:
        c.append(a[j])
        j=j+1
    else:
        c.append(b[k])
        k=k+1
print(c)