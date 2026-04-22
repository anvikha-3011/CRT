def Binary_search(nums,target):
    low,high = 0,len(nums)-1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

li = list(map(int, input().split()))
target = int(input())
print(Binary_search(li, target))

#LeetCode 35. Search Insert Position
def search_insert(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

li = list(map(int, input().split()))
target = int(input())
print(search_insert(li, target))

#LeetCode 875. Koko Eating Bananas
def min_eating_speed(piles, h):
    def can_eat(speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        return hours <= h

    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if can_eat(mid):
            right = mid
        else:
            left = mid + 1
    return left     
piles = list(map(int, input().split()))
h = int(input())
print(min_eating_speed(piles, h))
