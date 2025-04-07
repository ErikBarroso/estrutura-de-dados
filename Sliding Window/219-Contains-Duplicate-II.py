def containsNearbyDuplicate(nums, k):
    numbers = set()
    for i in range(len(nums)):
        numbers = set()
        if k == 0:
            return False
        for i in range(len(nums)):
            if nums[i] in numbers:
                return True
            if i >= k:
                numbers.discard(nums[i -k])
            numbers.add(nums[i])
        return False

nums = [99,99]
k = 2
containsNearbyDuplicate(nums, k)

# Você deve verificar se há dois números duplicados onde a distância entre seus índices é menor ou igual a 3.
# Neste caso, nums[0] = 1 e nums[3] = 1, e a diferença entre seus índices é abs(0 - 3) = 3.
# Como a diferença 3 é menor ou igual a k(3), a resposta é verdadeira.