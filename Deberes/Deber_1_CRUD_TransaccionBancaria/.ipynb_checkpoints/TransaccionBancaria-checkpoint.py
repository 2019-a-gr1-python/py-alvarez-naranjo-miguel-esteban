{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def crearUsuario(datosUsuario):\n",
    "    cabeceraUsuarios = [\"id\", \"nombre\", \"direccion\", \"telefono\", \"cedula\"]\n",
    "    UsuariosLista = []\n",
    "    datosLista = datosUsuario.split(',')\n",
    "    UsuariosLista.append(dict(zip(cabeceraUsuarios, datosLista)))\n",
    "    JSONusuario = json.dumps(UsuariosLista)\n",
    "    try:\n",
    "        path = './08_BDusuario.txt'\n",
    "        archivo_escritura_abierto = open(path,mode='w')\n",
    "        archivo_escritura_abierto.write(UsuariosLista) # Sobre escribe el contenido\n",
    "        \n",
    "    except:\n",
    "        print('Error leyendo archivo')\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def menu():\n",
    "\n",
    "    \"\"\"\n",
    "    Función que limpia la pantalla y muestra nuevamente el menu\n",
    "    \"\"\"\n",
    "\n",
    "    #os.system('clear') # NOTA para windows tienes que cambiar clear por cls\n",
    "    print (\"Bienvenido al Banco...\")\n",
    "    print (\"Selecciona una opción\")\n",
    "    print (\"\\t1 - Crear Nuevo Usuario\")\n",
    "    print (\"\\t2 - segunda opción\")\n",
    "    print (\"\\t3 - tercera opción\")\n",
    "    print (\"\\t9 - salir\")\n",
    "while True:\n",
    "\n",
    "    # Mostramos el menu\n",
    "    menu()\n",
    "    # solicituamos una opción al usuario\n",
    "\n",
    "    opcionMenu = input(\"Elija una opcion >> \")\n",
    "\n",
    "    if opcionMenu==\"1\":\n",
    "    \n",
    "        print (\"\\nlos datos deben estar separados por comas: id,nombre,direccion,numero de telefono,cedula\")\n",
    "        input(\"Ingrese los datos de un nuevo usuario: \")\n",
    "        crearUsuario(str(input))\n",
    "        \n",
    "    elif opcionMenu==\"2\":\n",
    "        print (\"\")\n",
    "        input(\"Has pulsado la opción 2...\\npulsa una tecla para continuar\")\n",
    "    elif opcionMenu==\"3\":\n",
    "        print (\"\")\n",
    "        input(\"Has pulsado la opción 3...\\npulsa una tecla para continuar\")\n",
    "    elif opcionMenu==\"9\":\n",
    "        break\n",
    "    else:\n",
    "        print (\"\")\n",
    "        input(\"No has pulsado ninguna opción correcta...\\npulsa una tecla para continuar\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
