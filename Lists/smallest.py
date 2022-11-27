def find_smallest(lst):
    smallest = lst[0]
    for digit in lst:
        if smallest > digit:
            smallest = digit
    return smallest

if __name__ == '__main__':
    lst = list(map(int, input("Enter space separated numbers: ").split()))
    print("smallest:", find_smallest(lst))