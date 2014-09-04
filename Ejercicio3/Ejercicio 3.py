def palindromo(cad):
	if cad[::-1]==cad:
		return "true"
	else:
		return "false"
print palindromo("radar")
raw_input()