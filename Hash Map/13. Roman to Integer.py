def romanToInt(nums):
    romans = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    result = 0
    for number in range(len(nums)-1):
        currente = romans[nums[number]]
        _next = romans[nums[number+1]]
        if currente < _next:
            result -= currente
        else:
            result += currente
    result += romans[nums[-1]]
    print(result)
    return result

s = "MCMXCIV"
romanToInt(s)
# Output: 1994