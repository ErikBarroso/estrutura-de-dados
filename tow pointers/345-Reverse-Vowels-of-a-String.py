def reverseStr(string):
    left = 0
    right = len(string) -1
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string = list(string)

    while left < right:
        if string[left] not in vowels:
            left += 1

        elif string[right] not in vowels:
            right -= 1

        else:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

    string = ''.join(string)
    print(string)


reverseStr('race a car')
# invertendo a primeira vogal com a ultima
# Output: "raca e car"