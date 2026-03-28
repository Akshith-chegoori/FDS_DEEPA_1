a = [1,2,3,4,5,6,7,6,4,11,12,13,14,15,16,17,18,19,20,21,24,23,22]
cm=0
b=[]
d=0
for i in range (0,len(a)):
    j=i+1
    c=0
    while(j<len(a) and a[j-1]<a[j]):
            c+=1
            j+=1
    if(c>cm):
        cm=c
print(cm)