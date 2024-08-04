# Problem 21 - Merge Two Sorted Lists

# Merged Two Already Sorted Linked Lists into One Sorted Linked List

# Example: List1 = 1 -> 3 -> 5 and list2 = 2 -> 4 -> 6
# Merged List = 1 -> 2 -> 3 -> 4 -> 5 -> 6


# Singly ListNode - Goes In 1 Direction.
class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next

# Test Inputs
list1 = ListNode(1 ,ListNode(3, ListNode(5)))
list2 = ListNode(2 ,ListNode(4, ListNode(6)))


# Prints Linked Lists
def print_linked_list(head):

    #Entry Point
    current = head

    # Loops Until None
    while current is not None:

        # Inserts -> between each link
        print(current.val, end=" -> ")

        # Moves to Next Node
        current = current.next
    print("None")



class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        
        # Entry Point
        dummy = ListNode()
        
        # Traversal Variable
        current = dummy

        # Loops While Both Lists aren't Empty.
        while list1 and list2:
            
            # Checks whose smaller.
            if list1.val < list2.val:
                
                # Current Link Value Becomes Link on New List.
                current.next = list1
                
                # Current List Moves Over a Link
                list1 = list1.next
            
            else:
                
                # Current Link Value Becomes Link on New List.
                current.next = list2
                
                # Current List Moves Over a Link
                list2 = list2.next

        # Move current to the newly added node
            current = current.next



        # Connect the remaining nodes, if any
        if list1:
            current.next = list1
            
        elif list2:
            current.next = list2

        # Return Sorted & Merged Linked List
        return dummy.next
                


print(Solution().mergeTwoLists(list1, list2))


