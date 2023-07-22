class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        dict_s = {}
        for i in range(len(s)):
            dict_s[s[i]] = (dict_s[s[i]] + 1) if s[i] in dict_s else 1
        for i in range(len(t)):
            if(t[i] in dict_s):
                dict_s[t[i]] -= 1
                if(dict_s[t[i]] == 0):
                    del dict_s[t[i]]
            else: 
                return False
            
        return False if dict_s else True