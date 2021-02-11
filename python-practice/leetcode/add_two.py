# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two(list1, list2):
    dummy_head = ListNode()
    p = list1
    q = list2
    current = dummy_head
    carry = 0
    while p != None or q != None:

        x = p.val if (p != None) else 0
        y = q.val if (q != None) else 0
        print(x, y)
        sum_val = carry + x + y
        carry = int(sum_val / 10)
        current.next = ListNode(sum_val % 10)
        current = current.next
        if p != None:
            p = p.next
        if q != None:
            q = q.next
    if carry > 0:
        current.next = ListNode(carry)

    return dummy_head.next


def reverse_listnode(l):
    new_head = ListNode()
    if l == None or l.next == None:
        return l
    new_head = reverse_listnode(l.next)
    l.next.next = l
    l.next = None

    return new_head


if __name__ == '__main__':
    """
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
    """
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    #l1 = ListNode(1,ListNode(8))
    #l2 = ListNode(0)
    result_list = add_two(l1, l2)
    result_cur = result_list
    result = ""
    while result_cur != None:
        result += str(result_cur.val)
        result_cur = result_cur.next
    print(result)
