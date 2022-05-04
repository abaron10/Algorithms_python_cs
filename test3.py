
def lengthOfLongestSubstring(s):
        
    charset = set()
    l = 0
    
    for r in range(len(s)):
        while s[r] in charset:
            charset.remove(s[l])
            l += 1
        charset.add(s[r])
        res = max(res, r-1 +1)
    return res

print(lengthOfLongestSubstring("pwwkew"))