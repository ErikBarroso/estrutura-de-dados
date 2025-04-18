def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    lastNumber1 = m - 1 
    lastNumber2 = n - 1
    right = m + n-1

    while lastNumber2 >=0:
        if lastNumber1 >= 0 and nums1[lastNumber1] > nums2[lastNumber2]:
            nums1[right] = nums1[lastNumber1]
            lastNumber1 -= 1
        else:
            nums1[right] = nums2[lastNumber2]
            lastNumber2 -=1
        right -=1