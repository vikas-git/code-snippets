# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [-1, -1]
        if target not in nums:
            return ans

        ans[0] = self.search(nums, target, True)
        if ans[0] != -1:
            ans[1] = self.search(nums, target, False)
        return ans



    def search(self, nums, target, find_start_index):
        first = 0
        last = len(nums)-1
        ans = -1
        while first <= last:
            mid = (first+last)//2

            if target < nums[mid]:
                last = mid-1
            elif target > nums[mid]:
                first = mid+1
            else: 
                ans = mid
                if find_start_index:
                    last = mid - 1
                else:
                    first = mid + 1
        return ans