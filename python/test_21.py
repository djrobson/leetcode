from typing import Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # prime the list with a dummy value to avoid special cases
        new_list_head = ListNode()
        new_list_cur = new_list_head

        cur1 = list1
        cur2 = list2

        while True:
            match (cur1, cur2):
                case (None, None):
                    break
                case (None, y):
                    new_list_cur.next = ListNode(y.val)
                    cur2 = cur2.next
                    new_list_cur = new_list_cur.next
                case (x, None):
                    new_list_cur.next = ListNode(x.val)
                    cur1 = cur1.next
                    new_list_cur = new_list_cur.next
                case (x, y) if x.val < y.val:
                    new_list_cur.next = ListNode(x.val)
                    cur1 = cur1.next
                    new_list_cur = new_list_cur.next
                case (x, y) if x.val >= y.val:
                    new_list_cur.next = ListNode(y.val)
                    cur2 = cur2.next
                    new_list_cur = new_list_cur.next

        # skip the initial dummy value
        return new_list_head.next

def test_empty():
    input = ""
    s = Solution()
    output = s.mergeTwoLists(None,None)
    assert output == None, "Failed with empty"

def test_one_empty():
    input = ""
    s = Solution()
    output = s.mergeTwoLists(None,ListNode(0))
    expected = ListNode(0)
    while(output is not None):
        assert output.val == expected.val, "Failed with one_empty"
        output = output.next
        expected = expected.next

def test_both():
    input = ""
    s = Solution()
    output = s.mergeTwoLists(ListNode(1,ListNode(2,ListNode(3))),ListNode(1,ListNode(3,ListNode(4))))
    expected = ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4))))))
    while(output is not None):
        assert output.val == expected.val, "Failed with both"
        output = output.next
        expected = expected.next
