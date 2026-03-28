nums = [2, 5, 1, 8, 3, 9, 4, 7, 6]
rmaxi=[]
rmi=[]
ma=0
mi=10000
for i in nums:
    if i >=ma:
        ma=i
    if i <= mi:
        mi=i
    rmaxi.append(ma)
    rmi.append(mi)
print(rmaxi)
print(rmi)