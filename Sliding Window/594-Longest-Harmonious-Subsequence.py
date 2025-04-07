def findLHS(nums):
    left, right = 0, 0
    subSequenceSize = 0
    nums.sort()

    for right in range(len(nums)):
        while nums[right] - nums[left] > 1:
            left +=1
        if nums[right] - nums[left] == 1:
            subSequenceSize = max(subSequenceSize, right - left +1)
                
    print(subSequenceSize)
    return subSequenceSize
            

findLHS([1,3,2,2,5,2,3,7])
 # retornar um subsequence
 #diferenã entre maior e menor numero seja 1