nums = [2, 5, 1, 8, 3, 9, 4, 7, 6]
rma=[]
rmi=[]
ma=0
mi=10000
for i in nums:
    if i >=ma:
        ma=i
    if i <= mi:
        mi=i
    rma.append(ma)
    rmi.append(mi)
print(rma)
print(rmi)