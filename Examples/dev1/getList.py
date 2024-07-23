def get_list():
    vals  = []
    val = 99
    while val != -1:
        val = int(input("Enter an integer (-1 to quit): "))
        if val != -1:
            vals.append(val)
    return vals

def print_list(nums):
    count = 1
    for n in nums:
        if count % 3 == 0:
            print(n)
        else:
            print(f"{n}, ", end=' ')
        count += 1


vals = get_list()
print(f"vals={vals}")
print_list(vals)