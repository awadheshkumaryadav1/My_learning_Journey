# q1
f=open("practice.txt","w")
f.write("Hi eveyone\nwe are learning File I/O\nusing java\nI like programming in java\n1,2,3,4,5,6,7,8,12,13,14,151,116,16")
f.close()

# q2
f=open("practice.txt","r")
data=f.read()
# print(data)
new_f=data.replace("java","python")
print(new_f)

word="xlearning"
f=open("practice.txt","r")
data=f.read()
if(data.find(word)!=-1):
	print("found")
else:
	print("not found")

# using function 
def check():
	word="learning"
	f=open("practice.txt","r")
	data=f.read()
	if(data.find(word)!=-1):
		print("found")
	else:
		print("not found")
		 
check()

def check_word_in_line():
	word="learning"
	data=True
	line_no=0
	
	with open("practice.txt","r") as f:
		while data:
			data=f.readline()
			if(word in data):
				print(line_no)
				x=f.readline()
				print(x)
				return
			line_no +=1
	return -1	 

check_word_in_line() #none because of print


# with open("practice.txt","r") as f:
# 	data=f.read()
# 	print(data)
# 	if data/2==0:
# 		print("even",data)





