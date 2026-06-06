# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    newHead = None
    curr = head
    while curr:
        newHead = ListNode(curr.val, next=newHead)
        curr = curr.next
    return newHead

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        mergedList = ListNode()
        result = mergedList
        rHead = reverseList(head)
        i = 0
        
        while rHead or head:
            if rHead.val == head.val:
                mergedList.next = head
                mergedList.next.next = None
                break
            if i % 2 == 0:
                mergedList.next = head
                head = head.next
            else:
                mergedList.next = rHead
                rHead = rHead.next
            
            mergedList = mergedList.next
            i+=1
        
        head = result.next
            


        