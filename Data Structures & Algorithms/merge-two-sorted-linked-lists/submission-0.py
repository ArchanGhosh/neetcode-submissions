# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = list1

        curr_2 = list2
        
        dmp = ListNode()
        tail = dmp

        while curr_1 and curr_2:
            if curr_1.val <=curr_2.val:
                tail.next = curr_1
                curr_1 = curr_1.next
            else:
                tail.next = curr_2
                curr_2 = curr_2.next
            tail = tail.next

        if curr_1:
            tail.next = curr_1
        else:
            tail.next = curr_2
            
        return dmp.next
