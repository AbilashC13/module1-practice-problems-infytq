#PF-Prac-32
'''
Given an integer n, write a python function to return true, if it is possible to represent it as a sum of the squares of 
two different integers, else return false.
'''
def check_squares(number):
    for i in range(1,10000):
        for j in range(i+1,10000):
            if(i*i + j*j ==number):
                return True
    return False


number=68
print(check_squares(number))
