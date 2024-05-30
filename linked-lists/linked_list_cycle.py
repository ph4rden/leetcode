# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next

        while fast and fast.next:  # Check to ensure 'fast' and 'fast.next' are not None
            slow = slow.next       # Move slow by 1
            fast = fast.next.next  # Move fast by 2

            if fast == slow:       # Check after both pointers have moved
                return True

        return False

def create_linked_list(values, pos=-1):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_node = None
    for index in range(1, len(values)):
        current.next = ListNode(values[index])
        current = current.next
        if index == pos:
            cycle_node = current
    if pos != -1:  # Create a cycle
        current.next = cycle_node
    return head

def print_linked_list(head, limit=100):
    """ Print the linked list up to 'limit' nodes to avoid infinite loop in case of a cycle. """
    current = head
    count = 0
    while current and count < limit:
        print(current.val, end=" -> ")
        current = current.next
        count += 1
    print("None" if count < limit else "... (list continues due to cycle)")

# Create a linked list without a cycle
list_no_cycle = create_linked_list([1, 2, 3, 4, 5])

# Print the list
print("Linked List without cycle:")
print_linked_list(list_no_cycle)

# Create a Solution object and test for a cycle
solution = Solution()
print("Does the list have a cycle?", solution.hasCycle(list_no_cycle))  # Expected: False

# Create a linked list with a cycle (cycle starts at index 1)
list_with_cycle = create_linked_list([1, 2, 3, 4, 5], pos=1)

# Print the list (with cycle handling)
print("Linked List with cycle:")
print_linked_list(list_with_cycle)

# Test for a cycle
print("Does the list have a cycle?", solution.hasCycle(list_with_cycle))  # Expected: True