lst = input("Enter array: ")
sub_string = input("Enter sub str: ")
subarr = []
length = len(lst)
for i in range(length):
    for j in range(i, length):
        arr = ""
        for k in range(i, j+1):
            # print(lst[k], end=" ")
            arr += lst[k]
        subarr.append(arr)
        # print()

count = 0
for i in subarr:
    if i == sub_string:
        count += 1

print(subarr)
print(count)