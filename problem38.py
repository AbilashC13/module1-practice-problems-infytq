#PF-Prac-38
'''
University of Washington CSE140 Mid term 2015

Write a function build_index_grid(rows, columns) that, given a number of rows and columns, creates a list of lists of that shape that includes the 'row,column' of that location.

For example, after the following code is executed: new_index_grid = build_index_grid(4,3)
new_index_grid would contain:
[['0,0', '0,1', '0,2'],
['1,0', '1,1', '1,2'],
['2,0', '2,1', '2,2'],
['3,0', '3,1', '3,2']]
Note that these are strings.

After the following code is executed: small_index_grid = build_index_grid(1,1)
small_index_grid would contain: [ ['0,0'] ]
'''
def build_index_grid(rows, columns):
    result_list=[]
    s=""
    for i in range(0,rows):
        for j in range(0,columns):
            if(i==0 and j==0):
                s=s+"["
            if(j==0):
                s=s+"["
            s=s+"'"+str(i)+","+str(j)+"'"
            if(j!=(columns-1)):
                s=s+","
            if(j==(columns-1) and j==(columns-1) and i!=(rows-1)):
                s=s+"],"
            if(j==(columns-1) and i==(rows-1)):
                s=s+"]]"
        result_list.append(s)
        s=""
    return result_list

rows=4
columns=3
result=build_index_grid(rows,columns)
print("Rows:",rows,"Columns:",columns)
print("The matrix is:",result)
for i in result:
    print(i)
