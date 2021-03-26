'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valores = {}
        for i in range(len(nums)):
            valores[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in valores:
                if i!=valores[nums[i]]:
                    return [i,valores[nums[i]]]


    nums = [3, 2, 4, 6]
    target = 6

    print(Solution(nums,target))
'''


'''
Success

Details 
Runtime: 52 ms, faster than 25.07% of Python3 online submissions for Two Sum.
Memory Usage: 14.2 MB, less than 90.95% of Python3 online submissions for Two Sum.
'''

# Bruteforce
'''
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] == target - nums[i]:
                return [i,j]

nums = [3,2,4]
target = 6

print(twoSum(nums,target))
'''

#Solution 100%

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = dict()
        pos = 0
        while pos < len(nums):
            if (target - nums[pos]) not in dictionary:
                dictionary[nums[pos]] = pos
                pos += 1
            else:
                return [dictionary[target - nums[pos]], pos]

                
