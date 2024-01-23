class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10**9 + 7
        maxi = pow(2, p) - 1
        sec = maxi - 1
        n = pow(2, p-1) - 1
        return (pow(sec, n, mod) * (maxi%mod))%mod
