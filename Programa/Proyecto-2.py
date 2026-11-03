#Segundo proyecto de taller de programacion. Laberinto
import tkinter as tk

global nombre_nivel #Str
global cant_max_mov #Int
global matriz #List
global modo_juego #str
global usuario #str
nombre_nivel = ""
cant_max_mov = 0
matriz = []
modo_juego = ""
nombre_usuario_global = ""

#E: Recibe el nombre de archivo del nivel que se selecciono por el usuario
#S: Retorna una matriz interna que sera en la que se modificara todo
#R: Debe tener una matriz valida para poder ejecutarse 
def cargar_nivel(nombre_archi):
    global matriz
    with open(nombre_archi, "r") as archivo_nivel:
        nivel = archivo_nivel.readline()
        separar = nivel.split(";")
        nombre_nivel = separar[0].strip()
        cant_max_mov = int(separar[1].strip()) #Para que sea un numero que se pueda restar
        if cant_max_mov <= 0:
            return False 

        
        dato = archivo_nivel.readline().strip()
        matriz = []
        while dato != "":
        #Crear matriz en base al txt
            fila = []
            while dato != "":
                fila += [dato[0]]
                dato = dato[1:]
            matriz += [fila]
            dato = archivo_nivel.readline().strip()

        #validarla, bordes con #, solo un J y un S y al menos un *
    if validar_matriz(matriz):
        print("Matriz valida") #Luego eliminar esto
    print(matriz)
    dibujar_matriz(matriz)
    


#E: recibe la matriz creada previamente y valida que exista todo lo necesario
#S: Retorna True si todo esta completo y False si falta algun elemento 
#R: N/A
def validar_matriz(m):
    global matriz 
    if not isinstance(m, list) or m == []:
        return False
    #Para validar que sea rectangular 
    for fila in m:
        if len(fila) != len(m[0]):
            return False
    
    jugador = 0
    salida = 0 #Solo debe haber 1
    objeto = False
    puerta_llave = []
    
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[0]):
            if i == 0 or i == len(m)-1 or j == 0 or j == len(m[0])-1:
                if m[i][j] != "#":
                    return False
            if m[i][j] == "J":
                jugador += 1
                
            elif m[i][j] == "S":
                salida += 1

            elif m[i][j] == "*":
                objeto += 1

            elif m[i][j] != "." and m[i][j] != "#" and m[i][j] != "<" and m[i][j] != ">" and m[i][j] != "^" and m[i][j] != "v" and m[i][j] != "O":
                puerta_llave += m[i][j]
            #Podria ser una llave o puerta. Si hay puerta debe haber llave
            j += 1
        i += 1

    if jugador != 1 or salida != 1 or not objeto:
        return False

    if not validar_llaves(puerta_llave):
        return False
    
    return True


#E: Recibe una lista que contiene tanto los simbolos de llaves como de puertas y los valida
#S: Retorna False si el dato que se encuentra en dicha lista no es una llave ni una puerta, o si no corresponde con ninguno
    #Ej: Si hay una puerta sin llave. Retorna True si existe la llave y su puerta y no se repite
#R: N/A
def validar_llaves(puerta_llave):
    puertas = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    llaves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    llaves_encont = []
    puertas_encont = []
    
    k = 0
    #Primero separa llaves de puertas
    while k < len(puertas) and puerta_llave != []:
        if puerta_llave[0] == puertas[k]:
            num = str(k + 1)
            puertas_encont += [num]
            k = 0
            puerta_llave = puerta_llave[1:]

        elif puerta_llave[0] == llaves[k]:
            llaves_encont += [puerta_llave[0]]
            k = 0
            puerta_llave = puerta_llave[1:]
            
        else:
            k += 1
        
    if puerta_llave != []:
        return False

    #Luego busca coincidencias.
    i = 0
    while i < len(puertas_encont):
        cmp = puertas_encont[i]
        for dato in llaves_encont:
            if cmp == dato:
                i -= 1
                puertas_encont = puertas_encont[1:]
                llaves_encont = llaves_encont[1:]
                
        i += 1
    if puertas_encont != [] or llaves_encont != []:
        return False
    
    return True 




#E:
#S:
#R:
def mover_jugador(matriz, direccion):
    i = 0

#E:
#S:
#R:
def validar_mov(mov):
    i = 0


#E:
#S:
#R:
def mover_guardias(matriz):
    i = 0

#E:
#S:
#R:
def patrullas():
    i = 0

#E:
#S:
#R:
def vigilante():
    i = 0

#E:
#S:
#R:
def verificar_captura():
    i = 0


#E: Recibe la matriz ya lista
#S: Muestra una lista de labels donde cada uno contiene 1 caracter representante de la matriz
#R: N/A
def dibujar_matriz(matriz):
    listaa = arriba.winfo_children()
    listaa += abajo.winfo_children()
    listaa += der.winfo_children()
    listaa += cen.winfo_children()
    for elemento in listaa:
        elemento.destroy()

    titulo = tk.Label(arriba,
                      text="Laberinto",
                      fg = "#FFD700",
                      font=("Arial", 18),
                      bg = "#87CEEB"
                      )
    titulo.pack(expand = True)
    volver = tk.Button(arriba,
                       text="Volver",
                       command=lambda : menu_principal()
                       )
    volver.pack(side = "right", expand = True)
    
        
    i = 0
    lista_labels = []
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            if matriz[i][j] == "#":
                color = "#708090"
            elif matriz[i][j] == "J":
                color = "#1E90FF"
            elif matriz[i][j] == "S":
                color = "#2E8B57"
            elif matriz[i][j] == "*":
                color = "#FFD700"
            elif matriz[i][j] == ".":
                color = "#EEDD82"
            else:
                color = "#DC143C"
                #Arena
            #Dependiendo de lo que hay en la posicion el fg o bg es diferente
            celda = tk.Label(cen,
                             text= matriz[i][j],
                             fg = color,
                             bg = "#FFE4C4",
                             width=5,  #Para que sea cuadrada
                             height=2,
                             font = ("Arial",11)
                             )
            celda.grid(row=i, column=j, padx=2, pady=2)
            lista_labels += [celda]
            
            j += 1
        i += 1
        #cargar_nivel(nombre_archi)
        #nivel = tk.Button(der,
         #                 text= texto_boton[0],
         #                 command=lambda n=niveles[i]: print(n) #Luego ver más sobre esto
         #                 )
        #nivel.pack(pady = 10, padx = 20, expand = True)
    
    

#E:
#S:
#R:
def actualizar_matriz(matriz):
    i = 0
    #cargar_nivel(nombre_archi)

#E:
#S:
#R:
#def

#------------------------Interfaz grafica -------------------------------------#

#E: Vacio
#S: Limpia todos los frames antes de crar los nuevos correspondientes al menu principal
#R:N/A
def menu_principal():
    #Primero limpiar todos los frames, incluso si no los vamos a utilizar, solo se deja el boton de "salir/volver"
    listaa = arriba.winfo_children()
    listaa += abajo.winfo_children()
    listaa += der.winfo_children()
    listaa += cen.winfo_children()
    #Limpiar todos los frames(Areas separadas donde se encuentran determinados botones o labels)
    for elemento in listaa:
        elemento.destroy()

    titulo = tk.Label(arriba,
                      text="Laberinto",
                      fg = "#FFD700",
                      font=("Arial", 18),
                      bg = "#87CEEB"
                      )
    titulo.pack(expand = True)
    #Botones del menu principal

    nueva = tk.Button(cen,
                      text="Iniciar nueva partida",
                      command=lambda : escribir_usuario("iniciar")
                      )
    
    nueva.pack( expand = True)
    cargar = tk.Button(cen,
                       text="Continuar partida",
                       command=lambda : escribir_usuario("cargar")
                       )
    cargar.pack( expand = True)
    consultar = tk.Button(cen,
                          text="Mejores marcas",
                          command=lambda : mejores_marcas()
                          )
    consultar.pack( expand = True)
    salir = tk.Button(cen,
                      text="Salir",
                      command=ventana.destroy
                      )
    salir.pack( expand = True)



#E: Modo de juego para luego de obtener el texto saber a donde dirigirse
#S: Muestra una nueva pantalla en la que el usuario debe ingresar su nombre para poder cargar la partida o empezar una nueva
#R: N/A
def escribir_usuario(modo):
    listaa = arriba.winfo_children()
    listaa += abajo.winfo_children()
    listaa += der.winfo_children()
    listaa += cen.winfo_children()
    for elemento in listaa:
        elemento.destroy()

    global modo_juego
    modo_juego = modo
    #-------------------------------------
        #Volver
        #Primero label que pide nombre
        #Espacio
        #Boton

    volver = tk.Button(arriba,
                       text="Volver",
                       command=lambda : menu_principal()
                       )
    volver.pack(side = "right", expand = True)

    solicitud = tk.Label(cen,
                         text="Por favor ingrese su nombre de usuario",
                         fg = "black",
                         font=("Arial", 12)
                         )
    solicitud.pack(side = "top")
        
    nombre_usuario = tk.Entry(cen)
    nombre_usuario.pack()

    enviar = tk.Button(cen,
                       text="Enviar",
                       command = lambda : accion_del_boton(nombre_usuario, modo_juego)
                       )
    enviar.pack()

#E: Recibe el nombre de la variable utilizada en el entry para poder hacer la funcion get() y el modo de juego en el que se encuentra actualmente
#S: Una vez se toma el valor que el usuario ingreso se lleva a una validacion dependiendo de su modo de juego
#R: N/A
def accion_del_boton(entrada, modo):
    #Funcion creada con apoyo/guia de la ia 
    global nombre_usuario_global  
    nombre_usuario_global = entrada.get() #capturar el texto
    

    if modo == "iniciar":
        validar_usuario_inicio(nombre_usuario_global)

    else:
        validar_usuario_cargar(nombre_usuario_global)
        
#E: Vacio
#S: retorna un mensaje de eror si encuentra alguna coincidencia con progreso.txt y guarda el nuevo nombre de usuario si no encuentra coincidencias. 
#R: Debe ser un nombre de un usuario, no vacio ni numeros
def validar_usuario_inicio(user):
    encontrado = False
    error = tk.Label(arriba,
                     text="",
                     )
    error.pack(side = "top", expand = True)

        #Se compara con los elementos de progreso.txt
    if user.strip() == "":
        error.config(text="Error, nombre debe ser diferente de vacio o un numero",
                     fg = "red"
                     )
        return
    try:
        numero_ent = int(user)
        error.configure(text="Error, nombre debe ser diferente de vacio o un numero",
                        fg = "red"
                        )
        return
    except:
        pass
        
    with open("progreso.txt", "r") as nombre_usuarios:
        todo = nombre_usuarios.readlines()

    i = 0
    while i < len(todo):
        usuario = todo[i].strip().split(";")
        if usuario[0].title() == user.title():
            #print("Hay una coincidencia! Intenta otro nombre para iniciar la partida!")
            error.configure(text = "Ese nombre de usuario ya existe! Intenta uno nuevo para iniciar la partida!",
                         fg = "#1E90FF",
                         font = ("Arial",11)
                         )
            error.pack()
            encontrado = True
        i += 1
        
    if not encontrado:
        print("No hay coincidencias. Puedes crear el usuario!!!")
        error.configure(text = "Creando nuevo nombre de usuario!",
                     fg = "blue",
                     font = ("Arial",11)
                     )
        error.pack()
        crear_usuario(user)
        seleccionar_nivel(user)
        #Se debe de agregar al .txt de progreso y agregar validacion por si no existe progreso.txt
        #O ir a cargar_partida()
#E: Vacio
#S: retorna un mensaje de eror si no encuentra alguna coincidencia con progreso.txt
#R: Debe ser un nombre de un usuario, no vacio ni numeros
def validar_usuario_cargar(user):
    encontrado = False
    error = tk.Label(arriba,
                     text="",
                     )
    error.pack(side = "top", expand = True)

        #Se compara con los elementos de progreso.txt
    if user.strip() == "":
        error.config(text="Error, nombre debe ser diferente de vacio o un numero",
                     fg = "red"
                     )
        return
    try:
        numero_ent = int(user)
        error.configure(text="Error, nombre debe ser diferente de vacio o un numero",
                        fg = "red"
                        )
        return
    except:
        pass
        
    with open("progreso.txt", "r") as nombre_usuarios:
        todo = nombre_usuarios.readlines()

    i = 0
    while i < len(todo):
        usuario = todo[i].strip().split(";")
        if usuario[0].title() == user.title():
            error.configure(text = "Nombre de usuario valido! Cargando la partida!",
                         fg = "#1E90FF",
                         font = ("Arial",11)
                         )
            error.pack()
            encontrado = True
        i += 1
        
    if encontrado:
        print("Hay coincidencias.Cargando su partida!!")
        error.configure(text = "Cargando su partida!",
                     fg = "blue",
                     font = ("Arial",11)
                     )
        error.pack()
        seleccionar_nivel(user)
        #O ir a cargar_partida()
    

#E: Recibe el nombre del usuario
#S: Se añade el nombre de usuario a progreso.txt y se le asigna el nivel 1 por default
#R: N/A
def crear_usuario(nombre):
    with open("progreso.txt", "a") as usuarios:
        nombre_formado = [nombre + ";1\n"]
        usuarios.writelines(nombre_formado)

#E: Recibe el nombre del usuario actual que esta jugando y nivel que acaba de superar 
#S: Reemplaza el simbolo del nivel anterior por el más reciente desbloqueado
#R: N/A
def actualizar_progreso(user_name, nivel):
    #Un ciclo while para que no cambie su posicion, solo su dato a modificar
    with open("progreso.txt", "r") as todos_usuarios:
        jugadores = todos_usuarios.readlines()

    with open("progreso.txt", "w") as todos_usuarios:
        save_jugador = []
        i = 0
        while jugadores != []:
            jugador = jugadores[i].strip().split(";")
            if jugador[0].title() == user_name.title():
                #jugador[1] = [";" + nivel + "\n"]
                save_jugador += [user_name.title + ";" + nivel + "\n"]
             
            else:
                save_jugador += jugador

            i += 1
            jugadores = jugadores[1:]
        
        todos_usuarios.writelines(save_jugador)



#-------------------------------------------------------
#E:
#S:
#R:
def mostrar_panel_info(nombre_nivel, mov_restantes, mov_max, objetos_recogidos, objetos_total, llaves, puertas):
    i = 0
#-------------------------------------------------------




#E: Recibe el nombre del jugador actual ya que sera necesario para una futura funcion
#S: Limpia los frames y muestra el titulo del juego junto al boton para regresar al menu inicial y al final va a la funcion de mostrar niveles
#R: N/A
def seleccionar_nivel(jugador):
    #Debe pedir que ingrese un nombre de usuario para continuar
    #Este crea un .txt (o lo añade a uno) donde se coloca el nombre junto a algun simbolo de la cantidad de niveles superado
    #Depediendo de ese .txt desbloquea los niveles
    
        #---------------------
    #Se necesita una funcion para leer, agregar/crear .txt con esa informacion y que de ahi vaya a niveles
    #Asi se puede reutilizar esta para iniciar nueva partida y cargar una. Ambas piden nombre del usuario
         #-------------------
    listaa = arriba.winfo_children()
    listaa += abajo.winfo_children()
    listaa += der.winfo_children()
    listaa += cen.winfo_children()
    for elemento in listaa:
        elemento.destroy()

    titulo = tk.Label(arriba,
                      text="Laberinto",
                      fg = "#FFD700",
                      font=("Arial", 18),
                      bg = "#87CEEB"
                      )
    titulo.pack(expand = True)

    volver = tk.Button(arriba,
                       text="Volver",
                       command=lambda : menu_principal()
                       )
    volver.pack(side = "right", expand = True)

    #Llamar a una auxiliar que abra el .txt de cuantos niveles hay y imprima botones "Nivel i".
    mostrar_niveles(jugador)



#E: El nombre del usuario
#S: Muestra los niveles disponibles 
#R: N/A
def mostrar_niveles(user_name):
    #niveles_existentes.txt
    #Crear otro .txt que diga cuales son los niveles que existen y como se llaman para que la funcion los pueda buscar y mostrar su titulo y
        #cantidad maxima de movimeintos. Tambien el numero que los representa para asi poder saber si ese nivele sta desbloqueado apra el usuario
#---------------------------------------
    #Abrir niveles_existentes.txt
    #Abrir cada nivel para obtener los datos 0 y 1 de su primera linea (Nombre y cant max mov
    #Para colocar todos los botones y labels segun esto mismo.
    #Se busca al usuario y se ve hasta que nivel está, si es menor que la cantidad total de botones estos se bloquean
    
#--------------------------------------
    with open("niveles_existentes.txt", "r") as todos_niveles:
        niveles = todos_niveles.readlines()
        #Validar tambien si hay algun salto o vacio

    with open("marcas.txt", "r") as marca:
        mejores = marca.readlines()
        
    i = 0
    lista_botones = []
    while i < len(niveles):
        if i >= len(mejores):
            mejor_marca = ["","",""]
        else:
            mejor_marca = mejores[i].strip().split(";")
        
        with open(niveles[i].strip(), "r") as info_nivel:
            nivel_comp = info_nivel.readline()
        primera_linea = nivel_comp.strip().split(";")
        texto_boton = niveles[i].split(".")
        nivel = tk.Button(der,
                          text= texto_boton[0],
                          command=lambda n=niveles[i]: cargar_nivel(n.strip()) #Luego ver más sobre esto
                          )
        nivel.pack(pady = 10, padx = 20, expand = True)
        #cargar_nivel(nombre_archi)
        #nivel = tk.Button(der,
         #                 text= texto_boton[0],
         #                 command=lambda n=niveles[i]: print(n) #Luego ver más sobre esto
         #                 )
        #nivel.pack(pady = 10, padx = 20, expand = True)
        
        lista_botones += [nivel]
        info = tk.Label(cen,
                        text=primera_linea[0] + " Limite movimientos:  " + primera_linea[1] + " Mejor marca:  " + mejor_marca[1] + " por:  " + mejor_marca[2],
                        fg = "#3E2723"
                        )
        info.pack(pady = 10, padx = 20, expand = True)
        
        i += 1

    #user_name
    nivel_desblo = "1"
    with open("progreso.txt", "r") as progreso:
        info_user = progreso.readlines()
        for elemento in info_user:
            separar = elemento.strip().split(";")
            if separar[0].title() == user_name.title():
                nivel_desblo = separar[1]
        
    i = 0
    #nivel_desblo
    while i < len(niveles):
        nivel_actual = i+1
        if nivel_actual <= int(nivel_desblo):
            lista_botones[i].configure(state = "normal",
                                       bg = "#DC143C",
                                       fg = "#FFFFFF")
        else:
            lista_botones[i].configure(state = "disabled",
                                       bg = "#708090",
                                       fg = "#FFFFFF"
                                       )
            
        i += 1


    



#E: Vacio
#S: Muestra una lista con el nombre del nivel, la cantidad minima de movimientos con la que se superó y el jugador que lo supero
#R: N/A
def mejores_marcas():
    listaa = arriba.winfo_children()
    listaa += abajo.winfo_children()
    listaa += der.winfo_children()
    listaa += cen.winfo_children()
    for elemento in listaa:
        elemento.destroy()
        
    #Funcion que revise marcas.txt y que por cada nivel muestre toda la info
    ranking = tk.Label(der,
                      text= "Nivel 3",
                      )
    
    ranking.pack(expand = True)
    marca = tk.Label(cen,
                     text="Nivel:  \t  Mejores marcas:  \t  Jugador: ",
                     )
    
    marca.pack(expand = True)

    #Aqui va la auxiliar que muestra lo que esta en el .txt

    titulo = tk.Label(arriba,
                      text="Mejores marcas",
                      fg = "#3E2723",
                      font=("Arial", 16)
                      )
    titulo.pack(expand = True)

    volver = tk.Button(arriba,
                      text="Volver",
                      command=lambda : menu_principal()
                      )
    
    volver.pack(side = "right", expand = True)

             
    

    

ventana = tk.Tk()
ventana.title("Laberinto")
ventana.geometry("800x550")
ventana.config(padx=20 , pady=20)
ventana.resizable(False, False)



#------------- Frames para acomodar los labels de forma más facil y ordenada -------
arriba = tk.Frame(ventana,
                  bg = "#87CEEB",
                  width= 200,
                  height=100,
                  )
arriba.pack_propagate(False)
arriba.pack(side="top", fill = "x")

abajo = tk.Frame(ventana,
                  bg = "#A0522D",
                  width= 200,
                  height=100,
                  )
abajo.pack_propagate(False)
abajo.pack(side="bottom", fill = "x")

der = tk.Frame(ventana,
                  bg = "#DEB887",
                  width= 200,
                  height=100,
                  )
der.pack_propagate(False)
der.pack(side="right", fill= "y")
#En el de la izq van los datos 


cen = tk.Frame(ventana,
                  bg = "#F4A460",
                  width= 200,
                  height=100,
                  )
cen.pack_propagate(False)
cen.pack(side = "left", expand=True, fill= "both")

#----------------------------------------------------------------------------------


menu_principal()
ventana.mainloop()




