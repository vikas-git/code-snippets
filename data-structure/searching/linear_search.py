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

print(linear_search([25,40,12,10,46,63], 11))