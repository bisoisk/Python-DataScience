#Area calculation function...

def traingle_area(base,height):
    area=(1.0/2)*base*height
    return area
Areat_test=traingle_area(12,60)
print Areat_test
Area_Test2=traingle_area(102,610)
print Area_Test2

#Fahrenite & celicius calculation...
def convert_F_C(fahrenite):
    celcius=(5.0/9)*(fahrenite-32)
    return celcius
c1=convert_F_C(32)
c2=convert_F_C(232)
print c1,c2

# celcius to kelvin ..through a function through another function...
def Convert_C_K(fahrenite):     #def means ---definition of function 
    c11=convert_F_C(fahrenite)
    k1=c11+273.30
    return k1
k1_test=Convert_C_K(32)
k2_test=Convert_C_K(212)
print k1_test,k2_test

#print hello world...
def hello():
    print "Hello.. World!"
    return hello()
h1=hello()

print h1

"""
problem for division
"""
num_1=49
tens_1=49//10
one_1=49%10
print tens_1,one_1

# application - 24 hour clock
# http://en.wikipedia.org/wiki/24-hour_clock

hour = 20
shift = 8
print (hour + shift) % 24


"""
Write a Python function miles_to_feet that takes a parameter miles and returns the number of feet in miles miles
"""


""" 
Logic & Conditions

"""
a_1=True
b_1=False
print a_1
print b_1
print '@@@@@@'

print not a_1
print not b_1
print '@@@@@@'

print a_1 and b_1
print a_1 or b_1
print (a_1 and b_1) or (a_1 or b_1)

"""
Comparision Operator

>
<
>=
<=
==
!=

"""

x_1=3
print x_1==3

"""
For Conditional statements...
"""

def greet(friend, money):
    
    if friend and (money > 20):
        print "Hi!"
        money = money - 20
    elif friend:
        print "Hello"
    else:
        print "Ha ha"
        money = money + 10
    return money


money = 15

money = greet(True, money)
print "Money:", money
print ""

money = greet(False, money)
print "Money:", money
print ""

money = greet(True, money)
print "Money:", money
print ""

"""
Leap Year
"""

# Conditionals Examples

# Return True if year is a leap year, false otherwise
def is_leap_year(year):
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False

#year = 2012
year=raw_input()
leap_year = is_leap_year(year)
    
if leap_year:
    print year, "is a leap year"
else:
    print year, "is not a leap year"


