'''
    Max subarray: https://leetcode.com/problems/maximum-subarray/
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solve using kadane's algo
        # for i in range(1, len(nums)):
        #     if nums[i-1] > 0:
        #         nums[i] += nums[i-1]
        # return max(nums)
    
        # 2nd solution
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

