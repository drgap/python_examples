# Testing input
def print_vals(n):
    for i in range(1, n+1):
        print(i, end=' ')

def print_everyother(n):
    for i in range(1, n+1):
        if i%2 == 1:
            print(i, end=' ')

def print_everyother2(n):
    for i in range(1, n+1, 2):
        print(i, end=' ')

def print_reverse(n):
    while n > 0:
        print(n, end=' ')
        n -= 1

def print_reverse2(n):
    for i in range(n, 0, -1):
        print(i, end=' ')

def print_reverse3(n):
    num_1 = n + 1

    for x in range(1, n+1):
        num_1 -= 1
        print(num_1, end=" ")


def count_divisible_by_2(n):
    count = 0
    while n > 0:
        if n%2 == 0:
            count += 1
            n = n/2
        else:
            n=0
    return count

def max_val(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

print("print_vals(5):", end=' ')
print_vals(5)
print("\nprint_everyother(1):", end=' ')
print_everyother(1)
print("\nprint_everyother(2):", end=' ')
print_everyother(2)
print("\nprint_everyother(3):", end=' ')
print_everyother(3)
print("\nprint_everyother(4):", end=' ')
print_everyother(4)
print("\nprint_everyother(5):", end=' ')
print_everyother(5)
print("\nprint_everyother(6):", end=' ')
print_everyother(6)
print("\nprint_everyother(7):", end=' ')
print_everyother(7)
print("\nprint_everyother2(6):", end=' ')
print_everyother2(6)
print("\nprint_everyother2(7):", end=' ')
print_everyother2(7)

print("\nprint_reverse(7):", end=' ')
print_reverse(7)
print("\nprint_reverse2(7):", end=' ')
print_reverse2(7)
print("\nprint_reverse3(7):", end=' ')
print_reverse3(7)

count = count_divisible_by_2(1)
print("\ncount_divisible_by_2(1)=", count, end=' ')
count = count_divisible_by_2(2)
print("\ncount_divisible_by_2(2)=", count, end=' ')
count = count_divisible_by_2(3)
print("\ncount_divisible_by_2(3)=", count, end=' ')
count = count_divisible_by_2(4)
print("\ncount_divisible_by_2(4)=", count, end=' ')
count = count_divisible_by_2(5)
print("\ncount_divisible_by_2(5)=", count, end=' ')
count = count_divisible_by_2(32)
print("\ncount_divisible_by_2(32)=", count, end=' ')
count = count_divisible_by_2(44)
print("\ncount_divisible_by_2(44)=", count, end=' ')

max_val2 = max_val(5,7,8)
print("\nmax_val(5,7,8)=", max_val2, end=' ')
max_val2 = max_val(8,7,5)
print("\nmax_val(8,7,5)=", max_val2, end=' ')
max_val2 = max_val(7,8,5)
print("\nmax_val(7,8,5)=", max_val2, end=' ')
max_val2 = max_val(8,7,8)
print("\nmax_val(8,7,8)=", max_val2, end=' ')