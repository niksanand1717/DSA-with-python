strr = input("Enter string: ").split()
for i in range(len(strr)):
    strr[i] = strr[i][::-1]

strr = " ".join(strr)
print(strr)

