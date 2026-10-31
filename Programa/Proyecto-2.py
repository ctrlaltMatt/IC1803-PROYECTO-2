#Segundo proyecto de taller de programacion. Laberinto
import tkinter as tk

global nombre_nivel #Str
global cant_max_mov #Int
global matriz #List

#E: Recibe el nombre de archivo del nivel que se selecciono por el usuario
#S: Retorna una matriz interna que sera en la que se modificara todo
#R: Debe tener una matriz valida para poder ejecutarse 
def cargar_nivel(nombre_archi):
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
    


#E: recibe la matriz creada previamente y valida que exista todo lo necesario
#S: Retorna True si todo esta completo y False si falta algun elemento 
#R: N/A
def validar_matriz(m):
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
def validar_mov():
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


#E:
#S:
#R:
def dibujar_matriz():
    i = 0
    

#E:
#S:
#R:
def actualizar_matriz():
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
                      fg = "black",
                      font=("Arial", 16)
                      )
    titulo.pack(expand = True)
    #Botones del menu principal

    nueva = tk.Button(cen,
                      text="Iniciar nueva partida",
                      command=lambda : seleccionar_nivel()
                      )
    
    nueva.pack( expand = True)
    cargar = tk.Button(cen,
                       text="Continuar partida",
                       command=lambda : print("cargar")
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


#E:
#S:
#R:
def seleccionar_nivel():
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
                      fg = "black",
                      font=("Arial", 16)
                      )
    titulo.pack(expand = True)

    volver = tk.Button(arriba,
                      text="Volver",
                      command=lambda : menu_principal()
                      )
    
    volver.pack(side = "right", expand = True)

    #Llamar a una auxiliar que abra el .txt de cuantos niveles hay y imprima botones "Nivel i". 

    nivel1 = tk.Button(der,
                      text="Nivel 1",
                      command=lambda : print("Nivel 1")
                      )
    
    nivel1.pack(expand = True)
    info1 = tk.Label(cen,
                     text="Bodega abandonada. Limite movimientos: 45. Mejor marca: 36",
                     )
    
    info1.pack(expand = True)


    

    nivel2 = tk.Button(der,
                      text="Nivel 2",
                      command=lambda : print("Nivel 2")
                      )
    
    nivel2.pack(expand = True)
    info2 = tk.Label(cen,
                     text="Playa de dia. Limite movimientos: 38. Mejor marca: 26",
                     )
    
    info2.pack(expand = True)


    

    nivel3 = tk.Button(der,
                      text="Nivel 3",
                      command=lambda : print("Nivel 3")
                      )
    
    nivel3.pack(expand = True)
    info3 = tk.Label(cen,
                     text="Desierto. Limite movimientos: 50. Mejor marca: 42",
                     )
    
    info3.pack(expand = True)


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
                      fg = "black",
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



#------------- Frames para acomodar los labels de forma más facil y ordenada -------
arriba = tk.Frame(ventana,
                  bg = "gray",
                  width= 200,
                  height=100,
                  )
arriba.pack_propagate(False)
arriba.pack(side="top", fill = "x")

abajo = tk.Frame(ventana,
                  bg = "gray",
                  width= 200,
                  height=100,
                  )
abajo.pack_propagate(False)
abajo.pack(side="bottom", fill = "x")

der = tk.Frame(ventana,
                  bg = "orange",
                  width= 200,
                  height=100,
                  )
der.pack_propagate(False)
der.pack(side="right", fill= "y")
#En el de la izq van los datos 


cen = tk.Frame(ventana,
                  bg = "yellow",
                  width= 200,
                  height=100,
                  )
cen.pack_propagate(False)
cen.pack(side = "left", expand=True, fill= "both")

#----------------------------------------------------------------------------------


menu_principal()
ventana.mainloop()




