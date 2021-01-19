#1 Basico
for x in range(151):
    print(x)

#2 Multiplos de 5
for x in range(0,1005,5):
    print(x)

#3 Contar, dojo way
for x in range(1,1001,1):
    if x % 5 == 0:
        print("Coding")
        if x % 10 == 0:
            print("Coding Dojo")
    else: print(x)


#4 ¡uf, Eso es bastante grande!
sum = 0
for x in range(1,500000,2):
    sum = sum+x
print(sum)

#5 Cuenta regresiva por cuatro
for x in range(2018,0,-4):
    print(x)

#6Contador flexible
lowNum = 1
highNum = 10
mult = 5
for x in range(lowNum,highNum+1):
    if x % mult == 0:
        print(x)