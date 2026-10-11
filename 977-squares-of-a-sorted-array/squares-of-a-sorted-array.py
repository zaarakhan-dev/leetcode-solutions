class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n

        left = 0
        right = n-1

        for pos in range(n-1,-1,-1):
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                res[pos] = left_sq
                left+=1
            else:
                res[pos] = right_sq
                right-=1

        return res   