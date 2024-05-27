#crear una lista de 5 alumnos cada alumno almacenaremos su nombre apellido y edad
# insertar al final de la lista los datos de antony
# eliminar de la lista si existe los datos de abel
# buscar y mostrar el alumno de la posision 4 de la lista

lista1=[{
    "nombre":"percy",
    "apellido":"yarihuaman",
    "edad":16
},{
    "nombre":"bretmer",
    "apellido":"condori",
    "edad":18
},{
    "nombre":"abel",
    "apellido":"jurado",
    "edad":20
},{
    "nombre":"erick",
    "apellido":"huamani",
    "edad":18
},{
    "nombre":"willians",
    "apellido":"barrientos",
    "edad":11
}]

lista1.append({
    "nombre":"anthony",
    "apellido":"crezes",
    "edad":30
})

lista1.pop(2)

len(lista1) > 3
alumno_posicion_4 = lista1[3]
print(lista1)
