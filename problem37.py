#PF-Prac-37
'''
Complete given function such that it returns the sum of the elements in num_list where num_list is a list of numbers.
Do not alter the statements already provided.
'''
def sum_of_list(num_list):
    if(len(num_list)>1):
        return num_list[0] + sum_of_list(num_list[1:])
    else:
        return num_list[0]
num_list=[44,23,77,11,89,3]
result=sum_of_list(num_list)
print("Sum of the elements:",result)
