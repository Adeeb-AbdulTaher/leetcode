#my optimized solution, top 45%

class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for i in strs:
                a["".join(sorted(i))].append(i)
        return a.values()


# my dict solution, bottom 15%

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a={}
        for i in strs:
            if str(sorted(i)) not in a:
                a[str(sorted(i))]=[i]
            else:
                a[str(sorted(i))].append(i)
        return a.values()


# my initial solution botton 5%
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s=[]
        n=[]
        final=[]
        finall=[]
        for i in strs:
            s=s+[sorted(i)]
        for i in range(len(s)):
            if s[i] not in n:
                n.append(s[i])
        for i in range(len(n)):
            final.append([])
            for j in range(len(s)):
                if n[i]==s[j]:
                    final[i].append(j)
        for i in range(len(final)):
            finall.append([])
            for j in range(len(final[i])):
                finall[i].append(strs[final[i][j]])
        return finall
