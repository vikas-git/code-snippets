'''
    Two adjacent elements compared, if element not in correct position(ASC/DESC) then swap it
    time complexity : O(n2) order of n square

    https://www.youtube.com/watch?v=o4bAoo_gFBU&list=PLuZ_bd9XlByzTIP5j1aWXo7smCIxvzd2D&index=1
'''

a = [2,0,2,1,1,0]
n = len(a)

for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
'''
    Can we optimize this code ?
    As we know the last element sorted so we don't need to run inner loop till last
'''

for i in range(n):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)

'''
    Can we optimize more ?
    suppose we have 10 elements in array/list and after 2 or 3 passes
    we got sorted array, so for that situation we have to maintain a tag.
'''

for i in range(n):
    flag = False
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            flag = True

    if not flag:
        break

print(a)