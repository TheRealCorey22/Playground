# Problem 21 - Merge Two Sorted Lists

# Merged Two Already Sorted Linked Lists into One Sorted Linked List

# Example: List1 = 1 -> 3 -> 5 and list2 = 2 -> 4 -> 6
# Merged List = 1 -> 2 -> 3 -> 4 -> 5 -> 6


class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next


def print_linked_list(head):

    current = head

    
    while current is not None:

        print(current.val, end=" -> ")

        current = current.next


    print("None")


list1 = ListNode(1 ,ListNode(3, ListNode(5)))

list2 = ListNode(2 ,ListNode(4, ListNode(6)))


class Solution:
    
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        
        
        dummy = ListNode()
        
        current = dummy

        
        while list1 and list2:
        
            if list1.val < list2.val:
                
                current.next = list1
                
                list1 = list1.next
            
            else:
            
                current.next = list2
                
                list2 = list2.next

        
            current = current.next


        # Connect remaining Nodes
        if list1:
            current.next = list1
            
        elif list2:
            current.next = list2

        
        return dummy.next
                

print(Solution().mergeTwoLists(list1, list2))


