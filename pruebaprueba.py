rchivo ordenado por cliente

for filas in temp:
	lineaNum=lineaNum+1
	if (cliente == filas[0]):
		precios=+filas[1]
		clientes=clienteCantidad+1
		lista.append(( cliente,clienteMonto,))
	else:
		if (lineaNum==1):
			clienteNombre=columnas[0]
			clienteCantidad=1
			clienteMonto=(columnas[1])
		else:
			lista.append(( clienteNombre,clienteMonto,2))
			clienteNombre=columnas[0]
			clienteMonto=columnas[1]
			clienteCantidad=1
	
		
				# ordena el resultado por MONTO descendente
lista.sort( key=lambda cliente:cliente[1], reverse=True)
print(lista)