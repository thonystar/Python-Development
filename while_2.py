'''Un programa que solicite a un usuario una entrada hasta 
que introduzca una respuesta válida. Un bucle while 
puede pedir repetidamente la entrada y comprobar su validez, 
terminando sólo cuando se proporciona una entrada válida '''

valor_aceptado = False

while not valor_aceptado:
    num = int(input('Introduzca un valor aceptado '))
    if num > 0:
        valor_aceptado = True
    else:
        print('No es el valor aceptado')
print('Correcto, valor aceptado')