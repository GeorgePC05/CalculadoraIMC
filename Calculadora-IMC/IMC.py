print("Bienvenido a tu calculadora de IMC")
apellidos = input ("Introduce tus apellidos\n")
nombre = input("Ahora tu nombre\n")
print ("Muchas gracias " + nombre)
float(input("¿Que edad tienes? "))
cond = False
while cond == False:
    try:
        edad = input("¿Que edad tienes?: ")
        if edad is not None:
            edad = float(edad)
            cond = True
        else:
            print("Ingresa un dato no nulo")
    except ValueError:
        print("Por favor, ingresa un valor númerico")   

float(input("Ingresa tu peso\n"))
peso = input("Ingresa tu peso\n")
tipo = peso.isnumeric()
if tipo == True:
     print("Gracias")
else: 
    print("Ingresa datos numericos")
peso = int(peso)

float(input("Ingresa tu estatura\n"))
estatura = input("Ingresa tu estatura\n")
tipo = estatura.isnumeric()
if tipo == True:
    print("Gracias, estamos trabajando en el calculo de tu IMC")
else: 
    print("Ingresa datos numericos")
estatura = float(estatura)

imc = peso / estatura**2
print(f"{nombre} hemos determinado que tu IMC es {imc}")

