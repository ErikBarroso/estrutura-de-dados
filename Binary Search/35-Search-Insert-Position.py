def searchInsert(nums, target):
    left = 0
    right = len(nums) -1

    while left < right:
        mid = int((left+right)/2)

        if nums[mid] == target:
            print(f' achei {mid}')
            return mid

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return mid

searchInsert([1,3,5,6], 7)