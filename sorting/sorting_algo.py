def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

count = 0
# time complexity : O(n2) order of n square
def bubble_sort(A):
    global count
    for i in range(len(A)):
        count += 1
        for k in range(len(A)-1, i, -1):
            count += 1
            if(A[k] < A[k-1]):
                swap(A, k, k-1)


# time complexity : O(n2) order of n square
def selection_sort(A):
    global count
    for i in range(len(A)):
        count += 1
        least = i
        for k in range(i+1, len(A)):
            count += 1
            if A[k] < A[least]:
                least = k
        swap(A, least, i)



_list = [534, 246, 933, 127, 277, 321, 454, 565, 220]
# bubble_sort(_list)
selection_sort(_list)
print(_list)
print(count)