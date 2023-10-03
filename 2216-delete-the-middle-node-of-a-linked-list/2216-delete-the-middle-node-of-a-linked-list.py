# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        # count number of elements in list to get mid
        list_nodes = [head]
        node = head
        while node.next is not None:
            node = node.next
            list_nodes.append(node)
        num_nodes = len(list_nodes)
        mid = int(num_nodes / 2)
        # set prev of mid's `next` to point to `ListNode` after mid
        if mid-1 >= 0:
            if mid+1 < num_nodes:
                list_nodes[mid-1].next = list_nodes[mid+1]
            else:
                head.next = None
        return head
        