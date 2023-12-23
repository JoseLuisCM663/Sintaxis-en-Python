lista =["hola", 2, 3.5, True, "adios"]

tupla=("hola", 2, 3.5, True, "adios")

#esto es valido
lista[0] = 9
#esto no es valido
#tupla[2] = "hola"

print(lista[0])
print(tupla[0])

#creando un conjunto set
conjunto = {"hola", 2, 3.5, True, "adios"}
print(conjunto)

conjunto={"pene"}
print(conjunto)

conjunto = {"hola", 2, 3.5, True, "hola"}
print(conjunto)

#creando un diccionario(key:value)
diccionario = {
    "nombre":"luis",
    "apellido":"marquez",
    "edad":20,
    "feliz":True,
    "altura":1.70
    }
print(diccionario)
print(diccionario["nombre"])