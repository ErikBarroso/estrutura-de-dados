def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newList = ListNode(-1)
        current = newList

        while head:
            if head.val == val:
                head = head.next
                current.next = None
            else:
                current.next = head
                current = current.next
                head = head.next
        return newList.next


#GPT
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next