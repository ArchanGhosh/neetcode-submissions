class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt


        first, second = head, prev
        while second:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2