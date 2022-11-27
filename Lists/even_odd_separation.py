def even_odd_separation(lst):
    odd, even = [], []
    for element in lst:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
    return odd, even

if __name__ == '__main__':
    lst = list(map(int, input().split()))
    odd, even = even_odd_separation(lst)
    print("odd: ", odd)
    print("even: ", even)