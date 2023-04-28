# ---SEMANA DOS---

#  CARÁCTERES ESPECIALES
print("I'm\nlearning \n"'"Python"')

print("--------")
# PARÁMETRO END
print("Hola", end=" ")
print("Adios")

print("--------")
# TRANSFERENCIA
print('Un tipo le dice a otro : "¿Cómo estás?"')
print("Y el otro le contesta : '¡Pues anda que tú!'")

print("--------")
text1 = "Hola"
text2 = "Mundo"
text3 = "Python"
print(text1, text2, text3, sep="-")

print("--------")

# ---SEMANA TRES---

#ACTIVIDAD 1
a = (5 + 3 * 2 / 6 - 4)
b = (4/2-3+6)
c = (7-8/2-2)**2
x = a * b / c
print(x)
print("--------")
#-----------------

#ACTIVIDAD 2
a = ((17-15)**3 + (7-12)**2)
b = ((6-7)*(12-23))
x = a / b
print(x)
print("--------")
#-----------------

#ACTIVIDAD 3
a = 14-(7+4*3-((-2)**2*2-6))
b = (2**2+6-5*3)+3-(5-2**3/2)
x = a + b
print(x)
print("--------")
#-----------------

#AREA DE UN TRIÁNGULO
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es: ", area)
print("--------")
#-----------------

#AREA Y PERÍMETRO DEL RECTÁNGULO
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
area = base * altura
perimetro = (base * 2) + (altura * 2)
print("El área del rectángulo es: ", area)
print("El perímetro del rectángulo es: ", perimetro)
print("--------")
#-----------------

#EXPRECIÓN MATEMÁTICA 1
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
d = float(input("Ingrese el valor de d: "))
mat1 = a**3*b
mat2 = 2*a*b**2
mat3 = pow(12*d**4, 1/2)
x = (mat1 / mat2 ) - mat3
print("El resultado de la expresión es: ", x)
print("--------")

#EXPRECIÓN MATEMÁTICA 2
x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))
c = float(input("Ingrese el valor de c: "))
mat1 = 5*x**3*y**2
mat2 = pow(2*c**3, 1/4)
mat3 = mat1 / mat2
print("El resultado de la expresión es: ", mat3)
print("--------")

