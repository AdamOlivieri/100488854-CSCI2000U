file_to_read = open('gadsby_stripped.txt', 'r')

def has_no_e(the_string):
	for i in the_string.readlines():
		if 'e' not in i:
			print("False")
			return False
		else:
			print("True")
			return True
			
has_no_e(file_to_read)

file_to_read.close()
