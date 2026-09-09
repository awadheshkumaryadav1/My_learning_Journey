def cal_sum(a,b):
	sum=a+b
	print(sum)
	return sum

cal_sum(2,3)
cal_sum(21,3)
cal_sum(12,3)

def sum(a,b):
	return a+b

sum=sum(1,2)
print(sum)

# without parameter
def print_hello():
	print("hello")

print_hello()

# average of three number
def cal_avg(a,b,c):
	sum=a+b+c
	average=sum/3
	print(average)
	return average

cal_avg(1,2,3)

# default parameter

# def cal_product(a,b):
# 	print(a*b)
# 	return a*b

# cal_product()

# default parameter

def cal_product(a,b=4):
	print(a*b)
	return(a*b)

cal_product(6)

# waf to print the length of a list.(list is a parameter)
l=[1,2,3,4,5]
def print_length(list):
	print(len(list))
	return list
                                                               
print_length(l)

cities=["Muzaffarpur","jahanabad","sarmastpur","patna"]
actor=["hritik","prabhas","ram charn","mahesh babu","allu arjun","akshay"]

def length(list):
	print(len(list))
	return list

length(cities)
length(actor)

# Waf to print the element of a list  in single line. (list is parameter)

list1=[1,2,3,4,5]
list2=[1,22,33,4,5]

def singleline(list):
	print(list,end=" ")

singleline(list1)
singleline(list2)
print(list1[0],end=" \n")
print(list1[1],end=" ")
print(list1[2])

def print_list2(list3):
	for item in list3:
		print(item,end=" ")

print_list2(list1)
print_list2(actor)
# print()              # % symbol hatne ke liye ye line

# Factorial using function
# n=5
# fact=1
# for i in range(1,n+1):
# 	fact*=i
# print(fact)
def facto(n):
	fact=(1)
	for i in range(1,n+1):
		fact=fact*i
	print(fact)

facto(25)

# Waf to convert USD to INR
# n=int(input("Enter usd number"))
# inr=n*83
# print(inr)

def usd_conversion(n):
	inr=n*83
	print(inr)

usd_conversion(2)

def converter(usd_val):
	inr_value=usd_val*83
	print(usd_val,"usd_val=",inr_value,"in inr_value")

converter(3)	

# Waf to print odd string if given no. is odd and print even string if number is even.
n=int(input("Enter number="))
if(n%2==0):
	print("string is even")
else:
	print("string is odd")

# using function 
def cond(n):
	if(n%2==0):
		print("string is even")
	else:
		print("string is odd")

cond(6)		



	 