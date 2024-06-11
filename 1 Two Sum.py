# dict solution 40 ms

class Solution:
    def twoSum(self, nums, target):
        numMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []


# my optimised solution 2000 ms
class Solution():
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                  
# my initial solution 3000+ms
class Solution():
    def twoSum(self, nums, target):
        i=0
        while(i<len(nums)):
            j=i+1
            while(j<len(nums)):
                if(nums[i]+nums[j]==target):
                        return [i,j]
                j=j+1
            i=i+1

  
