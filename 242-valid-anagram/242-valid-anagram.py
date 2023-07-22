class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        '''
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
        '''
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - 97] += 1
        for i in range(len(t)):
            freq[ord(t[i]) - 97] -= 1
            if(freq[ord(t[i]) - 97] < 0):
                return False
        return True