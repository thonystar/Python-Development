## Temperaturas árticas: Diversión con las Funciones matemáticas integradas en Python
### Ejercicio Matemático 1: Análisis de las Temperaturas Antárticas  
# Instrucciones:
# Comience con la lista antarctic_temperatures, que contiene los registros diarios
# de temperatura.

# Aplique la función max() a la lista antarctic_temperatures para obtener
# la temperatura más alta registrada.

# Aplique la función min() a la lista antarctic_temperatures
#  para determinar la temperatura más baja registrada.

# Imprima las temperaturas más alta y más baja.

# Calcule la temperatura media sumando todas las temperaturas de
#  la lista antarctic_temperatures mediante la función sum() y dividiendo por el número 
# de temperaturas, que puede determinar mediante la función len().
#  Redondee la temperatura media calculada a un decimal utilizando la función round().

#Imprima la temperatura media redondeada.

#Calcule el valor absoluto de la temperatura más fría utilizando la función abs().

# Imprime el valor absoluto de la temperatura más fría.

artarctic_temperatures = [-25.0, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

## Temperatura máxima
max_temperature = max(artarctic_temperatures)

print(f'La temperatura máxima es {max_temperature}')

## Temperatura minima
min_temperature = min(artarctic_temperatures)

print(f'La temperatura mínima es: {min_temperature}')
## Temperatura media
mean_temperature = round(sum(artarctic_temperatures) / len(artarctic_temperatures),1)
print(f'La temperatura media es: {mean_temperature} C°')

# el valor absoluto de la temperatura más fría

temperature_mas_fria = abs(min_temperature)

print(f'La temperatura más fría es: {temperature_mas_fria}')