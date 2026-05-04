#LeetCode 560. Subarray Sum Equals K
#Given an array of integers and an integer k, you need to find the total number of
#continuous subarrays whose sum equals to k.
from collections import defaultdict
li = list(map(int, input().split()))
k = int(input())
count = 0
prefix_sum = 0
freq = defaultdict(int)
freq[0] = 1 
for num in li:
    prefix_sum += num
    count += freq[prefix_sum - k]
    freq[prefix_sum] += 1
print(count)
