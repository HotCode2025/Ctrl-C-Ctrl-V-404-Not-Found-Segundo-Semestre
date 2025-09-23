def multiplicar(*args):
    if len(args) == 0:
        return 0
    
    resultado = 1
    for numero in args:
        resultado *= numero
    
    return resultado

print(multiplicar(2, 3, 4))        # Output: 24
print(multiplicar(5, 10))          # Output: 50
print(multiplicar(2, 2, 2, 2))     # Output: 16
print(multiplicar(1.4, 2, 3))      # Output: 8.399999
print(multiplicar())               # Output: 0 