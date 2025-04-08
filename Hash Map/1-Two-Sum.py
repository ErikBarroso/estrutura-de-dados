def twoSum(nums, target):
    numbers = {}

    for index, num in enumerate(nums):
        difference = target - num
        if difference in numbers:
            print([numbers[difference], index])
            return [numbers[difference], index]
        numbers[num] = index

nums = [3,2,3]
target = 6
twoSum(nums, target)