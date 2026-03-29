data =[55, 60, 48, 72, 95, 88, 34, 76, 62, 81]
z=len(data)
s1=0
for i in data:
    s1=s1+i
avg=s1/z
va1=0
for i in data:
    va1=va1+(i-avg)**2
var=va1/z
sd=var**0.5
wit=[]
for i in data:
    if avg-sd<=i and i<=avg +sd:
        wit.append(i)
print(len(wit),wit)