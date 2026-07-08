"""
Problem : 3754
Title   : Concatenate Non-Zero Digits and Multiply by Sum I

Started : 14:14:49
Date    : Tuesday, 07 July 2026
"""

from typing import *

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum = 0
        x = "0"
        for char in str(n):
            if char != "0":
                x += char
                sum += int(char)
        return sum * int(x)


if __name__ == "__main__":
# Example 1
    sol = Solution()
    print(sol.sumAndMultiply(n = 10203004))
# Expected:
# 12340

# Example 2
# sol = Solution()
# print(sol.sumAndMultiply(n = 1000))
# Expected:
# 1


import pytest

def test_example_1():
    s = Solution()
    assert s.sumAndMultiply(n = 10203004) == 12340

def test_example_2():
    s = Solution()
    assert s.sumAndMultiply(n = 1000) == 1

