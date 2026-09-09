# 1.
print(" question no.1")
#     *
#    ***
#   *****
#  *******
# *********

rows=5
for i in range(1,rows+1):
    print(' ' *(rows-i)+ "*" *(2*i-1))
    
# 2.   
print(" question no.2")
# *********
#  *******
#   *****
#    ***
#     *
rows=5
for i in range(rows,0,-1):
    print(' '*(rows-i)+'*' *(2*i-1))

# 3.
print(" question no.3")
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *
rows=5
for i in range(1,rows+1):
    print(' ' *(rows-i)+ "*" *(2*i-1))
rows=5
for i in range(rows,0,-1):
    print(' '*(rows-i)+'*' *(2*i-1))
    
# 4.
print(" question no.4")
rows=5
for i in range(1,rows+1):
    print(' ' *(rows-i)+ "*" *(i))
    

print(" question no.5")
rows=5
for i in range(1,rows+1):
    print("*" *(i))
    
print(" question no.6")
rows=5
for i in range(rows,rows+1):
    for j in range(5):
        print("*" *(i))
        
        
print("question number 7")
row=5
for i in range(1,row+1):
    for j in range(1 ,row+1):
        if i==1 or i==row or j==1 or j==row:
            print("*",end="")
        else:
            print(" ",end="")
    print()
