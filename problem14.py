#PF-Tryout
'''
Write a python function to find and display the five digit number in which the first digit is two more than the second, 
the second digit is two more than the third, the fourth digit is two less than the third, and the last digit is two more 
than the fourth. The sum of the third, fourth, and fifth digits equals the first. The sum of all the digits is 19.
''''
def find_five_digit():
    num2=0
    num3=0
    num4=0
    num5=0
    for i in range(9,-1,-1):
        num2=int(i-2)
        num3=int(num2-2)
        num4=int(num3-2)
        num5=int(num3)
        if(num3+num4+num5==i and num2+num3+num4+num5+i==19):
            break
    s=str(i)+str(num2)+str(num3)+str(num4)+str(num5)
    print(s)

find_five_digit()
