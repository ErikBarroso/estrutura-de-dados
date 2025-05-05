class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        one = 0
        two = 0
        left = 0

        while left < len(nums):
            if nums[left] == 0:
                zero += 1
            elif nums[left] == 1:
                one += 1
            else:
                two += 1
            left +=1
        nums[:] = [0] * zero + [1] * one + [2] * two