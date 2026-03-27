a=['a', 'b', 'c', 'd', 'e']
b=tuple(a)
c=len(a)
i=0
for j in range(c-1,-1,-1):
        a[i]=b[j]
        i=i+1
print(a)