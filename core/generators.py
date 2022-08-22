# def even_numbers(num):
#     for i in range(num):
#         if i%2 == 0:
#             yield i


# for i in even_numbers(10):
#     print(i)


# def multiple_yield():
#     str1 = 'first string'
#     yield str1

#     str2 = 'second string'
#     yield str2

#     str2 = 'third string'
#     yield str2

# for i in multiple_yield():
#     print(i)

# print('-'*100)
# # generator expression
# a = (x**3 for x in [1,2,3])

# for i in a:
#     print(i)

print('-'*100)

class Fib:
    def __init__(self):
        self.a, self.b = 0, 1
    def __next__(self):
        return_value = self.a
        self.a, self.b = self.b, self.a+self.b
        return return_value
    def __iter__(self):
        return self

f = Fib()
for i in range(5):
    print(next(f))