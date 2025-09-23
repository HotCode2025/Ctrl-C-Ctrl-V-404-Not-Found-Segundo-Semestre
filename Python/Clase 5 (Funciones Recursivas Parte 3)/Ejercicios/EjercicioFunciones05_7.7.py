# Ejercicio 5: Convertidor de temperaturas

# Función para convertir de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Función para convertir de Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Programa principal de prueba
print("=== Conversor de temperaturas ===")
c = float(input("Ingresa temperatura en Celsius: "))
print(f"{c}°C son {celsius_a_fahrenheit(c):.2f}°F")

f = float(input("Ingresa temperatura en Fahrenheit: "))
print(f"{f}°F son {fahrenheit_a_celsius(f):.2f}°C")



