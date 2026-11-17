# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Starting with empty back hand (prev) and front hand on the first train car (curr)
        prev, curr = None, head

        # loop until the front hand reaches the end of the train (None)
        while curr:
            next_temp = curr.next # 1. save the next car so it does not get lost
            curr.next = prev      # 2. flip the current car's hook to point backward
            prev = curr           # 3. slide back hand forward to the current car
            curr = next_temp      # 4. slide front hand forward to the saved next car
            
        # "curr" is now None (off the tracks); "prev" holds the new front of the train
        return prev
