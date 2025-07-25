'''Creará un juego de adivinar números en el que el ordenador intentará adivinar 
un número secreto que usted le indique. El ordenador generará conjeturas aleatorias 
dentro de un rango (1 a 10) y continuará adivinando hasta que encuentre 
el número correcto. '''

secret_number = 4
guess = 0

while guess != secret_number:
    num = int(input('Indicame un número del 1 al 10: '))
    if num == secret_number:
        guess = secret_number
    elif num > 10:
        print('El numero es mayor a 10')
    else:
        print('No es el número secreto')
print('Numero secreto encontrado')    