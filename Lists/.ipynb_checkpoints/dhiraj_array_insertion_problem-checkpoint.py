arr1 = list(map(int, input("Enter elements of first array: ").split()))
arr2 = list(map(int, input("Enter elements of second array: ").split()))
ins_index = int(input("Enter index to insert from: "))

arr1 = arr1[:ins_index]+arr2+arr1[ins_index:]
print(arr1)