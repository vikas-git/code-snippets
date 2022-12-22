def helper(n, count):
    if n == 0:
        return count
    rem = n%10
    if rem == 0:
        return helper(int(n//10), count+1)
    return helper(int(n//10), count)

def count(n):
    return helper(n, 0)

print(count(320100))