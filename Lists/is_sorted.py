def is_sorted(arr):
    if len(arr) <= 1: return True
    prev = arr[0]
    for x in arr[1:]:
        if x < prev: return False
        prev = x
    else: return True

if __name__ == '__main__':
    result = is_sorted(list(map(int, input("Enter array: ").split())))
    print("Yes" if result == True else "No")