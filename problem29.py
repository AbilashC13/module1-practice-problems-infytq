#PF-Prac-29
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
