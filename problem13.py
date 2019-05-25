#PF-Prac-13
'''
Write a python function which accepts three numbers and returns True if
a.	one of the three numbers is "close" to any one of the other numbers (differing from a number by at most 1), and

b.Number that is left out is "far", differing from both other values by 2 or more.

Return false if the above mentioned conditions are not satisfied.
'''
import math

def close_number(num1,num2,num3):
    if math.fabs(num1-num2)==1 and math.fabs(num3-num2)>=2 and math.fabs(num3-num1)>=2:
        return True
    elif math.fabs(num3-num2)==1 and math.fabs(num1-num2)>=2 and math.fabs(num3-num1)>=2:
        return True
    elif math.fabs(num1-num3)==1 and math.fabs(num3-num2)>=2 and math.fabs(num2-num1)>=2:
        return True
    else:
        return False
