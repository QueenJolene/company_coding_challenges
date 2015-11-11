f = open("data.txt", "r")

f.readlines

for line in f:
	new_line=line.strip()
	wordlist= new_line.split(",")

	print wordlist