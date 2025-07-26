### Se tocara el tema de la comprensión de listas 
## La comprensión de listas es la forma de crear una nueva lista respecto a otra 
## existente mediante iterables

notas = [10,12,9, 4, 13, 2]
curva = 10

curva_notas = [nota + curva for nota in notas]
print('Lista inicial: ', notas)
print('Lista final: ', curva_notas)