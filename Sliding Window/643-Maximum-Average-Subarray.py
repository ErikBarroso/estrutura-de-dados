def findMaxAverage(nums, k):
    currentSum = sum(nums[:k])
    maxSum = currentSum
    left = 0

    if k == 1:
        return max(nums)
    if len(nums) == 1:
        return nums[0]
    if len(nums) == k :
        return sum(nums) / k

    for right in range(k, len(nums)):
        currentSum  += nums[right] - nums[left]
        maxSum = max(maxSum, currentSum)
        left +=1
    return maxSum/k


nums = [1,12,-5,-6,50,3]
k = 4
findMaxAverage(nums, k)
