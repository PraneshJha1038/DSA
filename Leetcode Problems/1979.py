"""
Problem : 1979
Title   : Find Greatest Common Divisor of Array

Started : 12:29:41
Date    : Saturday, 18 July 2026
"""
from typing import List
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = float('inf')
        largest = -1 
        for num in nums:
            smallest = min(smallest,num)
            largest = max(largest,num)
        while smallest > 0 or largest > 0:
            if smallest > largest:
                smallest = smallest % largest
            else:
                largest = largest % smallest
            if smallest == 0:
                return largest #type:ignore
            elif largest == 0:
                return smallest #type:ignore
        return 1


if __name__ == "__main__":
    sol = Solution()
    _cases = [
        (sol.findGCD(nums = [2,5,6,9,10]), 2),
        (sol.findGCD(nums = [7,5,6,8,3]), 1),
        (sol.findGCD(nums = [3,3]), 3),
    ]
    _passed = 0
    for _i, (_actual, _expected) in enumerate(_cases, start=1):
        if _actual == _expected:
            print(f"[PASS] Example {_i}: {_actual!r}")
            _passed += 1
        else:
            print(f"[FAIL] Example {_i}: expected {_expected!r}, got {_actual!r}")
    print(f"\n{_passed}/{len(_cases)} example(s) passed.")
