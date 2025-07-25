'''Creará un juego de adivinar números en el que el ordenador intentará adivinar 
un número secreto que usted le indique. El ordenador generará conjeturas aleatorias 
dentro de un rango (1 a 10) y continuará adivinando hasta que encuentre 
el número correcto. 

La salida debe ser la siguiente:

Guessing: 3

Guessing: 8

Guessing: 1

Guessing: 7

I guessed the right number! It was 7
'''

import random

secret_number = 6
guess = 0

while guess != secret_number:
    guess = random.randint(1, 10)
    print('Guessing: ', guess)
print("I guessed the right number! It was",secret_number)