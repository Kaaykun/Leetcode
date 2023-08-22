class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        current = head
        if current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(head):
    if not head:
        return None

    linked_list = ListNode(head[0])
    current = linked_list

    for i in range(1, len(head)):
        new_node = ListNode(head[i])
        current.next = new_node
        current = current.next

    return linked_list


def main():
    solution = Solution()
    head = [1, 1, 2]
    linked_list = createLinkedList(head)  # Convert list to linked list
    result = solution.deleteDuplicates(linked_list)
    if result:
        current = result
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    main()