
# smart solution
class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


# my optimized code, top 1%

class Solution(object):
    def containsDuplicate(self, nums):
        numMap={}
        for i in nums:
            if i in numMap:
                return True
            else:
                numMap[i] = i
