def show(n):
	if(n==-2):
		return
	print(n)
	show(n-1)
		
show(5)

# factorial
def fact(n):
	if(n==1 or n==0):
		return 1
	return fact(n-1)*n
	
print(fact(5))	

# sum of n natural number

def sum_of_natural_no(n):
	if(n==0):
		return 0
	return sum_of_natural_no(n-1)+ n

sum=sum_of_natural_no(5)
print(sum)

# Waf a recursive function to print all elemnts in a list. 

# l=[1,2,3,4,5,"hello"]
# def li(list):
# 	print(list)
# 	return list

# li(l)	


def print_list(list,idx=0):
	if(idx==len(list)):
		return
	print(list[idx])
	print_list(list,idx+1)


num=[1,23,4,56,7,]	
	
print_list(num)	             