def findMaxAverage(nums, k):
    currentSum = sum(nums[:k])
    maxSum = currentSum
    right = k
    left = 0

    if k ==1:
        return max(nums)

    for right in range(k, len(nums))
        currentSum  += nums[right] - nums[left]
        maxSum = max(maxSum, currentSum)
        left +=1
    print(maxSum/k)
    return maxSum/k


nums = [4,2,1,3,3]
k = 2
findMaxAverage(nums, k)
# 3.00000
'''         0 1   2  3  4 5
    nums = [1,12,-5,-6,50,3]

'''