"""
Problem: Reverse Linked List
Platform: LeetCode
Topic: Linked List

Approach:
We iterate through the linked list and reverse the direction 
of each node by changing its next pointer.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev