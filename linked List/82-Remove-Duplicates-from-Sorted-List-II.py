def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    newList = ListNode(-1)
    current = newList
    duplicate = None
    while head:
        if head.next and head.val == head.next.val:
            duplicate = head.val
            while head and duplicate == head.val:
                head = head.next
        elif head.val != duplicate:
            current.next = head
            current = current.next
            head = head.next
            current.next = None 
        else:
            head = head.next
    return newList.next     

# ## GTP me ajudou a melhorar
# def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#     newList = ListNode(0, head)
#     current = newList
#     while head:
#         if head.next and head.val == head.next.val:
#             while head.next and head.next.val == head.val:
#                 head = head.next
#             current.next = head.next
#         else:
#             current = head
#         head = head.next
#     return newList.next