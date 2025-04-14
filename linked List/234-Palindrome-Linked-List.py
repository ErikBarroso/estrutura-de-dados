def isPalindrome(self, head: Optional[ListNode]) -> bool:
    fast = head
    slow = head
    firstHalf = head
    newList = None

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    while slow:
        next_node = slow.next
        slow.next = newList
        newList = slow
        slow = next_node
    while newList and firstHalf:
        if newList.val != firstHalf.val:
            return False
        newList = newList.next
        firstHalf = firstHalf.next
    return True