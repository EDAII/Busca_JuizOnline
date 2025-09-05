class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0

        # Coloca cada x (1..n) na posição x-1
        while i < n:
            x = nums[i]
            if 1 <= x <= n and nums[x - 1] != x:
                nums[i], nums[x - 1] = nums[x - 1], nums[i]
            else:
                i += 1

        # A primeira posição fora do lugar define a resposta
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
