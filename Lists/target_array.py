def fun(nums, index):
    target = []*len(nums)
    for i in range(len(nums)):
        target = target[:index[i]]+[nums[i]]+target[index[i]:]
    
    return target

# nums = [0,1,2,3,4]
# index = [0,1,2,2,1]

# nums = [1,2,3,4,0]
# index = [0,1,2,3,0]

nums = [1]
index = [0]


print(fun(nums, index))