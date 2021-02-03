
class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
        self.result += num
        for x in nums:
            self.result += x
            # print(x)
            # print(self.result)
        return self
    def subtract(self, num, *nums):
        self.result -= num
        # print(self.result)
        for y in nums:
            self.result -= y
            # print(y)
            # print(self.result)
        return self
# crear una instruccion:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!

xd = MathDojo()
x = xd.add(1,2,3,4).result
print(x)
dd = MathDojo()
x = dd.add(2,5,7).result
print(x)
df = MathDojo()
x = df.add(2,5,6,0,4,6).result
print(x)

x = xd.subtract(1,2).result
print(x)
x = dd.subtract(1,5).result
print(x)
x = df.subtract(2,10).result
print(x)

x = xd.add(1,2,3,5,4).add(2,1).subtract(5,9,1,7).result
print(x)