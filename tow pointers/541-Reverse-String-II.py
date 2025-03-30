def reverseStr(string, number):
    right = number
    newString = ''

    for i in range(0, len(string), 2 * number):
        print(len(string) -i)
        if len(string) < number:
            newString += string[i:i+number][::-1]
            continue
            print(f'1 {newString}')

        if len(string) -i >= number and len(string) -i < (number * 2):
            newString += string[i:i+number][::-1]
            newString += string[i+number:i+number*2]
            continue
            print(f'2 {newString}')

        newString += string[i:i+number][::-1]
        print(f'3 {newString}')
        newString += string[i+number:i+number*2]
        print(f'4 {newString}')
    print(newString)


reverseStr('a', 2)
