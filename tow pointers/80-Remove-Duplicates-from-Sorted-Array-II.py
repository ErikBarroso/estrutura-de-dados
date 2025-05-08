class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0

        while right < len(nums):
            if left < 2 or nums[right] != nums[left -2]:
                nums[left] = nums[right]
                left +=1
            right +=1
        return left