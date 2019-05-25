#PF-Prac-29
'''
Given a list of numbers, write a python function to exchange the first n/2 elements of a list with the last n/2 elements. The function should return the new list.
n represents the number of elements in the list. Assume that it will always be even.
'''
def exchange_list(number_list):
    #start writing your code here
    j=len(number_list)-1
    for i in range(len(number_list)//2):
        temp=number_list[i]
        number_list[i]=number_list[j]
        number_list[j]=temp
    
    return number_list
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))
