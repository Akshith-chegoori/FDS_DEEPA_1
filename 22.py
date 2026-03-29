lst = [1, 2, 3, 4, 5, 6]
ev=[]
od=[]
for i in lst:
    if i % 2 == 0 :
        ev.append(i)
    else:
        od.append(i)
print(ev+od)