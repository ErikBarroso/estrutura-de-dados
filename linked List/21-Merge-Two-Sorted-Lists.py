#Primeira logica
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    newList = ListNode(-1)
    current = newList

    while list1 and list2:
        if list1 and list1.val == list2.val:
            current.next = list1 
            list1 = list1.next
        elif list2 and list1 and list2.val > list1.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2 
            list2 = list2.next
        current = current.next
    current.next = list1 if list1 else list2
    return newList.next


#rafatorado com ajuda do gpt me mostrando outro ponto de vista
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    newList = ListNode(-1)
    current = newList

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1 
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 if list1 else list2 
    return newList.next