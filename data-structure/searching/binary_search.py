'''
    time complexity : O(logn).
'''
def binary_search_iterative(_list, search_value):
    first = 0
    last = len(_list)-1

    while first <= last:
        mid = (first+last)//2

        if search_value < _list[mid]: #search in left half
            last = mid-1
        elif search_value > _list[mid]: #search in right half
            first = mid+1
        else: #search value present at index mid
            return mid
    return -1

# print(binary_search_iterative([10,13,25,32,40,46,52,63], 31))

def binary_search_recursive(_list, first, last, search_value):
    if first <= last:
        mid = (first+last)//2

        if search_value < _list[mid]: #search in left half
            last = mid-1
            return binary_search_recursive(_list, first, last, search_value)
        elif search_value > _list[mid]: #search in right half
            first = mid+1
            return binary_search_recursive(_list, first, last, search_value)
        else: #search value present at index mid
            return mid
    else:
        return -1

_list = [10,13,25,32,40,46,52,63] 
print(binary_search_iterative(_list, 70))
print('-'*50)
# print(binary_search_recursive(_list, 0, len(_list)-1, 40))
