p=[100,250,80,430,150]
new_p=[]
for i in p:
    if i>200:
         new_p.append(i * 0.9)
    else:       
         new_p.append(i * 0.95)
print(new_p)
