class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # jab tak duplicate element hai left side se window chota karo
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            
            # window me right element add hoga
            charSet.add(s[r])
            window_size = r - l + 1
            res = max(res, window_size)

        return res
