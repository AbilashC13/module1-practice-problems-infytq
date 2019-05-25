#PF-Prac-31
'''
Given a list of integers and a number. Write a python function to find and return the sum of the elements of the list. 
Note: Don't add the given number and also the numbers present before and after the given number in the list .
'''
def sum_of_elements(num_list,number):
    a=len(num_list)
    result_sum=0
    for i in range(1,a-1):
        if(num_list[i-1]!=number and num_list[i+1]!=number and num_list[i]!=number):
            result_sum+=num_list[i]
    if(num_list[1]!=number and num_list[0]!=number):
        result_sum+=num_list[0]
    if(num_list[a-2]!=number and num_list[a-1]!=number):
        result_sum+=num_list[a-1]
    return result_sum
      
num_list=[1,2,1,2]
number=2
print(sum_of_elements(num_list, number))
