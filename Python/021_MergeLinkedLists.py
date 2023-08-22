class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        current = head
        # While list1 and list2 are not None
        while list1 and list2:
            # If value in node of list1 is bigger than value in list2
            if list1.val < list2.val:
                # Create a new ListNode with value from list1
                current.next = list1
                # Move list pointer to next node in list1
                list1 = list1.next
            # If value in node of list2 is bigger or equal to value in list1
            else:
                # Create a new ListNode with value from list2
                current.next = list2
                # Move list pointer to next node in list2
                list2 = list2.next
            # Move current pointer to next node in new list
            current = current.next
        # If one list is None, append the remaining nodes from the list that is not None
        current.next = list1 or list2
        # Return pointer to first node of the new list
        return head.next


class ListNode(object):
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next


def main():
    # Initialize the first linked list with values 2, 4, 3
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)

    node1.next = node2
    node2.next = node3

    l1 = node1

    # Initialize the second linked list with values 5, 6, 4
    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)

    node4.next = node5
    node5.next = node6

    l2 = node4

    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)

    output = []
    current = result
    while current:
        output.append(current.val)
        current = current.next

    print(output)

if __name__ == "__main__":
    main()     