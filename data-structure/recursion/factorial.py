
def fact_recursion(n):
    if n == 1:
        return 1
    return n*fact_recursion(n-1)


def fact(n):
    f = 1
    for i in range(n, 0, -1):
        f = f*i
    print(f)

print(fact_recursion(5))