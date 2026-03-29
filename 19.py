lst = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
n = 3

b = []

for i in range(0, len(lst), n):
    b.append(lst[i:i+n])

print(b)