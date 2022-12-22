def fun(n):
    if n == 0:
        return

    print(n) # print 5 to 1
    fun(n-1)
    print(n) # print 1 to 5
fun(5)
