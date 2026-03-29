nums= [3, 1, 4, 1, 5, 9, 2, 6, 5]
ma=0
mi=1000
ma2=0
mi2=1000
for i in nums:
    if(i >ma):
        ma=i
    elif(i<ma and i >ma2):
        ma2=i
    if(i<mi):
        mi=i
    elif(i>mi and i <mi2):
        mi2=i
print(ma,ma2,mi2,mi)