x = [1,2,3,4,5]
y = [2,4,5,4,5]
avg1=sum(x)/len(x)
avg2=sum(y)/len(y)
p=0
ja1=0
ja2=0
for i in range(0,len(x)):
    p=(x[i]-avg1)*(y[i]-avg2)+p
    ja1=(x[i]-avg1)**2+ja1
    ja2=(y[i]-avg2)**2+ja2
p2=(ja1*ja2)**0.5
r=p/p2
print(r)