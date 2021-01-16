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
