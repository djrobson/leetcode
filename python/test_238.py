from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    # First pass: calculate left products and store in result array
    # result[i] will contain the product of all elements to the left of nums[i]
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Second pass: multiply by right products in-place
    # For each position, multiply the left product (already in result[i])
    # by the product of all elements to the right
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product  # left_product * right_product
        right_product *= nums[i]

    return result


def test_productExceptSelf_positive_numbers():
    assert productExceptSelf([1, 2, 3, 4]) == [
        24,
        12,
        8,
        6,
    ], "Failed with positive numbers"


def test_productExceptSelf_mix_positive_negative():
    assert productExceptSelf([-1, 2, -3, 4]) == [
        -24,
        12,
        -8,
        6,
    ], "Failed with a mix of positive and negative numbers"


def test_productExceptSelf_with_zeros():
    assert productExceptSelf([0, 1, 2, 3, 4]) == [
        24,
        0,
        0,
        0,
        0,
    ], "Failed with zeros in the array"


def test_productExceptSelf_single_element():
    assert productExceptSelf([42]) == [1], "Failed with a single element"


def test_productExceptSelf_two_elements():
    assert productExceptSelf([0, 0]) == [0, 0], "Failed with two zeros"
    assert productExceptSelf([0, 2]) == [2, 0], "Failed with one zero and one non-zero"
    assert productExceptSelf([3, 4]) == [4, 3], "Failed with two non-zero elements"
