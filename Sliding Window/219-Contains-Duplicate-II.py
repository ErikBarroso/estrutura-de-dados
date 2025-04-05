def containsNearbyDuplicate(nums, k):
    lastIndex = {}
    for index, number in enumerate(nums):
        if number in lastIndex and index - lastIndex[number] <= k:
                return True
        lastIndex[number] = index
    return False

nums = [1,2,3,1,2,3]
k = 3
containsNearbyDuplicate(nums, k)

# Você deve verificar se há dois números duplicados onde a distância entre seus índices é menor ou igual a 3.
# Neste caso, nums[0] = 1 e nums[3] = 1, e a diferença entre seus índices é abs(0 - 3) = 3.
# Como a diferença 3 é menor ou igual a k(3), a resposta é verdadeira.