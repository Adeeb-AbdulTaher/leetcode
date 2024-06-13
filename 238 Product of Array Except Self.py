# better memory but beats 40% time

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)

#my working solution, better than 66%
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1]
        post=[1]*n
        final=[]

        for i in range(n):
            pre.append(nums[i] if i==0 else pre[i]*nums[i])
        for i in range(n-1,0,-1):
            post[i-1]=nums[i] if i==n-1 else post[i]*nums[i]

        for i in range(n):
            final.append(pre[i]*post[i])
        return final

        
