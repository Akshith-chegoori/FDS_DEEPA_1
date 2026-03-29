lst = [1, 2, 3, 4, 5, 6]
even=[]
odd=[]
for i in range (0,len(lst)):
    if i%2==0:
        even.append(lst[i])
    else:
        odd.append(lst[i])
print(even,odd)