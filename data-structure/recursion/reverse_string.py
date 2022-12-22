def reverse(s):
    #base case
    if len(s) <= 1:
        return s
    #recur case 
    elif len(s) >= 2:
        n=len(s)
        return reverse(s[n//2:])+reverse(s[:n//2])
    return s


# print(reverse(["h","e","l","l","o"]))

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return s
        #recur case 
        elif len(s) >= 2:
            n=len(s)
            return self.reverseString(s[n//2:]) + self.reverseString(s[:n//2])

obj = Solution()
obj.reverseString(["h","e","l","l","o"])
print(s)