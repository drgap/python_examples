from dev1.math_utility import divide_by_2
from dev1.math_utility import largest_n
from dev1.math_utility import largest_n2
from dev1.math_utility import find_gcd
from dev1.math_utility import *

def test_divide_by_2_n0():
    n = 0
    expected = 0
    actual = divide_by_2(n)
    print(f"n: {n}, Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_divide_by_2_n1():
    n = 1
    expected = 0
    actual = divide_by_2(n)
    print(f"n: {n}, Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_divide_by_2_n4():
    n = 4
    expected = 2
    actual = divide_by_2(n)
    print(f"n: {n}, Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_divide_by_2_n24():
    n = 24
    expected = 3
    actual = divide_by_2(n)
    print(f"n: {n}, Expected: {expected}, Actual: {actual}")
    #assert actual == expected
    
def test_divide_by_2_n16():
    n = 16
    expected = 4
    actual = divide_by_2(n)
    print(f"n: {n}, Expected: {expected}, Actual: {actual}")
    #assert actual == expected
    
def test_divide_by_2_n99():
    n = 99
    expected = 0
    actual = divide_by_2(n)
    print(f"n: {n}, Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_divide_by_2_n4096():
    n = 4096
    expected = 12
    actual = divide_by_2(n)
    print(f"n: {n}, Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_largest_n():
    expected = 22
    actual = largest_n()
    print(f"Largest n such that n**3<12000, Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_largest_n2():
    expected = 22
    actual = largest_n2()
    print(f"Largest n such that n**3<12000, Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_find_gcd_4_2():
    expected = 2
    n1 = 4
    n2 = 2
    actual = find_gcd(n1, n2)
    print(f"gcd({n1}, {n2}), Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_find_gcd_16_24():
    expected = 8
    n1 = 16
    n2 = 24
    actual = find_gcd(n1, n2)
    print(f"gcd({n1}, {n2}), Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_find_gcd_121_88():
    expected = 11
    n1 = 121
    n2 = 88
    actual = find_gcd(n1, n2)
    print(f"gcd({n1}, {n2}), Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_find_gcd2_121_88():
    expected = 11
    n1 = 121
    n2 = 88
    actual = find_gcd2(n1, n2)
    print(f"gcd2({n1}, {n2}), Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_find_gcd3_88_121():
    expected = 11
    n1 = 88
    n2 = 121
    actual = find_gcd3(n1, n2)
    print(f"gcd3({n1}, {n2}), Expected: {expected}, Actual: {actual}")
    #assert actual == expected

def test_find_confidence_interval():
    vals = [80, 90, 100, 100, 90]
    expected = (84.666, 99.334)
    actual = confidence_interval(vals)
    print(f"confidence_interval({vals}), Expected: {expected}, Actual: {actual}")
    #assert actual == expected


test_divide_by_2_n0()
test_divide_by_2_n1()
test_divide_by_2_n4()
test_divide_by_2_n24()
test_divide_by_2_n16()
test_divide_by_2_n99()
test_divide_by_2_n4096()
test_largest_n()
test_largest_n2()
test_find_gcd_4_2()
test_find_gcd_16_24()
test_find_gcd_121_88()
test_find_gcd2_121_88()
test_find_gcd3_88_121()
test_find_confidence_interval()