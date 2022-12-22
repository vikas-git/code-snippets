'''
    =, copy(), deepcopy()
'''

list1 = [1,2,3,4]
list2 = list1

# I made change in list2 but it reflect on list1 also because both variable referring to the same memory location
list2[1] = 10
print(id(list1) == id(list2)) # return True
print(list1, list2) # [1, 10, 3, 4] [1, 10, 3, 4]



# copy / shallow copy
import copy
lst1 = [1,2,3,4]
# here we can use copy.copy(lst1)
lst2 = lst1.copy() # it means we refer to diff memory location

lst2[1] = 100

print(id(lst1) == id(lst2)) # return False
print(lst1, lst2) # [1, 10, 3, 4] [1, 100, 3, 4]

# shallow copy on nested list
'''
whenever we use nested list, If we update some element it'll reflect on both list but if we try to append
any element then it'll reflect on only current list not other one.
it means shallow copy not work on nested element while we update or delete
'''

lst1 = [[1,2,3,4], [4,5,6,7]]
lst2 = lst1.copy()
lst2[1][1] = 50

print(id(lst1) == id(lst2)) # return False
print(lst1, lst2) #[[1, 2, 3, 4], [4, 50, 6, 7]] [[1, 2, 3, 4], [4, 50, 6, 7]]

# same behaviour on delete element also
lst2[1].pop()
print(id(lst1) == id(lst2)) # return False
print(lst1, lst2) #[[1, 2, 3, 4], [4, 50, 6]] [[1, 2, 3, 4], [4, 50, 6]]

print('-'*10)
# deep copy
import copy
lst1 = [1,2,3]
lst2 = copy.deepcopy(lst1)

lst2[1] = 100
print(id(lst1) == id(lst2)) # False
# In a normal list  shallow copy == deep copy
print(lst1, lst2) # [1, 2, 3] [1, 100, 3]

# shallow copy on nested list
lst1 = [[1,2,3], [3,4,5], [5,6,7]]
lst2 = copy.deepcopy(lst1)
lst2[1][1] = 40

print(id(lst1) == id(lst2)) # False
print(lst1, lst2) # [[1, 2, 3], [3, 4, 5], [5, 6, 7]] [[1, 2, 3], [3, 40, 5], [5, 6, 7]]



