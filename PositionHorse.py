import re
def ParoImpar(a):
    b=2
    while a>=b:
        a=a-b
    return a
def NumfAInd(PosF):
    PosF=(8-PosF)
    PosF=str(PosF)
    return PosF
def NumcAInd(PosC):
    if PosC==0:
        PosC="A"
    elif PosC==1:
        PosC="B"
    elif PosC==2:
        PosC="C"
    elif PosC==3:
        PosC="D"
    elif PosC==4:
        PosC="E"
    elif PosC==5:
        PosC="F"
    elif PosC==6:
        PosC="G"
    elif PosC==7:
        PosC="H"
    else:
        PosC="coordenada mala"
    return PosC

def IndANumF(posicionInd):
    Fila=int(posicionInd[1])
    return Fila


def IndANumC(posicionInd):
    colum=posicionInd[0]
    if colum=="A" or colum=="a":
        colum=0
    elif colum=="B" or colum=="b":
        colum=1
    elif colum=="C" or colum=="c":
        colum=2
    elif colum=="D" or colum=="d":
        colum=3
    elif colum=="E" or colum=="e":
        colum=4
    elif colum=="F" or colum=="f":
        colum=5
    elif colum=="G" or colum=="g":
        colum=6
    elif colum== "H" or colum=="h":
        colum=7
    else:
        print("coordenada no valida")
    return colum
#Mostrar Ubicacion ingresada
TamañoMatriz=8
bloques=TamañoMatriz^2
Temp=bloques

posicionInd=input("Ingrese la posicion del caballo: ")
NumFila=IndANumF(posicionInd) #COLUMNA_NUMEROS
NumColum=IndANumC(posicionInd) #COLUMNA_LETRAS
NumFila=TamañoMatriz-NumFila
#Mostrar coordenadas para sistema
if (NumFila>-1 and NumFila<8) and (NumColum>-1 and NumColum<8):
    print("Fila ", NumFila)
    print("Columna ", NumColum)
    Posicion = (NumFila * TamañoMatriz) + (NumColum + 1)
    print("Numero de bloque ", Posicion)

    print("")
    CantFilas = 8
    ContBloque = 1
    contF = 8
    mas = 0
    convuelta = 0
    #Tablero con ubicacion Ingresada
    print("Su caballo esta aqui: ", posicionInd)
    print("  ╔═══════════════════════════════════════════╗")
    print("  ║       A   B   C   D   E   F   G   H       ║")
    print("  ║     _________________________________     ║")

    while CantFilas > 0:
        BloqueXFila = 0
        if convuelta > 0:
            a = float(convuelta)
            if ParoImpar(a) == 0:
                mas = 0
            elif ParoImpar(a) != 0:
                mas = 1
        while BloqueXFila <= 8:
            if BloqueXFila == 0:
                print("  ║ ", contF, " ", end="")
                contF = contF - 1
            else:
                if ContBloque == Posicion:
                    a = float(ContBloque + mas)
                    if ParoImpar(a) == 0:
                        print("|ꞈ♘█", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a) != 0:
                        print("| ♘ꞈ", end="")
                        ContBloque = ContBloque + 1
                else:
                    a = float(ContBloque + mas)
                    if ParoImpar(a) == 0:
                        print("|███", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a) != 0:
                        print("|   ", end="")
                        ContBloque = ContBloque + 1
            if BloqueXFila == 8:
                print("|     ║ ")
            BloqueXFila = BloqueXFila + 1
        convuelta = convuelta + 1
        CantFilas = CantFilas - 1

    print("  ║     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯     ║")
    print("  ╚═══════════════════════════════════════════╝")
    print("")
    #posiciones de movimiento
    posicion1=0
    posicion2=0
    posicion3=0
    posicion4=0
    posicion5=0
    posicion6=0
    posicion7=0
    posicion8=0
    #evaluar posiciones
    print("Las posiciones legales son: ",end="")
    posF1=NumFila-2
    posC1=NumColum-1
    if (posF1>-1 and posF1<8) and (posC1>-1 and posC1<8):
        PosF=posF1
        PosC=posC1
        posicion1=NumcAInd(PosC) + NumfAInd(PosF)
        print(posicion1,end=", ")
        posicion1=(posF1 * TamañoMatriz) + (posC1 + 1)

    posF2 = NumFila - 2
    posC2 = NumColum + 1
    if (posF2 > -1 and posF2 < 8) and (posC2 > -1 and posC2 < 8):
        PosF = posF2
        PosC = posC2
        posicion2 = NumcAInd(PosC) + NumfAInd(PosF)
        print(posicion2, end=", ")
        posicion2=(posF2 * TamañoMatriz) + (posC2 + 1)

    posF3 = NumFila - 1
    posC3 = NumColum + 2
    if (posF3 > -1 and posF3 < 8) and (posC3 > -1 and posC3 < 8):
        PosF = posF3
        PosC = posC3
        posicion3 = NumcAInd(PosC) + NumfAInd(PosF)
        print(posicion3, end=", ")
        posicion3 = (posF3 * TamañoMatriz) + (posC3 + 1)

    posF4 = NumFila + 1
    posC4 = NumColum + 2
    if (posF4 > -1 and posF4 < 8) and (posC4 > -1 and posC4 < 8):
        PosF = posF4
        PosC = posC4
        posicion4 = NumcAInd(PosC) + NumfAInd(PosF)
        print(posicion4, end=", ")
        posicion4 = (posF4 * TamañoMatriz) + (posC4 + 1)

    posF5 = NumFila + 2
    posC5 = NumColum + 1
    if (posF5 > -1 and posF5 < 8) and (posC5 > -1 and posC5 < 8):
        PosF = posF5
        PosC = posC5
        posicion5 = NumcAInd(PosC) + NumfAInd(PosF)
        print(posicion5, end=", ")
        posicion5 = (posF5 * TamañoMatriz) + (posC5 + 1)

    posF6 = NumFila + 2
    posC6 = NumColum - 1
    if (posF6 > -1 and posF6 < 8) and (posC6 > -1 and posC6 < 8):
        PosF = posF6
        PosC = posC6
        posicion6 = NumcAInd(PosC) + NumfAInd(PosF)
        print(posicion6, end=", ")
        posicion6 = (posF6 * TamañoMatriz) + (posC6 + 1)

    posF7 = NumFila + 1
    posC7 = NumColum - 2
    if (posF7 > -1 and posF7 < 8) and (posC7 > -1 and posC7 < 8):
        PosF = posF7
        PosC = posC7
        posicion7 = NumcAInd(PosC) + NumfAInd(PosF)
        print(posicion7, end=", ")
        posicion7 = (posF7 * TamañoMatriz) + (posC7 + 1)

    posF8 = NumFila - 1
    posC8 = NumColum - 2
    if (posF8 > -1 and posF8 < 8) and (posC8 > -1 and posC8 < 8):
        PosF = posF8
        PosC = posC8
        posicion8 = NumcAInd(PosC) + NumfAInd(PosF)
        print(posicion8, end=", ")
        posicion8 = (posF8 * TamañoMatriz) + (posC8 + 1)
    print("")

    #Tablero con posiciones Legales
    print("")
    CantFilas = 8
    ContBloque = 1
    contF = 8
    mas = 0
    convuelta = 0
    print("  ╔═══════════════════════════════════════════╗")
    print("  ║       A   B   C   D   E   F   G   H       ║")
    print("  ║     _________________________________     ║")

    while CantFilas > 0:
        BloqueXFila = 0
        if convuelta > 0:
            a = float(convuelta)
            if ParoImpar(a) == 0:
                mas = 0
            elif ParoImpar(a) != 0:
                mas = 1
        while BloqueXFila <= 8:
            if BloqueXFila == 0:
                print("  ║ ", contF, " ", end="")
                contF = contF - 1
            else:
                if ContBloque == Posicion:
                    a = float(ContBloque + mas)
                    if ParoImpar(a) == 0:
                        print("|ꞈ♘█", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a) != 0:
                        print("| ♘ꞈ", end="")
                        ContBloque = ContBloque + 1
                elif ContBloque==posicion1:
                    a=float(ContBloque+mas)
                    if ParoImpar(a)==0:
                        print("|█❶█", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a)!=0:
                        print("| ①ꞈ", end="")
                        ContBloque = ContBloque + 1
                elif ContBloque==posicion2:
                    a=float(ContBloque+mas)
                    if ParoImpar(a)==0:
                        print("|█❷█", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a)!=0:
                        print("| ②ꞈ", end="")
                        ContBloque = ContBloque + 1
                elif ContBloque==posicion3:
                    a=float(ContBloque+mas)
                    if ParoImpar(a)==0:
                        print("|█❸█", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a)!=0:
                        print("| ③ꞈ", end="")
                        ContBloque = ContBloque + 1
                elif ContBloque==posicion4:
                    a=float(ContBloque+mas)
                    if ParoImpar(a)==0:
                        print("|█❹█", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a)!=0:
                        print("| ④ꞈ", end="")
                        ContBloque = ContBloque + 1
                elif ContBloque==posicion5:
                    a=float(ContBloque+mas)
                    if ParoImpar(a)==0:
                        print("|█❺█", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a)!=0:
                        print("| ⑤ꞈ", end="")
                        ContBloque = ContBloque + 1
                elif ContBloque==posicion6:
                    a=float(ContBloque+mas)
                    if ParoImpar(a)==0:
                        print("|█❻█", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a)!=0:
                        print("| ⑥ꞈ", end="")
                        ContBloque = ContBloque + 1
                elif ContBloque==posicion7:
                    a=float(ContBloque+mas)
                    if ParoImpar(a)==0:
                        print("|█❼█", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a)!=0:
                        print("| ⑦ꞈ", end="")
                        ContBloque = ContBloque + 1
                elif ContBloque==posicion8:
                    a=float(ContBloque+mas)
                    if ParoImpar(a)==0:
                        print("|█❽█", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a)!=0:
                        print("| ⑧ꞈ", end="")
                        ContBloque = ContBloque + 1
                else:
                    a = float(ContBloque + mas)
                    if ParoImpar(a) == 0:
                        print("|███", end="")
                        ContBloque = ContBloque + 1
                    elif ParoImpar(a) != 0:
                        print("|   ", end="")
                        ContBloque = ContBloque + 1
            if BloqueXFila == 8:
                print("|     ║ ")
            BloqueXFila = BloqueXFila + 1
        convuelta = convuelta + 1
        CantFilas = CantFilas - 1

    print("  ║     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯     ║")
    print("  ╚═══════════════════════════════════════════╝")


