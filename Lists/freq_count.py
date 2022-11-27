strr = "abacbd"

count = []

strr = sorted(strr)

c=1
prev = strr[0]
for i in strr[1:]:
    if i == prev:
        c += 1
    elif i != prev:
        count.append(c)
        prev = i
        c = 1
count.append(c)
strr = sorted(set(strr))
# print(strr)
# print(count)
strr2 = ""
for i in range(len(strr)):
    strr2 += strr[i]+str(count[i])

print(strr2)

