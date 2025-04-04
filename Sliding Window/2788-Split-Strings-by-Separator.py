def splitWordsBySeparator(words, separator):
    result = []
    for word in words:
        left, right = 0, 0
        while right <= len(word) -1:
            if word[right] == separator:
                if word[left:right] != "":
                    result.append(word[left:right])
                left = right +1
            right += 1
        if left < len(word) and word[left:] != "":
            result.append(word[left:])
    print(result)
    return result

words = ["$easy$","$problem$"]
separator = "$"
splitWordsBySeparator(words, separator)