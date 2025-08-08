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

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r = r - 1
                elif sum < 0:
                    l = l + 1
                else:  # sum == 0
                    output.append([nums[i], nums[l], nums[r]])

                    # fast forward the ends towards each other
                    cur_l = nums[l]
                    cur_r = nums[r]
                    while nums[l] == cur_l and l < len(nums) - 1:
                        l += 1
                    while nums[r] == cur_r and r > 0:
                        r -= 1

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