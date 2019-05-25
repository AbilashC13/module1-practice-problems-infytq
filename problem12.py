#PF-Prac-12
'''
Write a python function to generate and return the list of all possible sentences created from the given lists of Subject,
Verb and Object.
Note: The sentence should contain only one subject, verb and object each.
'''
def generate_sentences(subjects,verbs,objects):
    sentence_list=[]
    for i in subjects:
        for j in verbs:
	        for k in objects:
	            sentence_list.append(i+" "+j+" "+k)
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))
