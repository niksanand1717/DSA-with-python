lst = list(map(int, input("Enter array: ").split()))
diff = int(input("Enter diff: "))
length = len(lst)
for i in range(length):
    for j in range(i, length):
        for k in range(j, length):
            if lst[k] - lst[j] == diff and lst[j] == lst[i] == diff:
                print([i, j , k])
        
        # print()