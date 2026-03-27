a= [10, 20, 30, 40, 50, 60]
b=[]
for i in range(0,len(a)):
    if a[i]>25:
        b.append(i)
print(b)