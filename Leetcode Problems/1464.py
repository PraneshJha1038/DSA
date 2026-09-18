"""
Problem : 1464
Title   : Maximum Product of Two Elements in an Array

Started : 01:12:12
Date    : Tuesday, 28 July 2026
"""
from typing import *
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        


if __name__ == "__main__":
    sol = Solution()
    _cases = [
        (sol.maxProduct(nums = [3,4,5,2]), 12),
        (sol.maxProduct(nums = [1,5,4,5]), 16),
        (sol.maxProduct(nums = [3,7]), 12),
    ]
    _passed = 0
    for _i, (_actual, _expected) in enumerate(_cases, start=1):
        if _actual == _expected:
            print(f"[PASS] Example {_i}: {_actual!r}")
            _passed += 1
        else:
            print(f"[FAIL] Example {_i}: expected {_expected!r}, got {_actual!r}")
    print(f"\n{_passed}/{len(_cases)} example(s) passed.")
