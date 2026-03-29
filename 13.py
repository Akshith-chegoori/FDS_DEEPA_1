scores = [85, 92, 78, 95, 88, 72, 91,95]
s=0
for i in scores:
    s=s+i
mean=s/len(scores)
scores.sort()
median=scores[len(scores)//2]
di={}
for i in scores:
    if i in di:
        di[i]+=1
    else:
        di[i]=1
mmmm=max(di.values())
mode=[]
for i in di:
    if di[i]==mmmm:
        mode.append(i)
print(mean,median,mode)