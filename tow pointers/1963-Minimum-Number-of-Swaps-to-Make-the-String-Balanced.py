   def minSwaps(self, s: str) -> int:
        balance = 0 
        max_unbalance = 0

        for i in s:
            if i == '[':
                balance +=1
            elif i == ']':
                balance -=1
            if balance < 0:
                max_unbalance = max(max_unbalance, -balance)
        return (max_unbalance + 1) // 2