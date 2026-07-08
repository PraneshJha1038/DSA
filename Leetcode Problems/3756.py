"""
Problem : 3756
Title   : Concatenate Non-Zero Digits and Multiply by Sum II

Started : 09:31:04
Date    : Wednesday, 08 July 2026
"""
from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
        sum_pref = [0] * (n + 1)
        x_pref = [0] * (n + 1)
        nz_count = [0] * (n + 1)
        for i in range(n):
            digit = int(s[i])
            sum_pref[i+1] = sum_pref[i] + digit
            if digit != 0:
                x_pref[i+1] = (x_pref[i] * 10 + digit) % MOD
                nz_count[i+1] = nz_count[i] + 1
            else:
                x_pref[i+1] = x_pref[i]
                nz_count[i+1] = nz_count[i]
                
        result = []
        for l, r in queries:
            current_sum = sum_pref[r+1] - sum_pref[l]
            nz_in_range = nz_count[r+1] - nz_count[l]
            x_val = (x_pref[r+1] - (x_pref[l] * pow10[nz_in_range])) % MOD
            ans = (x_val * current_sum) % MOD
            result.append(ans)
        return result

# sol = Solution()
# sol.sumAndMultiply(s = "10203004", queries = [[0,7],[1,3],[4,6]])

if __name__ == "__main__":
    sol = Solution()
    _cases = [
        (sol.sumAndMultiply(s = "10203004", queries = [[0,7],[1,3],[4,6]]), [12340, 4, 9]),
        (sol.sumAndMultiply(s = "1000", queries = [[0,3],[1,1]]), [1, 0]),
        (sol.sumAndMultiply(s = "9876543210", queries = [[0,9]]), [444444137]),
    ]
    _passed = 0
    for _i, (_actual, _expected) in enumerate(_cases, start=1):
        if _actual == _expected:
            print(f"[PASS] Example {_i}: {_actual!r}")
            _passed += 1
        else:
            print(f"[FAIL] Example {_i}: expected {_expected!r}, got {_actual!r}")
    print(f"\n{_passed}/{len(_cases)} example(s) passed.")
