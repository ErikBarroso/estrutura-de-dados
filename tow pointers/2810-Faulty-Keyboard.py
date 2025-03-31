def finalString(self, string):
    newString = ''
    right = 0

    while right < len(string):
        if string[right] != 'i':
            newString += string[right]
            right += 1
            continue

        if string[right -1] == 'i':
            newString = newString[:right][::-1]
            right += 1
            continue
        
        newString = newString[:right][::-1]
        right += 1
    return newString
finalString('viwif')

# def finalString(string):
#     newString = ''

#     for i in string:
#         if i != 'i':
#             newString += i
#         else:
#             newString = newString[::-1]
#     print(newString)


# finalString('viwif')
# Solução q vi no leetcode