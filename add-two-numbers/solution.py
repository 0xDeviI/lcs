from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_value = ""
        l2_value = ""
        current_iterator: ListNode = l1
        while (current_iterator != None):
            l1_value += str(current_iterator.val)
            current_iterator = current_iterator.next
        l1_value = l1_value[::-1]
        
        current_iterator: ListNode = l2
        while (current_iterator != None):
            l2_value += str(current_iterator.val)
            current_iterator = current_iterator.next
        l2_value = l2_value[::-1]
        
        numerical_result = str(int(l1_value) + int(l2_value))[::-1]
        result_size = len(numerical_result)
        result: Optional[ListNode] = ListNode()
        current_iterator = result
        for i in range(result_size):
            current_iterator.val = int(numerical_result[i])
            if (i != result_size - 1):
                current_iterator.next = ListNode()
                current_iterator = current_iterator.next
            else:
                break
        return result