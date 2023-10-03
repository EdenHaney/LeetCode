# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur_node = head
        next_node = head.next
        head.next = None
        while next_node is not None:
            # record current.next.next
            after_next = next_node.next
            # set current.next.next = current
            next_node.next = cur_node
            # move on 
            cur_node = next_node
            next_node = after_next
        return cur_node

        