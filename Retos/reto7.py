# Escribir una función Python con un nombre descriptivo preciso, como 
# calculate_diameter_circle, incorporando al mismo tiempo un caso de serpiente.

# La función debe tomar un argumento: radius (con una pista de tipo float).

# Debe calcular el diámetro de un círculo (diámetro = radius * 2) y devolverlo. 
# ASí como no hay ningún requisito para que el radio sea un número entero, 
# usted debe asumir un retorno de float. Se le han dado instrucciones de que 
# si el usuario envía un radio negativo, la función debe devolver -1 
# para indicar un error, ya que un radio negativo no es una situación común. 

# Incluya un docstrip claro e informativo que explique el propósito de la función, 
# los argumentos y el valor de retorno, utilizando también sugerencias de tipo.

def calculate_diameter_circle(radius: float) -> float:
    """
        Esta función calcula el perimetro de un circulo

        Args: radius(float): el radio puede ser un número decimal o entero.
            Si el radio del circulo es negativo devolvera -1
        
        Returns: El diametro del circulo (radius * 2) 
    """
    if radius < 0:
        return -1.0
    else:
        return radius * 2

print("Radius: 7, Diameter: ", calculate_diameter_circle(7))
print("Radius: 2.5, Diameter: ", calculate_diameter_circle(2.5))
print("Radius: 0, Diameter: ", calculate_diameter_circle(0))
print("Radius: -1, Diameter: ", calculate_diameter_circle(-1))
print("Radius: 1000000, Diameter: ", calculate_diameter_circle(1000000))
