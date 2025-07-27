import pandas as pd

ruta = 'C:/Users/USER/OneDrive/Desktop/Python/Python-Development/Practicas/PC1-List/Archivos/grocery_list.csv'
compras = pd.read_csv(ruta)

print(compras.head(5))

# Transformamos el Dataframe en una lista

list_compras = compras['item'].tolist()

print(list_compras)


## Se quiere agregar mas elementos a la lista

agregar_listas = ['Melocoton', 'Arroz', 'Fideos', 'Granadia']

## Creamos un bucle para ingresar los nuevos valores
for lista in agregar_listas:
    list_compras.append(lista)

print(list_compras)

# Remueve de la lista "Eggs" y "Apples"


list_compras.remove('Eggs')
list_compras.remove('Apples')

print(list_compras)