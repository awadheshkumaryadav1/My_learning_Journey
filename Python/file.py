# data=f.read() # reads entire line

f=open("textfiles.txt","r")
data=f.read(6)   #starting 6 elements read
print(data)
print(type(data))
f.close()

# data=f.readline()  # reads one line a time
f=open("textfiles.txt","r")
data=f.readline() # read only one line
print(data)
data2=f.readline() # read only one line
print(data2)
print(type(data))
f.close()  
#  Note: agar pura data phle hi read ho gya tab ham readline() use kate hai tab blank line aayega


#Writing in a file

#there are two ways 'w' or 'a'
# start 
# 1st open file 
# w write
f=open("textfiles.txt","w")
f.write( "hello")
f.close()
# a append
f=open("textfiles.txt","a")
f.write( "\n ak")
f.close()
#  create sample file
f=open("sample.txt","w")
f.close()
# r+ 
f=open("sample.txt","w")
f.write("hello i am ready to speak")
f=open("sample.txt","w+")
f.write("go")
print(f.read())
f.close()

# with syntax 
with open("demo.txt","r") as f:
	print(f.read())
	# close() is not compulsary because in with syntax file is automatically closed
with open("demo.txt","w") as f:
	f.write("new data")	





