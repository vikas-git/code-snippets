'''
    242. Valid anagram: https://leetcode.com/problems/valid-anagram/
'''

from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 1st way
        # count the char like how many time certain char exist in string and then compare
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
        # 2nd way
        return Counter(s) == Counter(t)
        Counter
        # 3rd way
        return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"

obj = Solution()
print(obj.isAnagram(s,t))