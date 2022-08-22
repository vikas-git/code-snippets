
def longestPalindrome(s):
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True

    max_length = 1
    start = 0
    for l in range(2,len(s)+1):
        for i in range(len(s)-l+1):
            end = i+l
            if l==2:
                if s[i] == s[end-1]:
                    dp[i][end-1]=True
                    max_length = l
                    start = i
            else:
                if s[i] == s[end-1] and dp[i+1][end-2]:
                    dp[i][end-1]=True
                    max_length = l
                    start = i
    return s[start:start+max_length]

# print(longestPalindrome("ABBABBC"))

def find_min_max(a, n):
    min = a[0]
    max = a[0]
    for i in range(1, n):
        if a[i] < min:
            min = a[i]
        elif a[i] > max:
            max = a[i]
    return min, max

# print(find_min_max([1, 345, 234, 21, 56789], 5))

def sort(a, n):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a


print(sort([1,5,3,2], 4))