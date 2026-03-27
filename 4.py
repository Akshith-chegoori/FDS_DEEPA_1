a= [3, 1, 4, 1, 5, 9, 2, 6, 5]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)