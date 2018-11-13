from ListNode import ListNode

def mergeTwoSortedList(L1, L2):
    dummyHead = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummyHead.next

L1 = ListNode(1)
L1.next = ListNode(4)
L1.next.next = ListNode(7)

L2 = ListNode(2)
L2.next = ListNode(3)
L2.next.next = ListNode(9)

result = mergeTwoSortedList(L1, L2)

while result:
    print result.data
    result = result.next
