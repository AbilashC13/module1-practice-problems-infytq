#PF-Prac-26
'''
Given a string, write a python function to return True if the strings "mat" and "jet" appear the same number of times in the given string, else return False.
Note: Perform case insensitive string comparison wherever necessary.
'''
def check_occurence(string):
    #start writing your code here
    string=string.lower()
    a=string.count("jet")
    b=string.count("mat")
    if(a==b):
        return True
    else:
        return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))
