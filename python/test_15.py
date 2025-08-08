from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        output = list()

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                # skip repeats
                continue

            if nums[i] > 0:
                # no negative numbers left
                # so all remaining sequences can't subtract to 0
                break

            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right = right - 1
                elif sum < 0:
                    left = left + 1
                else:  # sum == 0
                    output.append([nums[i], nums[left], nums[right]])

                    # fast forward the ends towards each other
                    cur_left = nums[left]
                    cur_right = nums[right]
                    while nums[left] == cur_left and left < len(nums) - 1:
                        left += 1
                    while nums[right] == cur_right and right > 0:
                        right -= 1

        return output


def test_0s():
    input = [0, 0, 0]
    s = Solution()
    output = s.threeSum(input)
    assert output == [[0, 0, 0]], "Failed with 0's"


def test_some():
    input = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    output = s.threeSum(input)
    assert output == [[-1, -1, 2], [-1, 0, 1]], "Failed with Some"


def test_repeats():
    input = [-1, 0, 1, 0, -1, 0, 1, 0, -1]
    s = Solution()
    output = s.threeSum(input)
    assert output == [[-1, 0, 1], [0, 0, 0]], "Failed with repeats"


def test_no():
    input = [0, 1, 1]
    s = Solution()
    output = s.threeSum(input)
    assert output == [], "Failed with no solution"


def test_empty():
    input = []
    s = Solution()
    output = s.threeSum(input)
    assert output == [], "Failed with empty"


def test_small():
    input = [0, 1]
    s = Solution()
    output = s.threeSum(input)
    assert output == [], "Failed with small input"
