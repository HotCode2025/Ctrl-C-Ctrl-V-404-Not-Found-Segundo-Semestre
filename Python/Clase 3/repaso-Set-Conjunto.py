conjunto = set()
conjunto2 = {'bye'}

conjunto.add(7)
conjunto.add('Hola')
print(conjunto)

conjunto2.add('Hola')
print(conjunto2)

print(3 not in conjunto2)

#Igualdad de dos conjuntos

print(conjunto2 == conjunto)

conjunto3 = conjunto | conjunto2 #Union de dos conjuntos

print(conjunto3)

conjunto3 = conjunto & conjunto2 #Elementos que tienen en comun
print(conjunto3)

conjunto3 = conjunto - conjunto2 #Asigna el valor que esta en el conjunto y no en el conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto
print(conjunto3)

conjunto3 = conjunto ^ conjunto2 #Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto | conjunto2
print(conjunto.issubset(conjunto3)) #ver si conjunto es subconjunto del conjunto3
print(conjunto2.issubset(conjunto3)) #ver si conjunto2 es subconjunto del conjunto3
print(conjunto3.issubset(conjunto))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto)) #vemos si conjunto3 es un super conjunto
print(conjunto3.issuperset(conjunto2)) #vemos si conjunto3 es un super conjunto
print(conjunto2.issuperset(conjunto3)) #vemos si conjunto2 es un super conjunto

#Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun

print(conjunto.isdisjoint(conjunto2))