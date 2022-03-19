def reverse(s):
    #base case
    if len(s) <= 1:
        return s
    #recur case 
    elif len(s) >= 2:
        n=len(s)
        return reverse(s[n//2:])+reverse(s[:n//2])


print reverse(["h","e","l","l","o"])