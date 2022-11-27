num1 = 6
num2 = [4,4,7,8,8,8,9]

res = []
for i in range(len(num2)):
    for j in range(i+1, len(num2)):
        if num2[i] == num2[j]:
            res.append(num2[i])
    
print(res)