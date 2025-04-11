def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    newList = ListNode(-1)
    current = newList

    while head:
        if head.next and head.next.val == head.val:
            head = head.next
        else:
            current.next = head
            current = current.next
            head = head.next
    return newList.next