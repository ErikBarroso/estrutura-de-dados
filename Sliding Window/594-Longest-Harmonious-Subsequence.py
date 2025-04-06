def findLHS(nums):
    lef, right = 0, 0
    subSequence = {}
    subSequence[nums[0]] = 1
    subSequenceSize = 0

    while right < len(nums) -1:
        right += 1
        if subSequence.get(nums[right]):
            subSequence[nums[right]] += 1
        else:
            subSequence[nums[right]] = 1
    for number in subSequence:
        print(len(subSequence))
         if number+1 in subSequence and len(subSequence) < (subSequence[number] + subSequence[number+1]):
            subSequenceSize = subSequence[number] + subSequence[number+1]
    print(subSequenceSize)
    return subSequenceSize
            

findLHS([1,3,2,2,5,2,3,7])
 # retornar um subsequence
 #diferenã entre maior e menor numero seja 1