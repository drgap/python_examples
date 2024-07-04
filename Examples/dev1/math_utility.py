import math
def divide_by_2(n):
    if n==0 or n==1: 
        return 0# T
    count = 0
    while n%2 == 0:
        n = n/2
        count += 1
        
    return count

def largest_n():
    n=1
    current_n = n;
    while math.pow(n, 3) < 12000:
        current_n = n;
        n += 1
    return current_n

def largest_n2():
    val = math.pow(12000, 1/3)
    val = int(val);
    return val;

def find_gcd(n1, n2):
    gcd = 1
    k = 2
    while k <= n1 and k <= n2:
        if (n1 % k == 0 and n2 % k == 0):
            gcd = k
        k += 1
    return gcd

def find_gcd2(n1, n2):
    gcd = 1
    k = 2
    n = min(n1, n2)
    while k <= n:
        if (n1 % k == 0 and n2 % k == 0):
            gcd = k
        k += 1
    return gcd

def find_gcd3(n1,n2):
    first = max(n1,n2)
    second = min(n1,n2)
    while second != 0:
        temp = second
        second = first % second
        first = temp
    return first
    
    
    
    
def confidence_interval_bad(nums):
    # calc average
    sum2 = 0.0
    for n in nums:
        sum2 += n
    avg2 = sum2/len(nums)

    # calc standard deviation
    sum2 = 0.0
    for n in nums:
        diff = n - avg2
        sum2 += math.pow(diff, 2)
    sum2 = sum2 / (len(nums)-1)
    sd = math.sqrt(sum2)
    
    # get number of values
    n = len(nums)
    # calc margin of error
    me = 1.96 * sd / math.sqrt(n)
    # calculate and return confidence interval
    ll = avg2 - me
    ul = avg2 + me
    ci = (ll, ul)
    return ci

def confidence_interval(nums):
    # calc parameters
    avg2 = x_bar(nums)
    sd = std_dev(nums, avg2)
    n = len(nums)
    # calc margin of error
    me = 1.96 * sd / math.sqrt(n)
    # calculate and return confidence interval
    ll = avg2 - me
    ul = avg2 + me
    ci = (ll, ul)
    return ci
    
def x_bar(nums):
    sum2 = 0.0
    for n in nums:
        sum2 += n
    return sum2/len(nums)

def std_dev(nums, avg2):
    sum2 = 0.0
    for n in nums:
        diff = n - avg2
        sum2 += math.pow(diff, 2)
    sum2 = sum2 / (len(nums)-1)
    sd = math.sqrt(sum2)
    return sd