'''
#Sum of array elements 
def Array_sum(nums):
    s = 0
    for i in range(len(nums)-1,-1,-1):
        s += nums[i]
    return s 
print(Array_sum([1,2,3,4,5]))

#Recursive approach
def Array_sum(nums):
    if index == -1:
        return 0
    return nums[index] + Array_sum(nums,index-1)

print(Array_sum([1,2,3,4,5]))
print(Array_sums([10, 20, 30, 40, 50]))

#Recursive Approach-1 
def Array_sum1(nums,index):
    if index == -1:
        return 0
    return nums[index] + Array_sum1(nums,index-1)
print(Array_sum1([1,2,3,4,5],4))

#Recursive Approach-2
def Array_sum2(nums):
    if len(nums) == 0:
        return 0
    return nums[-1] + Array_sum2(nums[:-1])

print(Array_sum2([1,2,3,4,5]))

#Reverse an Array
def Reverse_array(nums,i,j):
    if i >= j:
        return nums 
    nums[i],nums[j] = nums[j],nums[i]
    return Reverse_array(nums,i+1,j-1)

print(Reverse_array([1,2,3,4,5],0,4))

#Reverse a String
def Reverse_String(st):
    if len(st) == 0:
        return ""
    return st[-1] + Reverse_String(st[:-1])

print(Reverse_String("abc"))

def is_palindrome(st):
    return st == Reverse_String(st)

print(is_palindrome("abc"))
print(is_palindrome("abcba"))
'''
