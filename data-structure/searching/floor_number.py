
# return the index of greatest no <= target
def floor_number(_list, target):

    first = 0
    last = len(_list)-1

    while first <= last:
        mid = (first+last)//2

        if target < _list[mid]: #search in left half
            last = mid-1
        elif target > _list[mid]: #search in right half
            first = mid+1
        else: #search value present at index mid
            return mid
    return last

print(floor_number([10,13,25,32,40,46,52,63], 8))