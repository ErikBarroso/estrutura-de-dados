def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')

        for index, i in enumerate(words):
            if i.startswith(searchWord):
                return index+1
        return -1