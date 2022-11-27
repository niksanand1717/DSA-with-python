# find element that is present odd number of times.
# only one integer can be present in array that appear odd number of times

def find_odd_occurence(arr):
    result = None
    if len(arr) < 1: return result
    elif len(arr) == 1: return arr[0]
    else:
        result = arr[0]
        for digit in arr[1:]:
            result = result ^ digit
    return result


print(find_odd_occurence(list(map(int, input("Enter numbers: ").split()))))