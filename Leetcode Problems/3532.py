"""
Problem : 3532
Title   : Path Existence Queries in a Graph I

Started : 20:52:38
Date    : Thursday, 09 July 2026
"""
from typing import List
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        qz = len(queries) 
        prev = -1
        cid = 0
        comp = [-1]*n
        for i, curr in enumerate(nums):
            cid += (prev+maxDiff<curr)
            comp[i] = cid
            prev = curr

        return [comp[x]==comp[y] for x,y in queries]


if __name__ == "__main__":
    sol = Solution()
    _cases = [
        (sol.pathExistenceQueries(n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]), [True,False]),
        (sol.pathExistenceQueries(n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]), [False,False,True,True]),
    ]
    _passed = 0
    for _i, (_actual, _expected) in enumerate(_cases, start=1):
        if _actual == _expected:
            print(f"[PASS] Example {_i}: {_actual!r}")
            _passed += 1
        else:
            print(f"[FAIL] Example {_i}: expected {_expected!r}, got {_actual!r}")
    print(f"\n{_passed}/{len(_cases)} example(s) passed.")
