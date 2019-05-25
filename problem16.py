#PF-Prac-16
'''
Write a Python function to rotate the list of elements by N positions. The function should return the rotated list.
'''
def rotate_list(input_list,n):
    #start writing your code here
    output_list=[]
    for i in range(len(input_list)-n,len(input_list)):
        output_list.append(input_list[i])
    for i in range(len(input_list)-n):
        output_list.append(input_list[i])
    
    
    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)
