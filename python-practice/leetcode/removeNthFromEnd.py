# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# delete the last n node
# 1. go through the list to get the length, and length - n will be the index of the element to be removed: O(L)
# 2. use two pointer to walk through the list parallelly
# we use the method 2
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
	dummy = ListNode()
	dummy.next = head
	first_ptr = dummy
	second_ptr = dummy
	
	for i in range(0,n):
		first_ptr = first_ptr.next

	while first_ptr.next:
		first_ptr = first_ptr.next
		second_ptr = second_ptr.next

	second_ptr.next = second_ptr.next.next
	return dummy.next


        