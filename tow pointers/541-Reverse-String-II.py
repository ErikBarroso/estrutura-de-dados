def reverseStr(string, number):
    left = 0
    right = number
    newString = ''

    for i in range(0, len(string), 2 * number):
        if len(string) - 1 < number:
            newString += string[::-1]
            print(f'1 {newString}')

        newString += string[i:i+number][::-1]
        newString += string[i+number:i+number*2]
        print(string[i])
    if len(string) - 1 >= number and len(string) -1 < (number * 2):
        newString += string[i:i+number][::-1]
        print(f'2 {newString}')
    print(newString)


reverseStr('abcd', 2)

        # newString += string[left:right][::-1]
        # left = right
        # right += number
        # newString += string[left:right]
        
        # left = right
        # right += number
        # if len(string) - right < 2:
        #     newString += string[left:right][::-1]
        #     left = right
        # if  len(string) - right < number * 2 and  len(string) - right >= number:
        #     newString += string[left:right][::-1]
    # print(newString)
    

# inverter os primeiros 2 para cada 4 de caractere
# se houver menos de 2 caracteres restante, inverter todos

# se menos de 4, mas >= a 2 caracteres, inverter os 1º 2 e deixar os outros originais 
#https://leetcode.com/problems/reverse-string-ii/description/

# A B C D E F G H
#   1[]