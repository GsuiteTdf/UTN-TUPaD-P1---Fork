#Actividad 1
print("Hola Mundo")
#Actividad 2
nombre = input("Por favor, ingresa tu nombre: ")
print(f"¡Hola, {nombre}!")
#Actividad 3
nombre = input("Por favor, ingresa tu nombre completo: ")
edad = input("¿Cuántos años tienes? ")
residencia = input("¿Dónde vives? ")
print(f"¡Soy, {nombre}!, tengo {edad} y soy de {residencia}!")
#Actividad 4
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)
# Actividad 5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600  # 1 hora = 3600 segundos
print(f"{segundos} segundos equivalen a {horas} horas.")
# Actividad 6
numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
# Actividad 7
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")
# Actividad 8
altura = float(input("Ingrese su altura en metros (por ejemplo, 1.75): "))
peso = float(input("Ingrese su peso en kilogramos (por ejemplo, 70): "))
imc = peso / (altura ** 2)
print(f"Su Índice de Masa Corporal (IMC) es: {imc}")
# Actividad 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius} °C equivalen a {fahrenheit} °F")
# Actividad 10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio}")
