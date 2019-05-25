#PF-Prac-4
'''
Given a list of numbers, write a python function which returns true if one of the first 4 elements in the list is 9. Otherwise it should return false.
The length of the list can be less than 4 also.
'''
def find_nine(nums):
    #Remove pass and write your code here
	for i in range(len(nums)):
	    if(nums[i]==9 and i<4):
	        return True
	return False
    

nums=[1,2,4,9]
print(find_nine(nums))
