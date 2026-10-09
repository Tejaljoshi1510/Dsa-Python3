def merge_lists(l1, l2):
    dummy = Node()
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next

        curr = curr.next

    curr.next = l1 if l1 else l2
    return dummy.next