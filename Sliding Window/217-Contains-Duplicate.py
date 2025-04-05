def containsDuplicate(nums):
    seen = set()
    for number in nums:
        if number in seen:
            return True
        see.add(number)
    return False