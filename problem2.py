#PF-Prac-2
'''
Write a python function which accepts a string containing a pattern of brackets and returns true if the pattern of brackets is correct. Otherwise it returns false.
The string of brackets is correct if it satisfies the following conditions:
1. Number of opening and closing brackets are equal.
2. Pattern should not start with closing bracket and end with opening bracket
'''
def bracket_pattern(input_str):
    #Remove pass and write your code here
	c1=input_str.count(")")
	c2=input_str.count("(")
	if(input_str.startswith(")") or input_str.endswith("(")):
	    return False
	elif(c1==c2):
	    return True
	else:
	    return False

    
input_str="(())("
print(bracket_pattern(input_str))
