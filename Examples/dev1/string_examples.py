'''
Created on Jul 11, 2024

@author: dgibson
'''
'''
Strings are a sequence type, having characters ordered by index from left to right. 
An index is an integer matching a specific position in a string's sequence of characters. 
An individual character is read using an index surrounded by brackets. Ex: my_str[5] reads 
the character at index 5 of the string my_str. Indices start at 0, so index 5 is a 
reference to the 6th character in the string.
'''
# Description: Count number of vowels in a string
# Input: my_str (string) - a string of characters
# Output: count (int) - the number of vowels in the string
# Notes: Uses a for loop to iterate over the characters.
def count_vowels(my_str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in my_str:
        if char in vowels:
            count += 1
    return count


# Description: Count number of vowels in a string, different vowel check
# Input: my_str (string) - a string of characters
# Output: count (int) - the number of vowels in the string
# Notes: Uses an if statement to check for each vowel
def count_vowels2(my_str):
    count = 0
    for char in my_str:
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            count += 1
    return count

# Description: Count number of vowels in a string, different loop
# Input: my_str (string) - a string of characters
# Output: count (int) - the number of vowels in the string
# Notes: Uses an index to access characters in the string
# Notes: Uses a for loop to iterate over the indices
def count_vowels3(my_str):
    vowels = "aeiouAEIOU"
    count = 0
    for index in range(len(my_str)):
        char = my_str[index]
        if char in vowels:
            count += 1
    return count

# Description: Build a string that contains each occurrence of a vowel in a string,
#              in the order they occur, and return it. For example:
#              get_vowel_string("hello") returns "eo"
# Input: my_str (string) - a string of characters
# Output: vowel_str (string) - a string
# Notes: Uses "+" to concatenate strings
def get_vowel_string(my_str):
    vowel_str = ""
    vowels = "aeiouAEIOU"
    for char in my_str:
        if char in vowels:
            vowel_str += char
    return vowel_str

# Description: Build a string that contains each occurrence of a vowel in a string,
#              in the order they occur, followed by any other characters, and return it. For example:
#              rearrange_vowels("hello") returns "eohll"
# Input: my_str (string) - a string of characters
# Output: new_str (string) - a string
# Notes: Uses "+" to concatenate strings
def rearrange_vowels(my_str):
    vowel_str = ""
    other_str = ""
    vowels = "aeiouAEIOU"
    for char in my_str:
        if char in vowels:
            vowel_str += char
        else:
            other_str += char
    new_str = vowel_str + other_str
    return new_str

# Description: Build a string that contains a single occurrence of each unique character in a string.
#              For example:
#              unique_chars("Mississippi") returns "Misp"
#              unique_chars("hello") returns "helo"
#              unique_chars("abc") returns "abc"
# Input: my_str (string) - a string of characters
# Output: new_str (string) - a string
# Notes: Uses "not" operator to check if a character is not in the new string
def unique_chars(my_str):
    new_str = ""
    for char in my_str:
        if char not in new_str:
            new_str += char
    return new_str

# Description: Build a string that contains the left and right substrings when the 
#              first occurrence of a character is removed from a string. For example: 
#              remove_char("hello", "l") returns "helo"
#              remove_char("dgibson@valdosta.edu", "@") returns "dgibsonvaldosta.edu"
# Input: my_str (string) - a string of characters
# Input: char_to_remove (string) - a character
# Output: new_str (string) - a string
# Notes: Uses string splicing 
# Examples: my_str = 'http://en.wikipedia.org/wiki/Nasa/'
# Syntax    Result    Description
# my_str[10:19]    wikipedia    Returns the characters in indices 10-18.
# my_str[10:-5]    wikipedia.org/wiki/    Returns the characters in indices 10-28.
# my_str[8:]       n.wikipedia.org/wiki/Nasa/    Returns all characters from index 8 until the end of the string.
# my_str[:23]      http://en.wikipedia.org    Returns every character up to index 23, but not including my_str[23].
# my_str[:-1]      http://en.wikipedia.org/wiki/Nasa    Returns all but the last character.

def remove_char(my_str, char_to_remove):
    new_str = ""
    left_str = ""
    righ_str = ""
    loc = my_str.find(char_to_remove)
    if loc != -1:
        left_str = my_str[:loc]
        righ_str = my_str[loc+1:]
        new_str = left_str + righ_str
        return new_str
    else:
        return my_str;

# Description: Build a string that contains the left and right substrings when the 
#              first occurrence of a character (regardless of case) is removed from a string. For example: 
#              remove_char("DAave", "a") returns "Dave"
#              remove_char("make", "E") returns "mak"
# Input: my_str (string) - a string of characters
# Input: char_to_remove (string) - a character
# Output: new_str (string) - a string
# Notes: Uses "not" operator to check if a character is not in the new string
def remove_char2(my_str, char_to_remove):
    new_str = ""
    left_str = ""
    righ_str = ""
    lc_my_str = my_str.lower()
    lc_char_to_remove = char_to_remove.lower()
    loc = lc_my_str.find(lc_char_to_remove)
    if loc != -1:
        left_str = my_str[:loc]
        righ_str = my_str[loc+1:]
        new_str = left_str + righ_str
        return new_str
    else:
        return my_str;
    
# Description: Accepts two strings, x and y. If y occurs in x, regardless of case, then return the string 
# that is the same as x, except that y is removed. If y doesn't occur in x, then return x. We are only 
# concered with the first occurrence of y in x, from left to right. It doesn't matter if there are 
# additional occurrences. For example:
#              remove_char("Paul Woods Gibson", "woods ") returns "Paul Gibson"
#              remove_char("ABCXYZDEFGH", "xyz") returns "ABCDEFGH"
#              remove_char("12ab34ab56", "ab") returns "1234ab56"
# Input: my_str (string) - a string of characters
# Input: str_to_remove (string) - 
# Output: new_str (string) - a string
# Notes: Uses "not" operator to check if a character is not in the new string
def remove_string(my_str, str_to_remove):
    new_str = ""
    left_str = ""
    righ_str = ""
    lc_my_str = my_str.lower()
    lc_str_to_remove = str_to_remove.lower()
    loc = lc_my_str.find(lc_str_to_remove)
    if loc != -1:
        left_str = my_str[:loc]
        righ_str = my_str[loc+len(str_to_remove):]
        new_str = left_str + righ_str
        return new_str
    else:
        return my_str;

def replace_pi2(my_string):
    left = ''
    right = ''
    pi = '3.14'
    loc = 'pi'

    if loc in my_string:
        location = my_string.find(loc) # new
        left = my_string[:location]
        right = my_string[location+len(loc):]
        return left + pi + right
    else:
        return my_string

msg = "davepigibson"
print(replace_pi2(msg))


