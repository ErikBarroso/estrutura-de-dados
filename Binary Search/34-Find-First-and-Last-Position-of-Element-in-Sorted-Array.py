class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        targets = {}
        
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        elif len(nums) == 1 and nums[0] != target:
            return [-1, -1]

        while left <= len(nums) -1:
            if nums[left] == target:
                targets += [left]
                left += 1
                continue
            left += 1

        if len(targets) == 0:
            return [-1, -1]

        if len(targets) == 1:
            return [targets[0],targets[0]]

        return [targets[0],targets[-1]]
            