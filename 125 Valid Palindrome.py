
#2 liner code
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[\W_]+', '', s).lower()
        #s = [i for i in s.lower() if i.isalnum()] has bette time, slightly
        return s == s[::-1]


# my initial solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[\W_]+', '', s).lower()
        i=0
        j=1
        n=len(s)
        while i<(n-j):
            print(s[i],s[n-j])
            if s[i]!=s[n-j]:
                return False
            i+=1
            j+=1
        return True
