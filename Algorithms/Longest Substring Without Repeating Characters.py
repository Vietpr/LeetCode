class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        max_length = 0
        index_map = {} # dictionary store the last index of each character
        for i in range(len(s)):
            if s[i] in index_map and index_map[s[i]] >= start:
                start = index_map[s[i]] + 1
            index_map[s[i]] = i
            current_length = i - start + 1
            max_length = max(max_length, current_length)
        return max_length
result = Solution()
s = "abcabcbb"
# print(result.lengthOfLongestSubstring(s))  
s = "bbbbb"
# print(result.lengthOfLongestSubstring(s))
s = "pwwkew"
# print(result.lengthOfLongestSubstring(s))