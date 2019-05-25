#PF-Prac-23
'''
Write a python function to find out whether a number is divisible by the sum of its digits. If so return True,else return False.
'''
def divisible_by_sum(number):
    temp=number
    sum=0
    while(number>0):
        rem=number%10
        number=number//10
        sum+=rem
    if(temp%sum==0):
        return True
    else:
        return False
    #start writing your code here

    
number=51
print(divisible_by_sum(number))
