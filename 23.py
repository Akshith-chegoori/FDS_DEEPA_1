lst = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(lst) // 2
result = []
for i in range(n):
    result.append(lst[i])       
    result.append(lst[i + n])   
print(result)