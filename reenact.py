

def subsets(nums):
    res = [[]]
    for num in nums:
        newArr = []
        for item in res:
            newArr.append(item + [num])
        res += newArr
    return res

print(subsets([1,2,3]))