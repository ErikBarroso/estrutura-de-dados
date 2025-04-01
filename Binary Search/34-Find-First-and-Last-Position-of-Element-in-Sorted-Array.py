def searchRange(nums, target):
    # solução do neetcode
    first = binSearch(nums, target, True)
    last = binSearch(nums, target, False)
    return [first, last]

def binSearch(nums, target, isLeft):
    left = 0
    right = len(nums) -1
    itemFound = -1 

    while left > right:
        mid = (left+right) // 2
        if nums[mid] > target:
            right = mid -1
        elif nums[mid] < target:
            left = mid +1
        else:
            itemFound = mid
            if isLeft:
                right = mid -1
            else:
                left = mid +1
    return itemFound


searchRange([1], 1)

#   def searchRange(self, nums, target):
#         left = 0
#         targets = []
        
#         if len(nums) == 1 and nums[0] == target:
#             return [0, 0]
#         elif len(nums) == 1 and nums[0] != target:
#             return [-1, -1]

#         while left <= len(nums) -1:
#             if nums[left] == target:
#                 targets += [left]
#                 left += 1
#             left += 1

#         if not targets:
#             return [-1, -1]

#         if len(targets) == 1:
#             return [targets[0],targets[0]]

#         return [targets[0],targets[-1]]