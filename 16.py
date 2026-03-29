sales = [120, 135, 98, 142, 167, 155, 110, 178, 145, 132, 160, 148]
avg=sum(sales)/len(sales)
mab=[]
pct=[]
for i in sales:
    if i>=avg:
        mab.append(i)
for i in range (1,len(sales)):
    j = ((sales[i]-sales[i-1])/sales[i-1])*100
    pct.append(j)
pct.insert(0,sales[0])
print(pct,mab)