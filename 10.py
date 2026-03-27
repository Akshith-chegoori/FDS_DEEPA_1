lst = [5, 3, 8, 1, 9, 2, 7]
s=0
for _ in lst:
    s=s+_
a=s//len(lst)
b=[]
c=[]
for i in lst:
    if i<a:
        b.append(i)
    else:
        c.append(i)
print(a,b,c)