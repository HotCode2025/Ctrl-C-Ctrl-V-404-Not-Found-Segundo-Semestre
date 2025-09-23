# List comprehension o lista de comprension
# Es una forma concisa de crear listas en Python

names = ['Juan', 'Ana', 'Pedro', 'Maria', 'Pablo']
alongP = [name for name in names if name[0] == 'P'] # Nombres que empiezan con P
along3 = [name for name in names if len(name) > 3] # Nombres con mas de 3 letras
print(alongP) # ['Pedro', 'Pablo']
print(along3) # ['Juan', 'Pedro', 'Maria', 'Pablo']

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mexico"},
           {"name": "Heineken", "country": "Holanda"},
           ]

Arg = [bottle for bottle in bottleC if bottle["country"] == "Arg"] # Cervezas de Argentina
print(Arg) # [{'name': 'Quilmes', 'country': 'Arg'}]

           