#Segundo proyecto de taller de programacion. Laberinto
import tkinter as tk

global nombre_nivel #Str
global cant_max_mov #Int
global matriz #List
global modo_juego #str
global usuario #str
global nombre_usuario_global #str
nombre_nivel = ""
matriz = []
modo_juego = ""
nombre_usuario_global = ""
llaves_nivel = []
puertas_nivel = []
cant_max_mov = 0
cant_max_mov = 0
mov_restantes = cant_max_mov #Se le va a ir restando con cada movimiento valido
objetos = False #Luego se le cambia a un numero enterto
matriz_labels = []
patrulleros = []


#E: Recibe el nombre de archivo del nivel que se selecciono por el usuario
#S: Retorna una matriz interna que sera en la que se modificara todo
#R: Debe tener una matriz valida para poder ejecutarse 
def cargar_nivel(nombre_archi):
    global matriz
    global mov_restantes
    with open(nombre_archi, "r") as archivo_nivel:
        nivel = archivo_nivel.readline()
        separar = nivel.split(";")
        nombre_nivel = separar[0].strip()
        cant_max_mov = int(separar[1].strip()) #Para que sea un numero que se pueda restar
        if cant_max_mov <= 0:
            return False
        mov_restantes = cant_max_mov

        
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
        dibujar_matriz(matriz)
        info_matriz(nombre_archi)
        print(matriz)
    else:
        print("Matriz ingresada para dicho nivel es invalida, error")
        print(matriz)
    
    
    
    


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
    global objetos
    puerta_llave = []
    
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[0]):
            if i == 0 or i == len(m)-1 or j == 0 or j == len(m[0])-1:
                if m[i][j] != "#":
                    return False

            #patrulleros = [i, j, "direccion" {d,izq,ae,ab}]
            if m[i][j] == "<":
                patrulleros = patrulleros + [i, j, "d"]
                
            if m[i][j] == ">":
                patrulleros = patrulleros + [i, j, "izq"]
                
            if m[i][j] == "^":
                patrulleros = patrulleros + [i, j, "ar"]
                
            if m[i][j] == "v":
                patrulleros = patrulleros + [i, j, "ab"]
                
            if m[i][j] == "J":
                jugador += 1
                
            elif m[i][j] == "S":
                salida += 1

            elif m[i][j] == "*":
                objetos += 1

            elif m[i][j] != "." and m[i][j] != "#" and m[i][j] != "<" and m[i][j] != ">" and m[i][j] != "^" and m[i][j] != "v" and m[i][j] != "O":
                puerta_llave += m[i][j]
            #Podria ser una llave o puerta. Si hay puerta debe haber llave
            j += 1
        i += 1

    if jugador != 1 or salida != 1 or not objetos:
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
    global llaves_nivel 
    global puertas_nivel
    puertas_nivel = []
    llaves_nivel = []
    
    k = 0
    #Primero separa llaves de puertas
    while k < len(puertas) and puerta_llave != []:
        if puerta_llave[0] == puertas[k]:
            num = str(k + 1)
            puertas_nivel += [puerta_llave[0]] #
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
                llaves_nivel += dato
                puertas_encont = puertas_encont[1:]
                llaves_encont = llaves_encont[1:]
                
        i += 1
    if puertas_encont != [] or llaves_encont != []:
        puertas_nivel = ["Error, no hay llaves"]
        llaves_nivel = ["Error, no hay puertas"]
        return False
    
    return True 


#E: Recibe el nombre simbolico de la tecla que presionó el usuario
#S: Se dirige a validar dicho mivimiento que se intenta hacer
#R:
def validar_mov(event):
    listaa = abajo.winfo_children()
    for elemento in listaa:
        elemento.destroy()
        
    global matriz
    global mov_restantes
    
    fila = 0
    colum = 0
    nueva_fila = 0
    nueva_colum = 0
    
    texto_jug = tk.Label(abajo,
                         text= "Mover arriba: [ ↑ ]   Mover abajo: [ ↓ ]   Mover izquierda: Tecla [ ← ]   Mover derecha: Tecla [ → ]",
                         fg = "#FFD700",
                         bg = "#8B4513",
                         font = ("Arial",11)
                         )
    texto_jug.pack(expand = True)
    
    error = tk.Label(abajo,
                     text= "",
                     fg = "#FFD700",
                     font = ("Arial",11)
                     )
    error.pack(expand = True)
    
    for i, fila_matriz in enumerate(matriz):
        for j, celda in enumerate(fila_matriz):
            if celda == "J":
                fila = i
                colum = j
    
    #Para crear esta función si se busco en internet y se apoyo de la ia utilizandola como guia/tutor
    if event.keysym == "Up":
        nueva_fila = fila -1
        direccion = matriz[nueva_fila][colum]
        #No puede atravesar ni paredes ni puertas cerradas si aun no tiene su llave
        if direccion == "#":
            error.configure(text = "Movimiento invalido!, intentelo de nuevo",
                            bg = "#8B4513"
                            )
        else:
            error.configure(text = "",
                            bg = "#A0522D"
                            )
            mov_restantes -= 1
            matriz[fila][colum] = "."
            matriz[nueva_fila][colum] = "J"
            mover_jugador(matriz, fila, colum, nueva_fila, colum)
            mover_guardias(matriz)
        
    elif event.keysym == "Down":
        nueva_fila = fila +1
        direccion = matriz[nueva_fila][colum]
        if direccion == "#":
            error.configure(text = "Movimiento invalido!, intentelo de nuevo",
                            bg = "#8B4513"
                            )
        else:
            error.configure(text = "",
                            bg = "#A0522D"
                            )
            mov_restantes -= 1
            matriz[fila][colum] = "."
            matriz[nueva_fila][colum] = "J"
            mover_jugador(matriz, fila, colum, nueva_fila, colum)
            mover_guardias(matriz)
        
            
    elif event.keysym == "Left":
        nueva_colum = colum - 1
        direccion = matriz[fila][nueva_colum]
        if direccion == "#":
            error.configure(text = "Movimiento invalido!, intentelo de nuevo",
                            bg = "#8B4513"
                            )
        else:
            error.configure(text = "",
                            bg = "#A0522D"
                            )
            mov_restantes -= 1
            matriz[fila][colum] = "."
            matriz[fila][nueva_colum] = "J"
            mover_jugador(matriz, fila, colum, fila, nueva_colum)
            mover_guardias(matriz)
        
    elif event.keysym == "Right":
        nueva_colum = colum + 1
        direccion = matriz[fila][nueva_colum]
        if direccion == "#":
            error.configure(text = "Movimiento invalido!, intentelo de nuevo",
                            bg = "#8B4513"
                            )
        else:
            error.configure(text = "",
                            bg = "#A0522D"
                            )
            mov_restantes -= 1
            matriz[fila][colum] = "."
            matriz[fila][nueva_colum] = "J"
            mover_jugador(matriz, fila, colum, fila, nueva_colum)
            mover_guardias(matriz)
        

#E: Recibe la matriz del juego y las posiciones tanto actual del jugador, como de su destino
#S: La matriz de labels actualizada con la nueva posicion del jugador
#R: N/A
def mover_jugador(matriz, fila, colum, nueva_fila, nueva_colum):
    if mov_restantes <= 0:
        pantalla_derrota("no_mov")
        
    else:
        global matriz_labels
        matriz_labels[fila][colum].configure(text= ".",
                                             fg = "#EEDD82"
                                             )
        matriz_labels[nueva_fila][nueva_colum].configure(text= "J",
                                             fg = "#1E90FF"
                                             )
        #mov_restantes
        listaa = der.winfo_children()
        for elemento in listaa:
            if elemento == cont_mov:
                cont_mov.configure(text= "Movimientos restante: " + str(mov_restantes))
                cont_mov.pack(expand = True)
      


#E:
#S:
#R:
def mover_guardias(matriz):
    #patrulleros = [i, j, "direccion" {d,izq,ae,ab}]
    global patrulleros
    i = 0
    #Tanto patrullas como vigilantes
    #Verificar captura, ver si ya capturo al jugador y eso lleva a derrota

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

#E: Recibe el motivo de la derrota (Captura por patrulleros o falta de movimientos
#S: Muestra en la pantalla un mensaje de que perdio el juego y le da la opcion de ir al menu principal o volver a seleccionar el nivel
#R:
def pantalla_derrota(motivo):
    listaa = arriba.winfo_children()
    listaa += abajo.winfo_children()
    listaa += der.winfo_children()
    listaa += cen.winfo_children()
    for elemento in listaa:
        elemento.destroy()

    global nombre_usuario_global

    titulo = tk.Label(arriba,
                      text="Derrota en el laberinto!",
                      fg = "#DC143C",
                      font=("Arial", 19),
                      bg = "#87CEEB"
                      )
    titulo.pack(expand = True)

    if motivo == "no_mov":
        msj_perdio = tk.Label(cen,
                          text="Derrota! Te has quedado sin más movimientos",
                          fg = "#DC143C", #Color rojo tal vez 
                          font=("Arial", 12),
                          bg = "#F4A460"
                          )
        msj_perdio.pack(expand = True)
    else: #Vacio "" o "patrullero"/"vigilante"
        msj_perdio = tk.Label(cen,
                          text="Derrota! Fuiste capturado por los guardias",
                          fg = "#DC143C", #Color rojo tal vez 
                          font=("Arial", 12),
                          bg = "#F4A460"
                          )
        msj_perdio.pack(expand = True)

    volver = tk.Button(cen,
                       text="Volver a selección de nivel",
                       command=lambda : seleccionar_nivel(nombre_usuario_global)
                       )
    volver.pack(expand = True)

    regresar = tk.Button(cen,
                         text="Regresar al menu principal",
                         command=lambda : menu_principal()
                         )
    regresar.pack(expand = True)

    cerrar = tk.Button(cen,
                       text="Cerrar programa",
                       command =ventana.destroy
                       )
    cerrar.pack(expand = True)
  

#E:
#S:
#R:
def pantalla_victoria():
    #No solo debe llegar al final, sino haber obtenido los objetos del nivel
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
                      fg = "#B8860B",
                      font=("Arial", 18),
                      bg = "#87CEEB"
                      )
    titulo.pack(expand = True)
        
    i = 0
    #
    global matriz_labels
    matriz_labels = []
    while i < len(matriz):
        lista_labels = []
        j = 0
        while j < len(matriz[0]):
            color_bg = "#FFE4C4"
            if matriz[i][j] == "#":
                color_bg = "#2E8B57"
                color = "#FFE4C4"
                if i == 0 or i == len(matriz)-1 or j == 0 or j == len(matriz[0])-1:
                    color_bg = "#8B5A2B"
                    color = "#FFE4C4"
                #   #2E8B57
                #      "#555555" Gris #Verificar y probar colores. Quiero un tono cafe para los bloqueos. 
            elif matriz[i][j] == "J":
                color = "#1E90FF"
            elif matriz[i][j] == "S":
                color = "#32CD32"
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
                             bg = color_bg,
                             width=5,  #Para que sea cuadrada
                             height=2,
                             font = ("Arial",11)
                             )
            celda.grid(row=i, column=j, padx=2, pady=2)
            lista_labels += [celda]
            
            j += 1
        matriz_labels += [lista_labels]
        i += 1
        #cargar_nivel(nombre_archi)
        #nivel = tk.Button(der,
         #                 text= texto_boton[0],
         #                 command=lambda n=niveles[i]: print(n) #Luego ver más sobre esto
         #                 )
        #nivel.pack(pady = 10, padx = 20, expand = True)

         #De aqui tambien muestra la info del nivel al que accede
         #Y va a recibir la tecla del jugador que esta por moverse. Despues de moverse se actualiza la matriz


#E: Nombre del nivel actual para buscarlo en los ,txt
#S: Muestra la info del nivel actual
#R: N/A
def info_matriz(nombre_nivel):
    listaa = abajo.winfo_children()
    listaa += der.winfo_children()
    for elemento in listaa:
        elemento.destroy()
        
    global nombre_usuario_global
    global mov_restantes 
    global llaves_nivel 
    global puertas_nivel  
    global objetos
    global cont_mov 

    volver = tk.Button(arriba,
                       text="Volver",
                       command=lambda : seleccionar_nivel(nombre_usuario_global)
                       )
    volver.pack(side = "right", expand = True)
    
    nombre = tk.Label(arriba,
                      text= nombre_usuario_global.title(),
                      fg = "#B8860B",
                      bg = "#87CEEB",
                      font = ("Arial",14)
                      )
    nombre.pack()
    with open(nombre_nivel, "r") as info_nivel:
        nombre_mov = info_nivel.readline()
    name_nivel = nombre_mov.strip().split(";") #Ej. ["Desierto","45"]

    nivel_name = tk.Label(der,
                          text= "Nombre del nivel: " + name_nivel[0],
                          fg = "#FFFACD",
                          bg = "#A0522D"
                          )
    nivel_name.pack(expand = True)
    #" Cantidad maxima de movimientos: " + name_nivel[1]
    nivel_max_mov = tk.Label(der,
                          text= "Cantidad maxima movimientos: " + name_nivel[1],
                          fg = "#FFFACD",
                          bg = "#A0522D"
                          )
    nivel_max_mov.pack(expand = True)

        #-------------------- Arreglar --------------------#
    #cont_mov = tk.Label(der)

    cont_mov = tk.Label(der,#Arreglar esto porque siempre dice la misma cant 
                          text= "Movimientos restante: " + str(mov_restantes),
                          fg = "#FFFACD",
                          bg = "#A0522D"
                          )
    cont_mov.pack(expand = True)

         #-------------------- Arreglar --------------------#

    llaves_msj = tk.Label(der,
                          text= "Llaves en el nivel: ",
                          fg = "#FFFACD",
                          bg = "#A0522D"
                          )
    llaves_msj.pack(expand = True)

    for elem in llaves_nivel:
        llaves_dato = tk.Label(der,
                               text= str(elem),
                               fg = "#FFFACD",
                               bg = "#A0522D"
                               )
        llaves_dato.pack(expand = True)
        
    puertas_msj = tk.Label(der,
                           text= "Puertas en el nivel: ",
                           fg = "#FFFACD",
                           bg = "#A0522D"
                           )
    puertas_msj.pack(expand = True)

    for elem in puertas_nivel:
        puertas_dato = tk.Label(der,
                                text= str(elem),
                                fg = "#FFFACD",
                                bg = "#A0522D"
                                )
        puertas_dato.pack(expand = True)

    #Reiniciar estas variables en su respectivo lugar antes de guardar algo ya que sino, muestra info del nivel anterior al que se agcedio
        # (Ej: de si estaba en nivel 2 y luego va a nivel 1. Se quedan aqui las puertas y llaves de nivel 2 y se juntan con las de 1


   

    objetos_dis = tk.Label(der,
                        text= "Objetos disponibles en el nivel: " + str(objetos),
                        fg = "#FFFACD",
                        bg = "#A0522D"
                        )
    objetos_dis.pack(expand = True)

    texto_jug = tk.Label(abajo,
                         text= "Mover arriba: [ ↑ ]   Mover abajo: [ ↓ ]   Mover izquierda: Tecla [ ← ]   Mover derecha: Tecla [ → ]",
                         fg = "#FFD700",
                         bg = "#8B4513",
                         font = ("Arial",11)
                         )
    texto_jug.pack(expand = True)

    
    #Frame der
    # Nombre del nivel, Movimientos restantes (ej: "15 / 45")
    #Objetos recogidos, Llaves en poder, Puertas abiertas.

    #nombre_usuario_global = ""
    #mov_restantes = 0
    #cant_max_mov = 0 #No lo utilizamos
    #llaves_nivel = [] str
    #puertas_nivel = []     Se debe hacer otra variable de estos para colocar los que faltan/los que ya se tienen
    #cont_puertas = 0      cont_llaves = 0      cont_objetos = 0  crear variables
    #objetos = 0 =  Ej: 0/2
    #Frame abajo
    #Mover izquierda: Tecla [ ← ] | Mover derecha: Tecla [ → ]

    
    

#E:
#S:
#R:
def actualizar_matriz(matriz):
    i = 0
    #cargar_nivel(nombre_archi)

#E:
#S:
#R:
def actualizar_info(matriz):
    i = 0
  



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
                      fg = "#B8860B",
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

    #--------------------Arreglar----------------------------------
    #Muestra tantas veces el texto en la parte superior como nombres invalidos

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
    #--------------------Arreglar----------------------------------
    #No muestra el texto
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
        #nombre_nivel
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

    marca = tk.Label(cen,
                     text="Nivel:    Mejores marcas:    Jugador: ",
                     )
    
    marca.pack()

    #Funcion que revise marcas.txt y que por cada nivel muestre toda la info
    with open("marcas.txt","r") as texto_marcas:
        todo_ranking = texto_marcas.readlines()
    for linea in todo_ranking:
        if linea.strip() != "":
            linea = linea.strip().split(";")
            pos_num = len(linea[0])-1
            ranking = tk.Label(cen,
                               text= "Nivel " + linea[0][pos_num] + " \t    " + linea[1] + "\t" + linea[2]
                               )
            ranking.pack()
            #La primera palabra queda "nivel3" por lo cual se toma solo el ultimo digito para que visualmente se vea bien
            
        

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
#ventana.resizable(False, False)



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
ventana.bind("<Up>", validar_mov)
ventana.bind("<Down>", validar_mov)
ventana.bind("<Left>", validar_mov)
ventana.bind("<Right>", validar_mov)

ventana.mainloop()




