# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not n or not head: return head
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy
        count = n + 1

        while fast:
            if count:
                fast = fast.next
                count-=1
                continue
            else:
                slow = slow.next
                fast = fast.next

        if not slow.next:
            slow = None
            return
        else:
            slow.next = slow.next.next

        return dummy.next
        

#  1>2>3>4 2nd
#f       ^
#s   ^

        