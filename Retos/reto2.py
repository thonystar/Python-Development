''' En este ejercicio, utilizarás un bucle for para mostrar valores que son divisibles 
entre 3 y 4. Empezarás por 0 y seguirás hasta el final. Comenzará en 0 y pasará 
por valor_máximo + 1. 

Una variable max_value, establecida en 50
'''

n = 51

for i in range(0, n):
    if i % 3 == 0 and i % 4 == 0:
        print(f'El numero {i} es divisible por 3 y 4')
    

