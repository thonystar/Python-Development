''' Ejecuta una fucnion que muestre una tabla de multiplicar usando bucles'''

for i in range(1, 13):
    for j in range(1, 13):
        print(i, '*', j, '=', i*j, end = "\t" )
    print()
