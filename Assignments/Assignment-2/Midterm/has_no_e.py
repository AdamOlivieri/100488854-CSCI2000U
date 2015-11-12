def has_no_e(line)
	if line.count('e') = 0:
	return true
	else:
	return false

reader = open('gadsby_stripped.txt', 'r')
line = reader.readline()
total = 0
count = 0
while line != '':
	count +=1
	total += len(line)
	line = reader.readline()
	has_no_e(line)
reader.close()
