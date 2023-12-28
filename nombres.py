integrantes = [
    {"Nombre": "Ricardo", "Apellido": "Hernandez"},
    {"Nombre": "Emanuel", "Apellido": "Lopez"},

]

for integrantes in integrantes:
    nombre_completo = f"{integrantes['Nombre']} {integrantes['Apellido']}"
    print(nombre_completo)
