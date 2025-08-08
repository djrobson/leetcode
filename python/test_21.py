from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # prime the list with a dummy value to avoid special cases
        dummy = ListNode()
        current = dummy

        # Reuse existing nodes instead of creating new ones
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes (at most one will be non-null)
        current.next = list1 or list2

        # Return the merged list, skipping the dummy node
        return dummy.next


def test_empty():
    s = Solution()
    output = s.mergeTwoLists(None, None)
    assert output == None, "Failed with empty"


def test_one_empty():
    s = Solution()
    output = s.mergeTwoLists(None, ListNode(0))
    expected = ListNode(0)
    while output is not None:
        assert output.val == expected.val, "Failed with one_empty"
        output = output.next
        expected = expected.next


def test_both():
    s = Solution()
    output = s.mergeTwoLists(
        ListNode(1, ListNode(2, ListNode(3))), ListNode(1, ListNode(3, ListNode(4)))
    )
    expected = ListNode(
        1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4)))))
    )
    while output is not None:
        assert output.val == expected.val, "Failed with both"
        output = output.next
        expected = expected.next
