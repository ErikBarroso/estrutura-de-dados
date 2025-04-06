def findLHS(nums):
    subSequence = {}
    subSequenceSize = 0

    for number in nums:
        if number in subSequence:
            subSequence[number] += 1
        else:
            subSequence[number] = 1
    for number in subSequence:
        if number+1 in subSequence:
            subSequenceSize = max(subSequenceSize, subSequence[number] + subSequence[number+1])
    print(subSequenceSize)
    return subSequenceSize
            

findLHS([1,3,2,2,5,2,3,7])
 # retornar um subsequence
 #diferenã entre maior e menor numero seja 1