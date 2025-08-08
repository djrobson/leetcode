from typing import List

import pytest


class Solution:
    digits = {
        "0": "",
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        output = [""]
        # for each digit of input
        for digit in digits:
            new_output = []
            # for every prefix in the output
            for out in output:
                #  append every possible mapping
                for l in self.digits[digit]:
                    new_output.append(f"{out}{l}")

            output = new_output

        if output[0] == "":
            output = []
        return output


def test_empty():
    input = ""
    s = Solution()
    output = s.letterCombinations(input)
    assert output == [], "Failed with empty"


def test_small():
    input = "2"
    s = Solution()
    output = s.letterCombinations(input)
    assert output == ["a", "b", "c"], "Failed with small"


def test_23():
    input = "23"
    s = Solution()
    output = s.letterCombinations(input)
    assert output == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ], "Failed with 23"
