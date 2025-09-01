def operaciones_conjuntos(lista1, lista2):

    set1 = set(lista1)
    set2 = set(lista2)
    
    union = list(set1 | set2)
    
    diferencia1 = list(set1 - set2)
    
    diferencia2 = list(set2 - set1)
    
    interseccion = list(set1 & set2)
    
    return union, diferencia1, diferencia2, interseccion

lista1 = ["python", "java", "c++", "javascript", "python", "java"]
lista2 = ["python", "ruby", "go", "javascript", "swift", "python"]

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("-" * 50)

union, dif1, dif2, inter = operaciones_conjuntos(lista1, lista2)

# Mostrar resultados
print("1. Palabras que aparecen en las listas (unión):")
print(union)
print()

print("2. Palabras que aparecen en la primera pero no en la segunda:")
print(dif1)
print()

print("3. Palabras que aparecen en la segunda pero no en la primera:")
print(dif2)
print()

print("4. Palabras que aparecen en ambas listas (intersección):")
print(inter)