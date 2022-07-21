'''
    Selection sort:
    Ref: https://www.youtube.com/watch?v=9oWd4VJOwr0&list=PLuZ_bd9XlByzTIP5j1aWXo7smCIxvzd2D&index=3
'''


# time complexity : O(n2) order of n square
def selection_sort(a):
    n = len(a)
    for i in range(n):
        least = i
        for k in range(i+1, n):
            if a[k] < a[least]:
                least = k

        if least != i:
            a[least], a[i] = a[i], a[least]



_list = [534, 246, 933, 127, 277, 321, 454, 565, 220]
selection_sort(_list)
print(_list)