'''Un programa que solicite a un usuario una entrada hasta 
que introduzca una respuesta válida. Un bucle while 
puede pedir repetidamente la entrada y comprobar su validez, 
terminando sólo cuando se proporciona una entrada válida '''

palabra_clave = 'Gen'
pregunta = input('Introduce la respuesta valida:')


while pregunta != palabra_clave:
    print('Error en la palabra')
    pregunta = input('Introduce la respuesta valida:')
print('Perfecto palabra correcta')

