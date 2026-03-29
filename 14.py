data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
z=len(data)
s1=0
max1=data[0]
min1=data[0]
for i in data:
    s1=s1+i
    if (i>max1):
        max1=i
    if(i<min1):
        min1=i
avg=s1/z
va1=0
for i in data:
    va1=va1+(i-avg)**2
var=va1/z
sd=var**0.5
ran=max1-min1
print(var,sd,ran)