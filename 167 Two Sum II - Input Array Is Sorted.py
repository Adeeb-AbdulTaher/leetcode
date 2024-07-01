# as an exercise, tried the binary search solution too

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        investigated = []
        for i in range(len(numbers)):
            if not numbers[i] in investigated:
                investigated.append(numbers[i])
                l, r = i + 1, len(numbers) - 1
                tmp = target - numbers[i]
                while l <= r:
                    mid = l + (r-l) // 2
                    if numbers[mid] == tmp:
                        return([i + 1, mid + 1])
                    elif numbers[mid] < tmp:
                        l = mid + 1
                    else:
                        r = mid - 1


# used dic for this like two sum problem, BUT used enumerate here and it was way better
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diffs={}
        for i,num in enumerate(numbers):
            if target-num in diffs:
                return [diffs[target-num]+1,i+1]
            diffs[num]=i


#my first simple logic solution. worst 5%. most did under 100ms, this took 5000ms [O(n^2)]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff=[target-i for i in numbers]
        i=0
        for i in range(len(diff)):
            print(i,diff[i])
            if diff[i] in numbers and i!=numbers.index(diff[i]):
                return [i+1,numbers.index(diff[i])+1] if i<numbers.index(diff[i]) else [numbers.index(diff[i])+1,i+1]
