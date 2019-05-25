#PF-Prac-29
'''
Given a list of numbers, write a python function to exchange the first n/2 elements of a list with the last n/2 elements. The function should return the new list.
n represents the number of elements in the list. Assume that it will always be even.
'''
def exchange_list(number_list):
    #start writing your code here
    d=len(number_list)
    a=len(number_list)//2
    b=a//2+a
    k=0
    for i in range(a,b):
        c=number_list[i]
        number_list[i]=number_list[d-k-1]
        number_list[d-k-1]=c
    for i in range(a):
        temp=number_list[i]
        number_list[i]=number_list[i+a]
        number_list[i+a]=temp
    return number_list

    
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))
