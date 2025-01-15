class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, longest = 0, 0, 0
        res = set()

        if len(s) == 1:
            return 1
        
        for r in range(len(s)):
            if s[r] in res:
                while s[r] in res:
                    res.remove(s[l])
                    l += 1
            res.add(s[r])
            
            longest = max(longest, len(res))
        
        return longest
        