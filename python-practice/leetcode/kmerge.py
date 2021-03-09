class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: list()) -> ListNode:
    q = list()
    for node in lists:
        if node != None:
            q.append(node)
    head = ListNode()
    point = head
    while q:
        min_num = 0
        for i in range(len(q)):
            if q[i].val < q[min_num].val:
                min_num = i
        point.next = q.pop(min_num)
        point = point.next
        nextN = point.next
        if nextN != None:
            q.append(nextN)
    return head.next


def mergeKLists2(lists: list()) -> ListNode:
    if len(lists) == 0:
        return None
    intvl = 1
    while intvl < len(lists):
        i = 0
        while i + intvl < len(lists):
            lists[i] = merge2List(lists[i], lists[i + intvl])
            i = i + intvl * 2
        intvl *= 2
    return lists[0]


def mergeKLists3(lists: list()) -> ListNode:
    c = []
    h = ListNode()
    t = h
    for l in lists:
        while l != None:
            c.append(l.val)
            l = l.next
    c.sort()
    for i in c:
        t.next = ListNode(i)
        t = t.next
    return h.next


def merge2List(listnode1, listnode2) -> ListNode:
    head = ListNode()
    ans = head
    while listnode1 != None and listnode2 != None:
        if listnode1.val < listnode2.val:
            head.next = listnode1
            head = head.next
            listnode1 = listnode1.next
        else:
            head.next = listnode2
            head = head.next
            listnode2 = listnode2.next
    if listnode1 == None:
        head.next = listnode2
    if listnode2 == None:
        head.next = listnode1
    return ans.next


if __name__ == "__main__":
    input_list = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ]
    result_node = mergeKLists3(input_list)
    output_node = result_node
    while output_node != None:
        print(output_node.val)
        output_node = output_node.next
