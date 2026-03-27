t=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
di={}
for i in t:
     di[i] = di.get(i, 0) + 1
print(di)