# comandos y ejemplos coding dojo analizar comando por separado en al consola
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"mi nombre es {first_name} {last_name} y tengo {age} años")
##
first_name = "Zen"
last_name = "Coder"
age = 27
print("Mi nombre es {} {} y tengo {} años.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("Mi nombre es {} {} y tengo {} años.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.
##
hw = "Hola %s" % "mundo" 	# con valores literales
py = "Me encanta Python %d" % 3
print(hw, py)
# salida: Hola mundo Me encanta Python 3
name = "Zen"
age = 27
print("Mi nombre es %s y soy %d" % (name, age))		# o con variables
# Salida: Mi nombre es Zen y tengo 27
##
x = "hola mundo"
print(x.title())
# Salida:
"Hello World"
##
##
#funciones
def add(a,b):#nombre de la función: 'add', parámetros: a y b 
    x = a + b# proceso
    return x# retorno value: x
#variables de la funcion
new_val = add(3, 5)    # llamando a la función add, con los argumentos 3 y 5 copy
print(new_val)    # el resultado de la función add se devuelve y se guarda en new_val, por lo que veremo
#ejemplos de funciones
def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # el valor devuelto por la función se asigna a la variable
print(greeting) # mostrará 'Hi Michael'
