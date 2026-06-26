# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        hashmap = {}

        # Store nodes grouped by their values
        for head in lists:
            curr = head
            while curr:
                nxt = curr.next          # Save next before disconnecting
                curr.next = None         # Break old link
                hashmap.setdefault(curr.val, []).append(curr)
                curr = nxt

        # Reconnect nodes in sorted order
        for key in sorted(hashmap.keys()):
            for node in hashmap[key]:
                tail.next = node
                tail = node

        tail.next = None
        return dummy.next