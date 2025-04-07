def findMaxAverage(nums, k):
    currentSum = sum(nums[:k])
    maxSum = currentSum
    result = nums[:k]
    for i in range(k, len(nums)):
        currentSum += nums[i] - nums[i-k]
        if currentSum > maxSum:
            maxSum = currentSum
            result = nums[i - k + 1:i+1]
    print(result)
    return result


nums = [2, 1, 5, 1, 3, 2]
k = 3  
#Output: [5, 1, 3]
findMaxAverage(nums, k)
#Dado um array de inteiros nums e um inteiro k, encontre o subarray de tamanho exato k que tenha a maior soma possível e retorne esse próprio subarray (não a média e nem a soma).