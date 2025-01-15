class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum, max_sum = 0, float('-inf')
        l = nums[0]

        for r in nums:
            curr_sum += r
            max_sum = max(curr_sum, max_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sum