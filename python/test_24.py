from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # check for empty list
        if head is None:
            return None

        # check for single list
        if head.next is None:
            return head

        new_head = head.next  # grab a reference to return at the end

        pointer_from_prev_pair = ListNode(0, head)  # a new ref to point to the start of
        start_of_this_pair = head  # prime the loop by remembering the first of the pair

        while True:
            next_first = start_of_this_pair
            if next_first is None:
                # the pre pair already points at next_first, we're done
                break

            next_second = next_first.next

            if next_second is None:
                # can't swap a single item, we're done
                break

            # do all the swaps and fix up the next's
            next_first.next = next_second.next
            next_second.next = next_first
            pointer_from_prev_pair.next = next_second

            # setup for the next iteration
            pointer_from_prev_pair = next_first
            start_of_this_pair = pointer_from_prev_pair.next

        return new_head


def print_list(list: Optional[ListNode]) -> ():
    print("List: ", end="")
    head = list
    while head is not None:
        print(f"{head.val} ", end="")
        head = head.next


def are_identical(list1: Optional[ListNode], list2: Optional[ListNode]) -> bool:
    list1_head = list1
    list2_head = list2
    while list1_head is not None and list2_head is not None:
        if list1_head.val != list2_head.val:
            return False
        list1_head = list1_head.next
        list2_head = list2_head.next

    return list1_head is None and list2_head is None


def test_0():
    input = None
    s = Solution()
    output = s.swapPairs(input)
    assert output == None, "Failed with 0"


def test_1():
    input = ListNode(1, None)
    s = Solution()
    output = s.swapPairs(input)

    assert are_identical(output, ListNode(1, None)), "Failed with 1"


def test_2():
    input = ListNode(1, ListNode(2))
    s = Solution()

    output = s.swapPairs(input)
    assert are_identical(output, ListNode(2, ListNode(1))), "Failed with 2"


def test_3():
    input = ListNode(1, ListNode(2, ListNode(3)))
    s = Solution()
    output = s.swapPairs(input)
    assert are_identical(output, ListNode(2, ListNode(1, ListNode(3)))), "Failed with 3"


def test_4():
    input = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    s = Solution()
    output = s.swapPairs(input)
    assert are_identical(
        output, ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
    ), "Failed with 4"


def test_multi_odd():
    input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solution()
    output = s.swapPairs(input)
    assert are_identical(
        output, ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5)))))
    ), "Failed with multi odd"
