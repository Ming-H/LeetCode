#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid]>nums[right]:
                left = mid + 1
            else:
                right = mid if nums[right]!=nums[mid] else right-1
        return nums[left]

