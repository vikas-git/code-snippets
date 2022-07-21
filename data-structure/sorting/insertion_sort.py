'''
    worst case: O(n2)
    best case:O(n)
    https://www.youtube.com/watch?v=yCxV0kBpA6M&list=PLuZ_bd9XlByzTIP5j1aWXo7smCIxvzd2D&index=2
'''

a = [5, 4, 10, 1, 6, 2]
n = len(a)

for i in range(1, n):
    temp = a[i]
    j = i-1

    while j>=0 and a[j] > temp:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = temp

print(a)
