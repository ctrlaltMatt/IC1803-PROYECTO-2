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

ventana = tk.Tk()
ventana.title("Laberinto")
ventana.geometry("800x550")
ventana.config(padx=20 , pady=20)

tk.Label(ventana,
         text="Laberinto",
         font=("Arial", 12)
         ).pack()



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

izq = tk.Frame(ventana,
                  bg = "orange",
                  width= 200,
                  height=100,
                  )
izq.pack_propagate(False)
izq.pack(side="right", fill= "y")
#En el de la izq van los datos 


cen = tk.Frame(ventana,
                  bg = "yellow",
                  width= 200,
                  height=100,
                  )
cen.pack_propagate(False)
cen.pack(side = "left", expand=True, fill= "both")

#----------------------------------------------------------------------------------


ventana.mainloop()




