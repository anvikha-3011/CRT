#Sum of array elements 
def Array_sum(nums):
    s = 0
    for i in range(len(nums)):
        s += nums[i]
    return s 
print(Array_sum([1,2,3,4,5]))