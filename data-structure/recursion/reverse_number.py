def reverse_number(n):
    if n==0:
        return 1

    return reverse_number(n//10)

print(reverse_number(54321))