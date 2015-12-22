import re

tokens = ("OP", "AT", "NO", "VA")

op1 = (";", ",", "(", ")",  "=",  "+", "-", ".")
op2 = (":-", "'/=")

# oper = r"[;,\(\)(:-)=(/=)\+\-\.]"
# atoms = r"([a-z][a-zA-Z0-9_]*) | (\'.\') "
# nums = r"[0-9]+(\.[0-9])*"
# var = r"[_A-Z][a-zA-Z0-9_]*"

symbolTable = []
count = 0

with open("file.pl") as prolFile :
	for line in prolFile :
		symbolTable.append([])
		i = 0
		while(i < len(line)):
			ch = line[i]
			tok = ()

			if ch in op1 :
				tok = ("OP", ch)
			elif  i+1 < len(line) and (ch+line[i+1]) in op2 :
				tok +=('OP', ch+line[i+1])
				i+=1

			if ch is "'" :
				i+=1
				tmp = ch
				while i < len(line) and line[i] is not "'" :
					tmp+=line[i]
					i+=1

				tmp+=ch

				tok += ("AT", tmp)

			if ch.islower() :
				i+=1
				tmp = ch
				while i < len(line) and (line[i].isalpha() or line[i].isdigit() or line[i] is "_") :
					tmp+=line[i]
					i+=1
				i-=1
				tok += ("AT", tmp)

			if ch.isupper() or ch is "_" :
				i+=1
				tmp = ch
				while i < len(line) and (line[i].isalpha() or line[i].isdigit() or line[i] is "_") :
					tmp+=line[i]
					i+=1
				i-=1
				tok += ("VA", tmp)

			if ch.isdigit() :
				i+=1
				tmp = ch
				flag = True
				while i < len(line) and (line[i].isdigit() or (line[i] is '.' and flag)):
					if line[i] is '.' :
						flag = False
					tmp+=line[i]
					i+=1
				i-=1
				tok += ("NO", tmp)

			if ch.isspace() :
				i+=1
				while i < len(line) and line[i].isspace() :
					i+=1
				continue

			print(tok)

			symbolTable[count].append(tok)
			i+=1

		count+=1

# print(symbolTable)

