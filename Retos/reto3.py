'''
Escribe un programa en Python que tome una lista de números e itere por cada 
número y compruebe si es par o impar. Utiliza la lista de números proporcionada
como punto de partida.
'''

números = [3, 9, 1, 10, 5, 2, 8]

for num in números:
    if num % 2 == 0:
        print(f'El número {num} es par')
    elif num % 2 != 0:
        print(f'El número {num} es impar')
    else:
        print('El número no esta dentro de la lista')
print('Listo!')
    