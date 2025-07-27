import pytest
from typing import List

class Solution:
    output: List[str] = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.output = []
        self.generateNext(0,0,n,"")
            
        return self.output
    
    def generateNext(self, num_open: int, num_closed: int, n:int, me: str) -> List[str]:
        if num_closed == n:
            # we're done, add this one to the list
            self.output.append(me)
        if num_open < n:
            # we can start another one
            self.generateNext(num_open+1, num_closed, n, me+"(")
        if num_open > num_closed:
            # we can close another one
            self.generateNext(num_open, num_closed+1, n, me+")")

def test_one():
    s = Solution()
    output = s.generateParenthesis(1)
    assert output == ["()"], "Failed with one"

def test_three():
    s = Solution()
    output = s.generateParenthesis(3)
    assert output == ["((()))","(()())","(())()","()(())","()()()"], "Failed with three"