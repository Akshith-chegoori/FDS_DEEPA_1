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
