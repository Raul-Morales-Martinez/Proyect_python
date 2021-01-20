#1Tamaño
def big(x):
    for z in range(len(x)):
        if x[z] > 0:
            x[z] ="big"
    print(x)
    return x
big([-1,5,-2,3])

#2 Contar positivos

def contpostive(x):
    cont = 0
    for z in range(len(x)):
        if x[z] > 0:
            cont = cont + 1;

    x[-1] = cont
    print(x)
    return x
contpostive([-1,3,5,-1,2,-1])

#3 Suma total

def sumatotal(x):
    sumatot = 0
    for z in range(len(x)):
        sumatot = sumatot + x[z]
    print(sumatot)
    return sumatot
sumatotal([1,2,3,4,5])

#4 Promedio
def promedtotal(x):
    sumatot = 0
    for z in range(len(x)):
        sumatot = sumatot + x[z]
    promediotot = sumatot / len(x)
    print(promediotot)
    return promediotot
promedtotal([1,2,3,4])

#5 Longitud
def longitud(x):
    print(len(x))
    return len(x)
longitud([2,3,8,6])

#6 Mínimo

def valminimo(x):
    if len(x) > 0:
        min = x[0]
        for z in range(len(x)):
            if x[z] < min:
                min = x[z]
        print(min)
        return min
    else:
        print(False)
        return False

valminimo([-1,2,-3,-10,-9])

#7 Máximo

def valmaximo(x):
    if len(x) > 0:
        max = x[0]
        for z in range(len(x)):
            if x[z] > max:
                max = x[z]
        print(max)
        return max
    else:
        print(False)
        return False

valmaximo([1,3,8,2,4])

#8 Análisis final

def analisisfinal(x):
    if len(x) > 0:
        max = x[0]
        min = x[0]
        sumtot = 0
        for z in range(len(x)):
            if x[z] > max:
                max = x[z]
            if x[z] < min:
                min = x[z]
            sumtot = sumtot + x[z]
        print("Tolal:",sumtot,", Promedio:",sumtot/len(x),", Minimo:",min,", Maximo:",max,", Longitud:",len(x))

        todo=[sumtot,sumtot/len(x),min,max,len(x)]
        return todo
    else:
        print(False)
        return False
analisisfinal([1,2,3,4])

#op 2 - eje8 (diccionario)
def ultimate_analysis(list):
    diccionario = {}
    diccionario.update({"totalTotal": sumatotal(list)})
    diccionario.update({"promedio": promedtotal(list)})
    diccionario.update({"minimo": valminimo(list)})
    diccionario.update({"maximo": valmaximo(list)})
    diccionario.update({"longitud": longitud(list)})
    return diccionario
print(ultimate_analysis([37, 2, 1, -9]))

#9 Lista inversa
def list_inversa(x):
    x.reverse()#primero se ejecuta la funcion
    return x
print(list_inversa([1,2,3,4]))