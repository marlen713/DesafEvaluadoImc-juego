'''
La piedra aplasta la tijera. ...
La tijera corta el papel. ...
El papel envuelve la piedra. ...
'''
# SE IMPORTA ESTA LIBRERIA PARA PODER USAR EL RAMDOM.CHOICE QUE PERMITE QUE EL PC AGARRE ALEATORIAMENTE LAS OPCIONES
import random


usuario = input("Escoge tu opción: ")
opciones = ["piedra", "papel", "tijera"]
pc =  random.choice(opciones)
inicia_juego = usuario in opciones



# AQUI INICIO MI JUEGO SI LLEGARAN A COLOCAR OTRA PALABRA NO TE DEJARA AVANZAR Y MOSTRARA ARGUMENTO INVALIDO
if inicia_juego == False:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
# EMPATE
elif usuario == "piedra" and pc == "piedra" or usuario == "papel" and pc == "papel" or usuario == "tijera" and pc == "tijera":
    print(f"Tu jugaste {usuario.capitalize()} \nComputador jugó {pc} \nEl juego empata")
# GANA EL USUARIO
elif usuario == "piedra" and pc == "tijera" or usuario == "tijera" and pc == "papel" or usuario == "papel" and pc == "piedra":
    print(f"Tu jugaste {usuario.capitalize()} \nComputador jugó {pc} \nGanastes!!")
# GANA EL COMPUTADOR
else:
    print(f"Tu jugaste {usuario.capitalize()} \nComputador jugó {pc} \nPerdiste!!")