
def reverseWords(string):
    newString = ''
    left, right = 0, 0

    while right < len(string):
        if string[right] == ' ':
            newString += string[left:right][::-1] + ' '
            right += 1
            left = right
        right += 1
    newString += string[left:right][::-1]
    print(newString)
        

reverseWords('erik teste barroso')