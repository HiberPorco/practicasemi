def secuencia(n):
	for i in range(n):
		s=""
		for j in range(i+1):
			s=s+str(i+1)
		print s
	while n>0:
		s=""
		for j in range(n-1):
			s=s+str(n-1)
		print s
		n=n-1
secuencia(5)
raw_input()