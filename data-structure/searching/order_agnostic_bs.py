'''
    time complexity : O(logn).
'''
def order_agnostic_binary_search(_list, search_value):
    first = 0
    last = len(_list)-1

    is_asc = _list[first] < _list[last]

    while first <= last:
        mid = (first+last)//2

        if _list[mid] == search_value:
            return mid
        
        if is_asc:
            if search_value < _list[mid]: #search in left half
                last = mid-1
            else:
                first = mid+1
        else:
            if search_value > _list[mid]: #search in left half
                last = mid-1
            else:
                first = mid+1
    return -1



print(order_agnostic_binary_search([10,13,25,32,40,46,52,63], 32))
print(order_agnostic_binary_search([63, 52, 46, 40, 32, 25, 13, 10], 32 ))