#abusing python lol

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)

#my initial code
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss=list(s)
        tt=list(t)
        if len(ss)!=len(tt):
            return False
        for i in ss:
            if i not in tt:
                return False
            else:
                tt.remove(i)
        return True
