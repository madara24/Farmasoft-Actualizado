from flask import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')



# Formulario de inicio de sión

@app.route('/login', methods=['GET', 'POST'])
def login():

	try:

		# Si hay una petición GET llamada "invalid".
		if request.method == "GET":
			
			# Verificamos que sea igual a nada o que tenga más de X caracteres.
			invalid = request.args.get("invalid")
			if invalid == "" or len(invalid) > 0:

				# Renderizamos el login con un mensaje de error.
				return render_template('login.html', error="error")

		# Verificamos si se ejecutó una petición POST.
		if request.method == "POST":

			# Obtenemos los datos de acceso ingresados.
			username = request.form["user"]
			password = request.form["pass"]


			# Leemos el CSV de cuentas de acceso.
			a = open('database/usuarios.csv')
			invalid = True
			with a as archivo:

				for line in archivo:
					
					# Obtenemos y separamos los datos leidos en la línea X.
					datos   = line.split(",")

					# Guardamos los datos por separado en variables, eliminando espacios.
					usuario = datos[0].strip()
					clave   = datos[1].strip()

					if username == usuario and password == clave:
						# Si la cuenta es válida, redireccionados a las últimas ventas.
						return redirect("ultimas_vtas/" + usuario)
						invalid = False

				# Si la cuenta es inválida, redireccionados al login, indicando error.
				if invalid == True:
					return redirect("login?invalid")

	except:
		# Si no pasa nada... no hacemos nada...
		pass

	return render_template('login.html', error="none")

@app.route('/register', methods=['GET', 'POST'])
def register():
		error = "none"
		# Verificamos si se ejecutó una petición POST.
		if request.method == "POST":

			# Obtenemos los datos de acceso ingresados.
			username = request.form["user"]
			password = request.form["pass"]
			repassword = request.form["repass"]

			# Abre archivo para escribir
			a = open('database/usuarios.csv','a')

			# Escribe username en el archivo añadiendo una coma(',') 
			a.write(username + ',')

			# Escribe password en el archivo
			a.write(password + '\n') 

			# cierra archivo
			a.close

			#Si la contraseña coincide con repetir contraseña
			if password == repassword:

				#Entonces redireccionamos para loguear
				return redirect("/login")
			else:
				error = "pass"


		return render_template('register.html', error=error)

@app.route('/ultimas_vtas/<usuario>')
def ultimas_vtas(usuario):

	# Declaramos variable de error.
	error = "none"
	cantidad_maxima = 5

	try:
		# Iniciamos un contador de lineas.
		i = 0

		# Declaramos lista de datos a mostrar.
		lista = []

		# Abrimos el CSV de ventas para lectura.
		a = open('database/ventas.csv')
		with a as archivo:

			# Leemos linea a linea.
			for line in archivo:

				# Separamos los valores y los guardamos en formato de lista.
				dato = line.split(",")

				# Leemos la primera linea para comprobar el orden de las columnas.
				if i == 0:

					# Indicamos el orden correspondiente de cada columna en diversas variables.
					for x in range(5):
						if dato[x].strip().lower() == "codigo":
							col_codigo = x
						elif dato[x].strip().lower() == "producto":
							col_producto = x
						elif dato[x].strip().lower() == "cliente":
							col_cliente = x
						elif dato[x].strip().lower() == "cantidad":
							col_cantidad = x
						elif dato[x].strip().lower() == "precio":
							col_precio = x

					# Terminamos el contador para pasar a identificar las ventas.
					i = 1

				else:

					# Definimos una lista temporal.
					temp = []

					# Parseamos los datos.
					codigo   = dato[col_codigo].strip()

					if codigo != "":

						cliente  = dato[col_cliente].strip()
						producto = dato[col_producto].strip()
						cantidad = int(float(dato[col_cantidad].strip()))
						precio   = dato[col_precio].strip().split(".")
						precio   = str(precio[0] + "." + precio[1][:2])

						if int(cantidad):

							# Guardamos los valores parseados en la lista temporal.
							temp.append( codigo )
							temp.append( producto )
							temp.append( cliente )
							temp.append( cantidad )
							temp.append( precio )

							# Guardamos los datos de la lista temporal en la lista principal.
							lista.append(temp)
					else:
						# Si hay un codigo vacio, devolvemos error.
						error = "codigo"
	except:
		error = "archivo"


	return render_template('ultimas_vtas.html', usuario=usuario, ventas=lista[-cantidad_maxima::][::-1], error=error)


@app.route('/segun_cliente/<usuario>', methods=['GET', 'POST'])
def segun_cliente(usuario):

	# Declaramos variable de error.
	error = "none"

	try:
		# Iniciamos un contador de lineas.
		i = 0

		# Declaramos lista de datos a mostrar.
		item = []

		# Abrimos el CSV de ventas para lectura.
		a = open('database/ventas.csv')
		with a as archivo:

			# Leemos linea a linea.
			for line in archivo:

				# Separamos los valores y los guardamos en formato de lista.
				dato = line.split(",")

				# Leemos la primera linea para comprobar el orden de las columnas.
				if i == 0:

					# Indicamos el orden correspondiente de cada columna en diversas variables.
					for x in range(5):
						if dato[x].strip().lower() == "codigo":
							col_codigo = x
						elif dato[x].strip().lower() == "producto":
							col_producto = x
						elif dato[x].strip().lower() == "cliente":
							col_cliente = x
						elif dato[x].strip().lower() == "cantidad":
							col_cantidad = x
						elif dato[x].strip().lower() == "precio":
							col_precio = x

					# Terminamos el contador para pasar a identificar las ventas.
					i = 1

				else:

					# Definimos una lista temporal.
					temp = []

					# Parseamos los datos.
					codigo   = dato[col_codigo].strip()

					if codigo != "":

						cliente  = dato[col_cliente].strip()
						producto = dato[col_producto].strip()
						cantidad = int(float(dato[col_cantidad].strip()))
						precio   = dato[col_precio].strip().split(".")
						precio   = str(precio[0] + "." + precio[1][:2])

						if request.method == "POST":

							if cliente.find(request.form["cliente"].upper())  >= 0:

								if int(cantidad):

									# Guardamos los valores parseados en la lista temporal.
									temp.append( codigo )
									temp.append( producto )
									temp.append( cliente )
									temp.append( cantidad )
									temp.append( precio )

									# Guardamos los datos de la lista temporal en la lista principal.
									item.append(temp)
					else:
						# Si hay un codigo vacio, devolvemos error.
						error = "codigo"
	except:
		error = "archivo"	

	return render_template('segun_cliente.html', usuario=usuario, ventas=item)

@app.route('/segun_producto/<usuario>', methods=['GET', 'POST'])
def segun_producto(usuario):

	# Declaramos variable de error.
	error = "none"

	try:
		# Iniciamos un contador de lineas.
		i = 0

		# Declaramos lista de datos a mostrar.
		item = []

		# Abrimos el CSV de ventas para lectura.
		a = open('database/ventas.csv')
		with a as archivo:

			# Leemos linea a linea.
			for line in archivo:

				# Separamos los valores y los guardamos en formato de lista.
				dato = line.split(",")

				# Leemos la primera linea para comprobar el orden de las columnas.
				if i == 0:

					# Indicamos el orden correspondiente de cada columna en diversas variables.
					for x in range(5):
						if dato[x].strip().lower() == "codigo":
							col_codigo = x
						elif dato[x].strip().lower() == "producto":
							col_producto = x
						elif dato[x].strip().lower() == "cliente":
							col_cliente = x
						elif dato[x].strip().lower() == "cantidad":
							col_cantidad = x
						elif dato[x].strip().lower() == "precio":
							col_precio = x

					# Terminamos el contador para pasar a identificar las ventas.
					i = 1

				else:

					# Definimos una lista temporal.
					temp = []

					# Parseamos los datos.
					codigo   = dato[col_codigo].strip()

					if codigo != "":

						cliente  = dato[col_cliente].strip()
						producto = dato[col_producto].strip()
						cantidad = int(float(dato[col_cantidad].strip()))
						precio   = dato[col_precio].strip().split(".")
						precio   = str(precio[0] + "." + precio[1][:2])

						if request.method == "POST":

							if producto.find(request.form["producto"].upper())  >= 0:

								if int(cantidad):

									# Guardamos los valores parseados en la lista temporal.
									temp.append( codigo )
									temp.append( producto )
									temp.append( cliente )
									temp.append( cantidad )
									temp.append( precio )

									# Guardamos los datos de la lista temporal en la lista principal.
									item.append(temp)
					else:
						# Si hay un codigo vacio, devolvemos error.
						error = "codigo"
	except:
		error = "archivo"	

	return render_template('segun_producto.html', usuario=usuario, ventas=item)

@app.route('/top_vendidos/<usuario>')
def top_vendidos(usuario):


	# Declaramos variable de error.
	error = "none"

	try:
		# Iniciamos un contador de lineas.
		i = 0

		# Declaramos lista de datos a mostrar.
		lista = []

		# Abrimos el CSV de ventas para lectura.
		a = open('database/ventas.csv')
		with a as archivo:

			# Leemos linea a linea.
			for line in archivo:

				# Separamos los valores y los guardamos en formato de lista.
				dato = line.split(",")

				# Leemos la primera linea para comprobar el orden de las columnas.
				if i == 0:

					# Indicamos el orden correspondiente de cada columna en diversas variables.
					for x in range(5):
						if dato[x].strip().lower() == "codigo":
							col_codigo = x
						elif dato[x].strip().lower() == "producto":
							col_producto = x
						elif dato[x].strip().lower() == "cliente":
							col_cliente = x
						elif dato[x].strip().lower() == "cantidad":
							col_cantidad = x
						elif dato[x].strip().lower() == "precio":
							col_precio = x

					# Terminamos el contador para pasar a identificar las ventas.
					i = 1

				else:

					# Definimos una lista temporal.
					temp = []

					# Parseamos los datos.
					codigo   = dato[col_codigo].strip()

					if codigo != "":

						cliente  = dato[col_cliente].strip()
						producto = dato[col_producto].strip()
						cantidad = int(float(dato[col_cantidad].strip()))
						precio   = float(dato[col_precio].strip())
						precio = round(precio,1)
						if int(cantidad):


								# Guardamos los valores parseados en la lista temporal.
								temp.append( codigo )
								temp.append( producto )
								temp.append( cliente )
								temp.append( cantidad )
								temp.append( precio )

								#for filas in temp:							
								#vuelta=vuelta+1
								#productos=[]
								#cantidades=[]
								#if (productos == filas[1]):
								#	cantidades=+filas[3]
								#	lista.append(( productos,cantidades))
								#else:
								#	if (vuelta==1):
								#		clientes=filas[1]
								#		cantidad=(columnas[3])
								#	else:
								#		lista.append(( productos,cantidades))
								#		productos=filas[1]
								#		cantidades=filas[3]

								# Guardamos los datos de la lista temporal en la lista principal.
								lista.append(temp)

								lista.sort(key=lambda cantidad:cantidad[3], reverse=True)
					else:
						# Si hay un codigo vacio, devolvemos error.
						error = "codigo"
	except:
		error = "archivo"

	return render_template('top_vendidos.html', usuario=usuario, ventas=lista, error=error)


@app.route('/top_clientes/<usuario>')
def top_clientes(usuario):


	# Declaramos variable de error.
	error = "none"

	try:
		# Iniciamos un contador de lineas.
		i = 0

		# Declaramos lista de datos a mostrar.
		lista = []

		# Abrimos el CSV de ventas para lectura.
		a = open('database/ventas.csv')
		with a as archivo:

			# Leemos linea a linea.
			for line in archivo:

				# Separamos los valores y los guardamos en formato de lista.
				dato = line.split(",")

				# Leemos la primera linea para comprobar el orden de las columnas.
				if i == 0:

					# Indicamos el orden correspondiente de cada columna en diversas variables.
					for x in range(5):
						if dato[x].strip().lower() == "codigo":
							col_codigo = x
						elif dato[x].strip().lower() == "producto":
							col_producto = x
						elif dato[x].strip().lower() == "cliente":
							col_cliente = x
						elif dato[x].strip().lower() == "cantidad":
							col_cantidad = x
						elif dato[x].strip().lower() == "precio":
							col_precio = x

					# Terminamos el contador para pasar a identificar las ventas.
					i = 1

				else:

					# Definimos una lista temporal.
					temp = []

					# Parseamos los datos.
					codigo   = dato[col_codigo].strip()

					if codigo != "":

						cliente  = dato[col_cliente].strip()
						producto = dato[col_producto].strip()
						cantidad = int(float(dato[col_cantidad].strip()))
						precio   = float(dato[col_precio].strip())
						precio = round(precio,1)
						if int(cantidad):

							# Guardamos los valores parseados en la lista temporal.
							#temp.append( codigo )
							#temp.append( producto )
							temp.append( cliente )
							#temp.append( cantidad )
							temp.append( precio )

							#for filas in temp:							
							#vuelta=vuelta+1
							#clientes=[]
							#precios=[]
							#if (cliente == filas[0]):
							#	precios=+filas[1]
							#	lista.append(( cliente,precio))
							#else:
							#	if (vuelta==1):
							#		cliente=filas[0]
							#		precio=(columnas[1])
							#	else:
							#		lista.append(( cliente,precio))
							#		clientes=filas[0]
							#		precios=filas[1]
							
							# Guardamos los datos de la lista temporal en la lista principal.
							
							lista.append(temp) 
									
							lista.sort(key=lambda precio:precio[1], reverse=True)

					else:
						# Si hay un codigo vacio, devolvemos error.
						error = "codigo"
	except:
		error = "archivo"

	return render_template('top_clientes.html', usuario=usuario, ventas=lista, error=error)

@app.errorhandler(404)
def error404(error):

	return render_template('error404.html'), 404


@app.errorhandler(500)
def error500(error):

	return render_template('error500.html'), 500



if __name__ == "__main__":
	app.run(debug=True)