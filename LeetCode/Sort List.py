class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left, right = self.splitList(head)

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def splitList(self, head: ListNode) -> Tuple[ListNode, ListNode]:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        return head, right

    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        new_head = ListNode()
        tail = new_head

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return new_head.next
