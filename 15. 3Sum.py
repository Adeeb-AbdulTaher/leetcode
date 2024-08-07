


#skightly better brute force. shortening the search arrays.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums=[]
        nums.sort()
        ii=0
        for i in nums:
            jj=ii+1
            for j in nums[ii+1:]:
                kk=jj
                for k in nums[jj:]:
                    if i+j+k==0 and ii != jj and ii != kk and jj != kk:
                        sums.append(sorted([i,k,j]))
                    kk+=1
                jj+=1
            ii+=1
        dup_free = []
        for x in sums:
            if x not in dup_free:
                dup_free.append(x)
        return(dup_free)


#brute force takes too long ofc, O(n^3) then also applying 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums=[]
        nums.sort()
        ii=0
        for i in nums:
            ii+=1
            jj=0
            for j in nums:
                jj+=1
                kk=0
                for k in nums:
                    kk+=1
                    if i+j+k==0 and ii != jj and ii != kk and jj != kk:
                        sums.append(sorted([i,k,j]))
        dup_free = []
        for x in sums:
            if x not in dup_free:
                dup_free.append(x)
        return(dup_free)
