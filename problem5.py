#PF-Prac-5
'''
Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.
It should return a list in which the first value should be letter count and second value should be digit count. 
Ignore the spaces or any other special character in the sentence.
'''
def count_digits_letters(sentence):
    #start writing your code here
    c1=0
    c2=0
    result_list=[]
    for i in sentence:
        if((i>="a" and i<="z") or (i>="A" and i<="Z")):
            c1+=1
        if(i>="0" and i<="9"):
            c2+=1
    result_list.append(c1)
    result_list.append(c2)

    
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
