print "BIENVENIDO A LA CALCULADORA PERSONAL DE PYTHON"
print " QUE OPERACION DESEA REALIZAR "
print "1.suma"
print "2.resta"
print "3.multiplicacion"
print "4.division"
print "5.exponencial"
def suma ():
	z = x + y
	print z
def resta ():
        z = x - y
        print z
def multiplicacion ():
        z = x * y
        print z
def division ():
        z = x / y
        print z
def exponencial ():
        z = x ** y
        print z
try:
	while True:
		menu = raw_input(" ELIJA UNA DE LAS OPCIONES " )
		if menu == "1":
			x = int (raw_input("introduce un numero " ))
			y = int (raw_input("introduce otro numero " ))
			suma()
		if menu == "2":
       			x = int (raw_input("introduce un numero " ))
        		y = int (raw_input("introduce otro numero " ))
        		resta()
		if menu == "3":
        		x = int (raw_input("introduce un numero " ))
        		y = int (raw_input("introduce otro numero " ))
        		multiplicacion()
		if menu == "4":
        		x = float (raw_input("introduce un numero " ))
        		y = float (raw_input("introduce otro numero " ))
        		division()
		if menu == "5":
        		x = int (raw_input("introduce un numero " ))
        		y = int (raw_input("introduce otro numero " ))
        		exponencial()
		else:
			print(" ELIJA UNA OPCION CORRECTA ")
except KeyboardInterrupt:
	print " HA CERRADO LA CALCULADORA"

