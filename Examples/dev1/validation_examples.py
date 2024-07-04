# Testing input
def print_vals():
    # This is a common solution, but has faults, isdigit returns false for a negative integer
    x_str = input("Enter an integer: ")
    if x_str.isdigit() == True:
        x = int(x_str)
        print("The integer entered:", x)
    else:
        print("***Error, value not an integer.")


def validating_ints_better():
    try:
        x = int(input("Enter an integer: "))
        print("The integer entered:", x)
    except ValueError:
        print("***Error, value not an integer.")
        
def loop_until_validated():
    while True:
        try:
            x = int(input("Enter an integer: "))
            print("The integer entered:", x)
            break
        except ValueError:
            print("***Try again, value must be an integer.")

    print("\nThanks for playing.")

#validating_numbers()
#validating_ints_better()
loop_until_validated()