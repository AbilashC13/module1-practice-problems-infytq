#PF-Prac-11
'''
Write a python function which accepts a sentence and returns a list in which first value is the count of upper case letters 
and second value is the count of lower case letters in the sentence. Ignore spaces, numbers and other special characters if any.
'''
def find_upper_and_lower(sentence):
    #start writing your code here
    up=0
    lo=0
    for i in sentence:
        if(i>="a" and i<="z"):
            lo+=1
        if(i>="A" and i<="Z"):
            up+=1
    result_list=[]
    result_list.append(up)
    result_list.append(lo)

    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))
