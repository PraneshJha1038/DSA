"""
Problem : 1081
Title   : Smallest Subsequence of Distinct Characters

Started : 13:03:04
Date    : Sunday, 19 July 2026
"""
from typing import AnyStr
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurence = {}
        for i, char in enumerate(s):
            last_occurence[char] = i
        stack = [] 
        visited = set()
        for i in range(len(s)):
            if s[i] in visited:
                continue
            while stack and s[i] < stack[-1] and i < last_occurence.get(stack[-1],-1):
                visited.remove(stack.pop())
            visited.add(s[i])
            stack.append(s[i])
        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    _cases = [
        (sol.smallestSubsequence(s = "bcabc"), "abc"),
        (sol.smallestSubsequence(s = "cbacdcbc"), "acdb"),
    ]
    _passed = 0
    for _i, (_actual, _expected) in enumerate(_cases, start=1):
        if _actual == _expected:
            print(f"[PASS] Example {_i}: {_actual!r}")
            _passed += 1
        else:
            print(f"[FAIL] Example {_i}: expected {_expected!r}, got {_actual!r}")
    print(f"\n{_passed}/{len(_cases)} example(s) passed.")
