# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
def next_greatest_letter(_list, target):
    first = 0
    last = len(_list)-1

    while first <= last:
        mid = (first+last)//2

        if target < _list[mid]: #search in left half
            last = mid-1
        else:
            first = mid+1

    return _list[first % len(_list)]

print(next_greatest_letter(['a', 'c', 'e', 'f'], 'b'))