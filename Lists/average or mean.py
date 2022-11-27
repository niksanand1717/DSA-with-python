def mean_or_average(array):
    length = len(array)
    sum=0
    for i in array:
        sum+=i
    return sum/length


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    print(mean_or_average(lst))
