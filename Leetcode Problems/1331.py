"""
Problem : 1331
Title   : Rank Transform of an Array

Started : 13:54:32
Date    : Sunday, 12 July 2026
"""
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        sorted_unique = sorted(set(arr))
        rank_map = {value: index + 1 for index, value in enumerate(sorted_unique)}
        return [rank_map[value] for value in arr]


if __name__ == "__main__":
    sol = Solution()
    _cases = [
        (sol.arrayRankTransform(arr=[40, 10, 20, 30]), [4, 1, 2, 3]),
        (sol.arrayRankTransform(arr=[100, 100, 100]), [1, 1, 1]),
        (sol.arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]), [5, 3, 4, 2, 8, 6, 7, 1, 3]),
    ]
    _passed = 0
    for _i, (_actual, _expected) in enumerate(_cases, start=1):
        if _actual == _expected:
            print(f"[PASS] Example {_i}: {_actual!r}")
            _passed += 1
        else:
            print(f"[FAIL] Example {_i}: expected {_expected!r}, got {_actual!r}")
    print(f"\n{_passed}/{len(_cases)} example(s) passed.")
