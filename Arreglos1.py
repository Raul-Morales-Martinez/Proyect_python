#lista
#pares de elementos
#ordenadas segun su ingreso
#acepta todos los tipos de datos
#se pueden recorrer y modificar los valores
#conjunto de datos, ordenados segun su ingreso, separados por coma(,),en []

lista_pares = [2,4,6,8,0]
print(lista_pares)
#todas comienzan en el posicion cero
print(lista_pares[0])#2
#tamaño de una lista len(arreglo)
print(len(lista_pares))#5
#acceder al ultimo elemento de la lista
print(lista_pares[len(lista_pares)-1])#0
#podemos recorrer los arreglos con valores negativos
print(lista_pares[-1])#0
print(lista_pares[-2])#8
print(lista_pares[-5])#2

#crear un arreglo vacio
arreglo = []
print("arreglo vacio de tamaño",len(arreglo))

print()
#secciones de lista
print(lista_pares[3:])#[8,0]
print(lista_pares[:3])#[2,4,6] no considera la posicion mencionada
print(lista_pares[:])#todos los elementos
arreglo = lista_pares #igualando las listas
arreglo2 = lista_pares[:]#obteniendo los valores del arreglo
print(arreglo)#[2,4,6,8,0]
#modificar valor de una lista
lista_pares[2] = 5
print(lista_pares)#[2,4,5,8,0]
print(arreglo)#[2,4,5,8,0]
print(arreglo2)#no se modifica [2,4,6,8,0]
num1 = lista_pares[2]#5 se guarda el valor
lista_pares[2] = 7 #[2,4,7,8,0]
print(lista_pares)#[2,4,7,8,0]
print(num1)#5 no recibio cambios
arreglo[0] = 1 #[1,4,7,8,0]
print(lista_pares)#[1,4,7,8,0] se modifican ambos arreglos
#agrega un valor al alrreglo al final
arreglo.append("a")
print(arreglo)#[1,4,7,8,0,'a']
