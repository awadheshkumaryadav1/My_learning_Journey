# def check_word_in_line():
# 	no=1
# 	data=True
# 	line_no=0
	
# 	with open("practice.txt","r") as f:
# 		while data:
# 			data=f.readline()
# 			if line_no==no:
# 				print(line_no)
# 				x=f.readline()
# 				print(x)
# 				return
# 			line_no +=1
# 	return -1	 
def check_word_in_line():
    no = 1  # The target line number
    line_no = 0  # Tracks the current line number

    with open("practice.txt", "r") as f:
        while True:
            data = f.readline()  # Read each line
            if not data:  # Stop when no more lines to read (end of file)
                break
            if line_no == no:  # If current line number matches the target
                print(f"Line {line_no}: {data.strip()}")  # Print the line
                return
            line_no += 1  # Move to the next line
    
    print(f"Line {no} not found")
    return -1
