from typing import Optional

# Definição da classe ListNode (estrutura da lista ligada)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Só pra facilitar visualização no print
    def __str__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ahead = head
        while ahead and ahead.next:
           ahead = ahead.next.next
           head = head.next
        return head


# Função pra criar a lista ligada a partir de uma lista normal
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Função pra converter de volta pra lista normal (pra printar no teste)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Teste
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7]
    head = build_linked_list(values)

    solution = Solution()
    reversed_head = solution.reverseList(head)

    print(linked_list_to_list(reversed_head))  
