# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def revList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        counter = 0
        dummynode = ListNode(val=0, next=head)
        curr = dummynode

        if left == right:
            return curr.next
        
        while curr:
            if counter == left-1:
                prev, start = curr, curr.next

            elif counter == right:
                end, after = curr, curr.next

            curr = curr.next
            counter += 1

        end.next = None

        new_head = self.revList(start)
        
        prev.next, start.next = new_head, after

        return dummynode.next