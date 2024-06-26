

#my first simple logic solution. worst 5%. most did under 100ms, this took 5000ms [O(n)]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff=[target-i for i in numbers]
        i=0
        for i in range(len(diff)):
            print(i,diff[i])
            if diff[i] in numbers and i!=numbers.index(diff[i]):
                return [i+1,numbers.index(diff[i])+1] if i<numbers.index(diff[i]) else [numbers.index(diff[i])+1,i+1]
