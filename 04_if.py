x=40
try:
	while True:
		numero = int (raw_input ("introduce un numero "))
		if numero == x:
			print "lo has adivinado"
			break
		elif x <= 20 and x <= 20 and numero != x:
			print "estas cerca"
			print "prueba otro numero menor que 20"
		elif x > 20 and x <= 39 and numero != x:
			print "estas cerca"
			print "prueba otro numero menor de 39"
		elif x > 39 and x <= 60 and numero != x:
			print "estas cerca"
			print "prueba otro numero menor de 60"
		else x > 60 and numero != x:
			print "prueba otro nunero mayor de 60"
except KeyboardInterrupt:
	print "FIN"
