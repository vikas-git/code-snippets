# linear search
'''
    time complexity 
    best case: O(1).
    Worst case: O(n).
'''
def linear_search(_list, search_value):
    for itemk, itemv in enumerate(_list) :
        if itemv == search_value:
            return itemk
    return -1

# print(linear_search([25,40,12,10,46,63], 11))

'''
    time complexity : O(n).
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
print(binary_search_iterative(_list, 40))
print('-'*50)
print(binary_search_recursive(_list, 0, len(_list)-1, 40))
