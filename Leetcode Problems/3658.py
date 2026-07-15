"""
Problem : 3658
Title   : GCD of Odd and Even Sums

Started : 15:22:17
Date    : Wednesday, 15 July 2026
"""

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = n*(2 + (n-1)*2)/2
        even = n * (4 + (n-1)*2)/2
        while odd > 0 or even > 0:
            if odd > even:
                odd = odd % even
            else:
                even = even % odd
            if odd == 0:
                return int(even) #type:ignore
            elif even == 0: return int(odd) #type:ignore
        return 1


if __name__ == "__main__":
    sol = Solution()
    _cases = [
        (sol.gcdOfOddEvenSums(n = 4), 4),
        (sol.gcdOfOddEvenSums(n = 5), 5),
    ]
    _passed = 0
    for _i, (_actual, _expected) in enumerate(_cases, start=1):
        if _actual == _expected:
            print(f"[PASS] Example {_i}: {_actual!r}")
            _passed += 1
        else:
            print(f"[FAIL] Example {_i}: expected {_expected!r}, got {_actual!r}")
    print(f"\n{_passed}/{len(_cases)} example(s) passed.")
