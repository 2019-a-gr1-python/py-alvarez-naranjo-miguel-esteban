import os

path = './BDusuario.txt'

def crearUsuario(datosUsuario):
        
    
    try:            
       
      archivo_escritura_abierto = open(path,mode='a')
      archivo_escritura_abierto.writelines(datosUsuario + '\n') # Sobre escribe el contenido
      archivo_escritura_abierto.close()
      print('\n\nUSUARIO CREADO CON EXITO\n')
    except:
      print('Error leyendo archivo')

def verListaUsuarios():
         
    try:   
      archivo_escritura_abierto = open(path,mode='r')
      for lines in archivo_escritura_abierto:
        print(lines)
      archivo_escritura_abierto.close()
      
    except:
      print('Error leyendo archivo')

def buscarUsuarioPorID(identificador):
     
    listaUsuarios = []
    try:   
      archivo_escritura_abierto = open(path,mode='r')
      for lines in archivo_escritura_abierto:
        listaUsuarios.append(lines)
      archivo_escritura_abierto.close()
      
    except:
      print('Error leyendo archivo')

    for x in listaUsuarios:
      y = x.split(',')
      if y[0] == identificador:
        return x

def buscarUsuarioPorNombre(nombre):
     
    listaUsuarios = []
    try:   
      archivo_escritura_abierto = open(path,mode='r')
      for lines in archivo_escritura_abierto:
        listaUsuarios.append(lines)
      archivo_escritura_abierto.close()
      
    except:
      print('Error leyendo archivo')

    for x in listaUsuarios:
      y = x.split(',')
      if y[1] == nombre:
        return x

def borrarUsuario(identificador):
    listaUsuarios = []
    elementoAEliminar = -1
    try:   
      archivo_escritura_abierto = open(path,mode='r')
      for lines in archivo_escritura_abierto:
        listaUsuarios.append(lines)
      archivo_escritura_abierto.close()
      
    except:
      print('Error leyendo archivo')

    for x in listaUsuarios:
      y = x.split(',')
      if y[0] == identificador:
        elementoAEliminar = int(listaUsuarios.index(x))        
        print ('Se elimino el usuario: ' + listaUsuarios.pop(elementoAEliminar))


    limpiarArchivo()
    llenarArchivo(listaUsuarios)
    
def actualizarUsuario(indice, nuevoDato):
    listaUsuarios = []
    elementoAActualizar = -1
    try:   
      archivo_escritura_abierto = open(path,mode='r')
      for lines in archivo_escritura_abierto:
        listaUsuarios.append(lines)
      archivo_escritura_abierto.close()
      
    except:
      print('Error leyendo archivo')

    for x in listaUsuarios:
      y = x.split(',')
      if y[0] == indice:
        elementoAActualizar = int(listaUsuarios.index(x))        
        listaUsuarios[elementoAActualizar] = nuevoDato+'\n'


    limpiarArchivo()
    llenarArchivo(listaUsuarios)    

    print('\n\nUSUARIO ACTUALIZADO\n')

def limpiarArchivo():
    try:   
        archivo_escritura_abierto = open(path,mode='w')
        archivo_escritura_abierto.write('')
        archivo_escritura_abierto.close()
        
    except:
       print('Error leyendo archivo')

def llenarArchivo(listaUser):
    try:   
      archivo_escritura_abierto = open(path,mode='a')
      for user in listaUser:
        archivo_escritura_abierto.writelines(user)
      archivo_escritura_abierto.close()
        
    except:
        print('Error leyendo archivo')


def menu():
    '''
    Función que limpia la pantalla y muestra nuevamente el menu
    '''
    #os.system('cls') # NOTA para windows tienes que cambiar clear por cls
    print ('Bienvenido al Banco...')
    print ('Selecciona una opción')
    print ('\t1 - Crear Nuevo Usuario')
    print ('\t2 - Ver Lista de Usuarios')
    print ('\t3 - Buscar Usuario por ID')
    print ('\t4 - Buscar Usuario por Nombre')
    print ('\t5 - Borrar Usuario')
    print ('\t6 - Actualizar Usuario')
    print ('\t9 - salir')


while True:

    # Mostramos el menu
    menu()
    # solicituamos una opción al usuario

    opcionMenu = input('Elija una opcion >> ')

    if opcionMenu=='1':
    
      print ('\nlos datos deben estar separados por comas: id,nombre,direccion,numero de telefono,cedula')
      datosIngresados = input('Ingrese los datos de un nuevo usuario: ')
      crearUsuario(str(datosIngresados))
        
    elif opcionMenu=='2':
      print('\n')
      verListaUsuarios()
      print('\n')
    elif opcionMenu=='3':
      print ('\nIngrese el ID del usuario que desea consultar')
      idABuscar = input('Ingrese el ID: ')
      print('\n')
      print (buscarUsuarioPorID(idABuscar))
      print('\n')
    elif opcionMenu=='4':
      print ('\nIngrese el Nombre del usuario que desea consultar')
      idABuscarNomb = input('Ingrese el Nombre: ')
      print('\n')
      print (buscarUsuarioPorNombre(idABuscarNomb))
      print('\n')
    elif opcionMenu=='5':
      print ('\nIngrese el ID del usuario que desea Borrar')
      idABuscarBorrar = input('Ingrese el ID: ')
      print('\n')
      borrarUsuario(idABuscarBorrar)
      print('\n')
    elif opcionMenu=='6':
      print ('\nActualizar Usuario')
      idActualizar = input('Ingrese el ID del usuario que requiera actualizar: ')
      print ('\nlos datos deben estar separados por comas: id,nombre,direccion,numero de telefono,cedula')
      nuevoDatoUsuario = input('Ingrese los nuevos datos del usuario a actualizar: ')
      print('\n')
      actualizarUsuario(idActualizar,nuevoDatoUsuario)
      print('\n')
    elif opcionMenu=='9':
      break
    else:
      print ('')
      input('No has pulsado ninguna opción correcta...\npulsa una tecla para continuar')