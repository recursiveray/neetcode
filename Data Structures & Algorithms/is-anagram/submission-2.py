class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a1 = {}
        a2 = {}
        for char in s:
            if char not in a1:
                a1[char] = 1
            else:
                a1[char] += 1
        
        for char in t:
            if char not in a2:
                a2[char] = 1
            else:
                a2[char] += 1
                
        return a1 == a2

