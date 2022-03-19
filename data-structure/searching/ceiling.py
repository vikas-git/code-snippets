
# return the index of smallest no >= target
def ceiling_number(_list, target):
    # but what if the target is greater than the greatest number in the list
    if target > _list[len(_list)-1]:
        return -1

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
    return first

print(ceiling_number([10,13,25,32,40,46,52,63], 15))