# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        current = merged

        while list1 is not None and list2 is not None: 
            if list1.val < list2.val: 
                current.next = list1
                list1 = list1.next
                current = current.next
            elif list2.val < list1.val: 
                current.next = list2
                list2 = list2.next
                current = current.next
            else: 
                current.next = list1
                list1 = list1.next
                current = current.next
        
        if list1 is None:
            current.next = list2
            return merged.next

        if list2 is None: 
            current.next = list1
            return merged.next 
        
def create_linked_list(elements):
    if not elements:  # If the list is empty, return None
        return None
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
    
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

print_linked_list(merged_list)