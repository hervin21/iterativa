n = int(input("Ingresa un número entero: "))
suma = 0

while n > 9:
    suma += n % 10
    n //= 10

suma += n  # Agregar el último dígito a la suma

print("La suma de los dígitos de", n, "es:", suma)

