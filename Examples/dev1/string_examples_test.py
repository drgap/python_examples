from dev1.string_examples import *

def test_count_vowels():
    print("\ntest_count_vowels(my_str)")
    my_str = "xyz"
    expected = 0
    actual = count_vowels(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "abc"
    expected = 1
    actual = count_vowels(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "abuba"
    expected = 3
    actual = count_vowels(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "UbubAE"
    expected = 4
    actual = count_vowels(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")


def test_count_vowels2():
    print("\ntest_count_vowels2(my_str)")
    my_str = "xyz"
    expected = 0
    actual = count_vowels2(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "abc"
    expected = 1
    actual = count_vowels2(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "abuba"
    expected = 3
    actual = count_vowels2(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")

def test_count_vowels3():
    print("\ntest_count_vowels3(my_str)")
    my_str = "xyz"
    expected = 0
    actual = count_vowels3(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "abc"
    expected = 1
    actual = count_vowels3(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "abuba"
    expected = 3
    actual = count_vowels3(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")

def test_get_vowel_string():
    print("\ntest_get_vowel_string()")
    my_str = "xyz"
    expected = ""
    actual = get_vowel_string(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "abc"
    expected = "a"
    actual = get_vowel_string(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "abuba"
    expected = "aua"
    actual = get_vowel_string(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")

def test_rearrange_vowels():
    print("\ntest_rearrange_vowels()")
    my_str = "hello"
    expected = "eohll"
    actual = rearrange_vowels(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "12B34"
    expected = "12B34"
    actual = rearrange_vowels(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "aaeoccc"
    expected = "aaeoccc"
    actual = rearrange_vowels(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "cccaaeo"
    expected = "aaeoccc"
    actual = rearrange_vowels(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")

def test_unique_chars():
    print("\ntest_unique_chars()")
    my_str = "Mississippi"
    expected = "Misp"
    actual = unique_chars(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "hello"
    expected = "helo"
    actual = unique_chars(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")
    my_str = "abc"
    expected = "abc"
    actual = unique_chars(my_str)
    print(f"my_str: {my_str}, Expected: {expected}, Actual: {actual}")

def test_remove_char():
    print("\ntest_remove_char()")
    my_str = "Hello"
    char_to_remove = "l"
    expected = "Helo"
    actual = remove_char(my_str, char_to_remove)
    print(f"my_str: {my_str}, char: {char_to_remove}, Expected: {expected}, Actual: {actual}")
    my_str = "dgibson@valdosta.edu"
    char_to_remove = "@"
    expected = "dgibsonvaldosta.edu"
    actual = remove_char(my_str, char_to_remove)
    print(f"my_str: {my_str}, char: {char_to_remove}, Expected: {expected}, Actual: {actual}")
    my_str = "abc"
    char_to_remove = "x"
    expected = "abc"
    actual = remove_char(my_str, char_to_remove)
    print(f"my_str: {my_str}, char: {char_to_remove}, Expected: {expected}, Actual: {actual}")

def test_remove_char2():
    print("\ntest_remove_char2()")
    my_str = "DAave"
    char_to_remove = "a"
    expected = "Dave"
    actual = remove_char2(my_str, char_to_remove)
    print(f"my_str: {my_str}, char: {char_to_remove}, Expected: {expected}, Actual: {actual}")
    my_str = "make"
    char_to_remove = "E"
    expected = "mak"
    actual = remove_char2(my_str, char_to_remove)
    print(f"my_str: {my_str}, char: {char_to_remove}, Expected: {expected}, Actual: {actual}")

def test_remove_string():
    print("\ntest_remove_string()")
    my_str = "Paul Woods Gibson"
    char_to_remove = "woods "
    expected = "Paul Gibson"
    actual = remove_string(my_str, char_to_remove)
    print(f"my_str: '{my_str}', str: '{char_to_remove}', Expected: {expected}, Actual: {actual}")

    my_str = "ABCXYZDEFGH"
    char_to_remove = "xyz"
    expected = "ABCDEFGH"
    actual = remove_string(my_str, char_to_remove)
    print(f"my_str: '{my_str}', str: '{char_to_remove}', Expected: {expected}, Actual: {actual}")


'''
test_count_vowels()
test_count_vowels2()
test_count_vowels3()
test_get_vowel_string()
test_rearrange_vowels()
'''
test_unique_chars()
test_remove_char()
test_remove_char2()
test_remove_string()