'''
    1. two sum: https://leetcode.com/problems/two-sum/
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+ nums[j] == target:
                    return [i, j]
        return []
        '''
        '''
        for i in nums:
            first_num = nums.index(i)
            nums[first_num]  = "a"
            if target - i in nums:
                print(nums)
                return [first_num, nums.index(target-i)]
        return []
        '''

        # faster than prev two solutions
        prevMap = {} # value: index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []

obj = Solution()
print(obj.twoSum([2,7,11,15], 15))