strr = str(input("Enter a string: "))

length = len(strr)
substr_list = []
for i in range(length):
    for j in range(i, length):
        substr = ""
        for k in range(i, j+1):
            substr += strr[k]
        substr_list.append(substr)

print(sorted(substr_list))
