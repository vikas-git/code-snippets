'''
    merge sort is a recursive algorithm
    it goes on splitting the array into sub-arry till we ge sub-arrays of size 1.
    then it compares elements off 1-element sub-arrays to merge then into a 2-elements sorted array.
    then it merges two such 2-element sorted sub-arrays to build a 4-element sorted sub-array.
    this process continues up the ladder till we get a complete sorted array.

    this is also c/d as DAC(Divide And Conquer) method.
'''

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2

        l_arr = arr[:mid]
        r_arr = arr[mid:]
        merge_sort(l_arr)
        merge_sort(r_arr)

        # conquer process
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1


# Driver Code
if __name__ == '__main__':
	arr = [6, 3, 9, 5, 2, 8]
	print("Given array is", end="\n")
	print(arr)
	merge_sort(arr)
	print("Sorted array is: ", end="\n")
	print(arr)

# This code is contributed by Mayank Khanna
