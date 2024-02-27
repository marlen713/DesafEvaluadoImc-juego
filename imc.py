'''
Actividad 1 - IMC
El IMC, conocido también como el Índice de masa corporal, es una medida que asocia el peso de una persona con su talla (su altura). Este valor es utilizado normalmente como un indicador nutricional y constituye un índice fácil y sencillo de calcular para determinar el estado de obesidad y sobrepeso de una persona. El IMC se calcula de la siguiente manera:
            𝐼𝑀𝐶 = 𝑊
                  𝐻 2
                  
W : corresponde al peso de la persona en Kg.
H: corresponde a la altura en metros.
IMC: EL valor del IMC, en [Kg/m2]
'''
# AQUI ES PARA QUE PODAMOS INGRESAR NUESTROS DATOS
w = float(input("Coloca tu peso en número: "))
centimetros = float(input("Coloca tu altura en centímetros: "))

# ESTA ES PARA QUE LOS CENTIMETROS DADO ME LOS DIVIDA Y PODER USARLOS EN LA FORMULA
h = centimetros /100

# AQUI MI FORMULA LA CUAL debo la altura primero exponenciarla para luego dividir y me de mi IMC
imc = w / (h**2)

if imc >= 0 and imc <= 18.4:
    print(f"Su IMC es : {imc:.2f} La clasificación OMS es: Bajo Peso")
elif imc >= 18.5 and imc <= 25:
    print(f"Su IMC es : {imc:.2f} La clasificación OMS es: Adecuado")     
elif imc >= 25 and imc <= 30:
    print(f"Su IMC es : {imc:.2f} La clasificación OMS es: Sobre Peso")   
elif imc >= 30 and imc <= 35:
    print(f"Su IMC es : {imc:.2f} La clasificación OMS es: Obesidad Grado I") 
elif imc >= 35 and imc <= 40:
    print(f"Su IMC es : {imc:.2f} La clasificación OMS es: Obesidad Grado II") 
elif imc >= 40:
    print(f"Su IMC es : {imc:.2f} La clasificación OMS es: Obesidad Grado III") 
else:
    print("ingrese un valor valido...")
