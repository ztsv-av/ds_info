from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    dummy = ListNode()
    tail = dummy

    curr1, curr2 = list1, list2

    while curr1 and curr2:
        if curr1.val <= curr2.val:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next
        tail = tail.next

    tail.next = curr1 if curr1 else curr2

    return dummy.next
