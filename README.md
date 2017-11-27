Farmasoft - Jonathan Walter Medina, Gabriel Emiliano Estrugo
Parcial Paradigma e la Programacion/ Estructura de Base de Datos 
2° Cuatrimestre Año 2017

Aplicacion:
La aplicacion consiste en un programa que dependiendo de la consulta muestra
una determinada informacion.
Fue programado en Python 3.6 usando a la vez el Framework de Python llamado Flask

Estructura:
Tomando como base de datos, poseemos archivos formato .csv. Que en conjunto con
con codigo de Python y Html se leera y renderizara en una pantalla atraves de un sistema

Modulos:
1- Index: Posee 2 opciones tanto para loguearse como para registrarse, junto a un mensaje
         debaje en el cual se da la bienvenida y los que han hecho el programa
2- Login: Un formulario compuesto por 2 campos. Uno de usuario y otro de contraseña, en el cual
         al ingresar los datos, este verificara que coincidan con los encontrados en el archivo
         csv. 
         De no existir en el archivo, se comunicara de que el usuario no existe o es incorrecto
	 De Existir, el usuario podra acceder al sistema  
3- Registro: En este, el usuario debera crear en los campos, los datos de usuario que quedaran
         grabados en un archivo .csv
         En de que no coincida la contraseñas para el registro, se mostrara el mensaje de que 
         no coinciden las contraseñas
         En caso de que si coincidan. Se redireccionara al Login.
4- Menu: Una ves logueado la persona lo primero que vera es este Menu junto al nombre Farmasoft
4.1-	Ultimas Ventas: Se llera un archivo csv que mostrara los ultimos registros de las ultimas 5 ventas. 
                       Si el archivo esta dañado, o no se lee correctamente o no existe, mostrara el mensaje de que la base
                       no existe
4.2-	Cliente x Producto: Consta de un Campo en donde el usuario podra buscar, colocando el nombre de un cliente, 
                       los productos que este a comprado. Ya que el campo se conectara con el archivo csv buscando las
                       coincidencias con la palabra buscada
                       Si el archivo esta dañado, no se lee correctamente o no existe, mostrara un mensaje de que la base
                       no existe
4.3- 	Producto x Cliente: Aqui el usuario podra buscar, segun el Producto, los clientes que han comprado el producto 
                       la pagina se conectara al archivo csv buscando las coincidencias con la palabra buscada
                       Si el archivo esta dañado, no se lee correctamente o no existe, mostrara un mensaje de que la base
                       no existe
4.4- 	Productos + Vendidos: La pagina se conecta con el archivo csv de ventas mostrando los productos que mas se vendieron
                       teniendo en cuenta la cantidad vendida de un determinado producto
4.5- 	Mejores Clientes: el archivo consulta al csv y se fija las coincidencias en un nombre para sumar los precios y detectar
                       cual es el cliente que mas a gastado en la empresa
4.6-	Cerrar Sesion: cierra la sesion de usuario y devuelve a index
5- Error 400: un archivo de error que en caso de no encontrarse una pagina o algun error, te da el aviso
6- Error 500: un archivo de error, que en caso de no detectar el server muestra un aviso