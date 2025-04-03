def binary_search(nums, target, left, right):
        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid +1
            else:
                right = mid -1
        return -1

def exponetial_search(nums, target):
    if nums[0] == target:
        return 0
    left = 1

    while left < len(nums) and nums[left] < target:
        left *= 2

    right = min(left, len(nums) - 1)
    if nums[right] == target:
        return right
    return binary_search(nums, target, left//2, min(left,right))

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result= exponetial_search(nums, 20)

print(result)