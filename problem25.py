#PF-Prac-25
'''
Write a python function that accepts a list of words and returns the list of integers representing the length of the 
corresponding words.
'''
def list_of_count(word_list):
    #start writing your code here
    count_list=[]
    for i in word_list:
        x=len(i)
        count_list.append(x)
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))
