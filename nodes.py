from typing import List



# List Nodes
class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next

# Prints Designated Node
def printNode(node):

    # Initializes Empty List
    values = []

    # Loops Until Links Are Gone
    while node:
        
        # Adds Value of Link to Values List
        values.append(str(node.val))

        node = node.next

    print(' -> '.join(values))
   

node1 = ListNode(1, ListNode(3, ListNode(5)))
node2 = ListNode(2, ListNode(4, ListNode(6)))


class Solution:
    def mergeNodes(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        # Entry Point - Anchor
        dummy = ListNode()
        # 'dummy' is a placeholder node that helps in simplifying the merge process. It doesn’t hold any useful data but allows us to easily manage the head of the merged list.

        # Traversable Variable - Link Builder
        current = dummy
        # 'current' is used to build the new merged list. It starts at 'dummy' and will be moved forward as we add nodes to the merged list.

        while list1 and list2:
            # Continue merging as long as there are nodes in both linked lists

            # Compares List Values
            if list1.val < list2.val:
                # Link 'current.next' to 'list1'
                current.next = list1
                list1 = list1.next
            else:
                # Link 'current.next' to 'list2'
                current.next = list2
                list2 = list2.next

            # Move 'current' forward to point to the newly added node
            current = current.next

        # If there are remaining nodes in 'list1', append them
        if list1:
            current.next = list1

        # If there are remaining nodes in 'list2', append them
        if list2:
            current.next = list2

        return dummy.next

print("\nSorted Linked List 1")
printNode(node1)

print("\nSorted Linked List 2")
printNode(node2)

merged_list = Solution().mergeNodes(node1, node2)

    
print("\nSorted Merged List")
printNode(merged_list)


