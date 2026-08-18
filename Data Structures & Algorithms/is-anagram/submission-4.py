class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s: dict[str, int] = {}
        dict_t: dict[str, int] = {}

        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1

        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        return dict_s == dict_t