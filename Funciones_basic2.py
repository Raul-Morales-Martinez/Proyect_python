#1Cuenta regresiva

def  cuentaregre(y):
    list = []
    for x in range (y,-1,-1):
     list.append(x)
    print(list)
    return list
cuentaregre(5)

#2Imprimir y volver

def imprimirvolver(x):
    print(x[0])
    return x[1]
arr = [2 , 3]
imprimirvolver(arr)

#3 First Plus Length

def firstlong (x):
    sum = x[0] + len(x)
    print(sum)
    return sum
firstlong([1,5,8,7,6])

#4 Valores mayores que el segundo

def valmayorsec(arr):
    list = []
    if len(arr)>= 2:
        for x in arr:
            if x >= arr[1]:
                list.append(x)
        print(len(list))
        print(list)
        return list
    else:
        print(False)
        return False

valmayorsec([1,3,4,2,5])

#5 Esta longitud, ese valor

def tamvalor(x,y):
    #validación a traves try(numeros,letras, etc..) try => control o manejo de errores
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("no eran enteros")
        return False
    list = []
    for z in range(x):
        list.append(y)
    print(list)
    return list

tamvalor(4,7)