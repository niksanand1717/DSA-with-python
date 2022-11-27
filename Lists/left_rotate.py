def left_rotate(arr, by):

    # arr = arr[by:] + arr[:by] 


    for j in range(by % len(arr)):
        temp = arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[-1] = temp

    return arr

if __name__ == "__main__":
    arr = list(map(int, input("Enter an array: ").split()))
    no_of_times = int(input("Input number of times: "))
    print(left_rotate(arr, no_of_times))