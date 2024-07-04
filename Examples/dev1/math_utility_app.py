from dev1.math_utility import divide_by_2

def divide_by_2_app():
    print("This app accepts a number and divides it by 2.")
    x = input("Enter an integer: ")
    x = int(x)
    ans = divide_by_2(x)
    print(f"{x} is divisible by 2, {ans} times")

def enhanced_app():
    print("This app accepts a number and divides it by 2.")
    user_val = 'z'
    while user_val != 'q' or user_val != 'Q':
        user_val = input("Enter an integer (q to quit): ")
        if user_val == 'q' or user_val == 'Q':
            print("Thanks for playing! See you later!")
        else:
            x = int(user_val)
            ans = divide_by_2(x)
            print(f"{x} is divisible by 2, {ans} times")

def enhanced_app2():
    print("This pc app accepts an integer and divides it by 2.")
    user_val = input("Enter an integer (anything else to quit): ")
    while is_int(user_val):
        x = int(user_val)
        ans = divide_by_2(x)
        print(f"{x} is divisible by 2, {ans} times")
        user_val = input("Enter an integer (anything else to quit): ")
        
    print("Thanks for playing! See you later!")

def is_int(var):
    try:
        int(var)
        return True
    except ValueError:
        return False
#divide_by_2_app()
enhanced_app2()
