  def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        mid = []

        for i in nums:
            if i > pivot:
                right.append(i)
            elif i < pivot:
                left.append(i)
            else:
                mid.append(i)
        return left+mid+right