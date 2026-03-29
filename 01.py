n=10
l=[]
a=[2,4,6,8,10]
for i in range (0,n):
    l.append(i+1)
print(l)
i=0
while(i<5):
    l.remove(a[i])
    i=i+1
print(l)