def maximumLengthSubstring(string):
        left, right = 0, 0
        _max = 1
        counter = {}
        counter[string[0]] = 1

        while right < len(string) -1:
            right += 1
            if counter.get(string[right]):
                counter[string[right]] += 1
            else:
                counter[string[right]] = 1

            while counter[string[right]] == 3:
                counter[string[left]] -= 1
                left += 1
            _max = max(_max, right-left+1)
        return _max

maximumLengthSubstring('bcbbbcba')
#saida 4