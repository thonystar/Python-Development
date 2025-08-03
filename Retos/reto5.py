## Pregunta 2
### Conversiones de texto: Funciones integradas de conversión en Python
# Instrucciones:

#Comience con las variables proporcionadas int_value, float_value, y text_value.

#Utilice la función type() para guardar el tipo de datos de float_value
#  en la variable type_of_float_value donde dice STEP 2: YOUR CODE HERE.
#  La función tipo se puede utilizar para determinar el tipo de datos de
#  las variables, y se puede utilizar para evitar errores y excepciones.

# Utilice la función int() para convertir el valor de text_value a un número
#  entero y almacenarlo en la variable text_value_as_int donde dice STEP 3:
#  YOUR CODE HERE. Incluso si una cadena contiene un valor numérico, debe ser
#  convertida a un valor numérico (int o float) para ser utilizada como parte
#  de operaciones matemáticas.

# Utilice la función str() para convertir el valor de int_value en una cadena y
#  almacenarlo en la variable int_value_as_text donde dice STEP 4: YOUR CODE HERE.
#  Muchas veces, los valores numéricos que no tendrán operaciones matemáticas realizadas
#  sobre ellos (por ejemplo, números de tarjetas de crédito, números de serie, códigos
#  postales americanos) serán convertidos a texto.

# Los resultados se imprimirán. Verás el tipo de datos de la variable float, seguido
#  de los resultados de sumar dos valores numéricos, seguido de los resultados de
#  sumar esos mismos dos valores como cadenas.

int_value = 15
float_value = 4.1
text_value = "33"

# Guarda el tipo de variable
type_of_float_value = type(float_value)
type_of_int_value = type(int_value)
type_of_text_value = type(text_value)


## Convierte un valor de texto en numeric
text_value_as_int = int(text_value)

## Convertir un valor entero en texto
int_value_as_text = str(int_value)

print(f'El tipo de dato de la variable float value es: {type_of_float_value}')
print(f'El valor de la suma entre {int_value} y {text_value_as_int} es {int_value + text_value_as_int}')
print(f'El valor de la suma entre {text_value} y {int_value_as_text} es {text_value + int_value_as_text}')

