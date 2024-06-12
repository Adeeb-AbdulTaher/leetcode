# my solution with heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=defaultdict(int)
        for i in nums:
            a[i]+=1
        return heapq.nlargest(k,a,key=a.get)

# suggested solution 
return sorted(a, key=a.get, reverse=True)[:k]
