def second_largest(arr):
    if len(arr) <= 1: return None
    lar = arr[0]
    slar = None
    for x in arr[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or slar < x :
                slar = x
    return slar

print(second_largest(list(map(int, input().split()))))