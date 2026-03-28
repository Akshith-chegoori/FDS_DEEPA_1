<<<<<<< HEAD
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
=======
n=[2,5,1,8,3,9,4,7,6]
max=[]
maximum=n[0]
for i in n:
    if i>maximum:
        maximum=i
    max.append(maximum)

min=[]
minimum=n[0]
for i in n:
    if i<minimum:
        minimum=i
    min.append(minimum)

print("running_max  = ",max)
print("running_min = ",min)
>>>>>>> c3a4c4207ad1f0b49f87511129a72a30736d84db
