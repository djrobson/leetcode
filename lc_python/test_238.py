import pytest
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:

    num_count = len(nums)
    fwd_product = 1
    fwd_nums = []

    for num in nums:
        fwd_nums.append(fwd_product)
        fwd_product *= num

    back_product = 1
    back_nums = []
    for num in reversed(nums):
        back_nums.append(back_product)
        back_product *= num

    prod_except_self = []

    for i in range(num_count):
        pre_prod = 1
        if i > 0 :
            pre_prod = fwd_nums[i]

        post_prod = 1
        if i < num_count -1:
            post_prod = back_nums[num_count - i -1]
        prod_except_self.append(pre_prod * post_prod)

    return prod_except_self

def test_productExceptSelf_positive_numbers():
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6], "Failed with positive numbers"

def test_productExceptSelf_mix_positive_negative():
    assert productExceptSelf([-1, 2, -3, 4]) == [-24, 12, -8, 6], "Failed with a mix of positive and negative numbers"

def test_productExceptSelf_with_zeros():
    assert productExceptSelf([0, 1, 2, 3, 4]) == [24, 0, 0, 0, 0], "Failed with zeros in the array"

def test_productExceptSelf_single_element():
    assert productExceptSelf([42]) == [1], "Failed with a single element"

def test_productExceptSelf_two_elements():
    assert productExceptSelf([0, 0]) == [0, 0], "Failed with two zeros"
    assert productExceptSelf([0, 2]) == [2, 0], "Failed with one zero and one non-zero"
    assert productExceptSelf([3, 4]) == [4, 3], "Failed with two non-zero elements"