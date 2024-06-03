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
print(lista1)

lista1.remove({
    "nombre":"abel",
    "apellido":"jurado",
    "edad":20
})
print(lista1)

indice=lista1.index({
   "nombre":"willians",
   "apellido":"barrientos",
   "edad":11 
})
print(lista1[indice])

# 2 CREAR UNA LISTA CON 4 DICCIONARIOS DONDE TENTENDRAN LOS DATOS DE SUS MASCOTAS (NOMBRE, EDAD, SEXO Y RAZA)
## TAREAS
# 1. MOSTRAR LA LISTA CON LOS 4 DICCIONARIOS
# 2. EDITAR EL TERCER REGISTRO Y CAMBIARLE LA EDAD SIN MODIFICAR LA LISTA ORIGINAL
# 3. MOSTRAR LA LISTA ORIGINAL Y LUEGO LA LISTA CON EL TERCER REGISTRO MODIFICADO
lista_mascotas=[{
    "nombre":"Toby",
    "edad":3,
    "sexo":"Macho",
    "raza":"Pastor Aleman"
},
{
    "nombre":"Luna",
    "edad":2,
    "sexo":"Hembra",
    "raza":"Chihuahua"
},
{
    "nombre":"Pancho",
    "edad":1,
    "sexo":"Macho",
    "raza":"Dalmata"
},
{
    "nombres":"bella",
    "edad":4,
    "sexo":"hembra",
    "raza":"Boxer"
}]
print(lista_mascotas)

copia_lista=lista_mascotas.copy()
print(lista_mascotas)
copia_lista[3]["edad"]=2
print(copia_lista)

# 3 UN EMPRESARIO DE ALQUILER DE MOTOS DESEA GUARDAR EN UNA BASE DE DATOS  LA INFORMACION  DE SUS VEHICULOS, PROCESO QUE DESEA AUTOMATIZAR
# CON UN SISTEMA INFORMATICO, LAS ACCIONES QUE PUEDE REALIZAR EL EMPRESARIO SON  VER LAS LISTAS DE AUTOS QUE TIENE, PODRA TAMBIEN ACTUALIZAR
# LA LISTA Y AGREGAR UN NUEVO VEHICULO

# CASOS DE USO
 
 # YO COMO EMPRESARIO DE AUTOS
 # DESEO GUARDAR EN UNA BASE DE DATOS LA INFORMACION DE MIS VEHICULOS
 # PARA PODER VER LA LISTA DE MIS AUTOS


# PROGRAMACION
lista_autos=[{
    "matricula":"1111-BAB",
    "modelo":"19 TSE CHAMADE",
    "precio":700,
    "año":2000,
    "estado":"Bueno",
    "color":"Plomo",
    "motor":"Diesel"
},{
    "matricula":"1258-FRA",
    "modelo":"Passat",
    "precio":8000,
    "año":2014,
    "estado":"Bueno",
    "color":"Rojo",
    "motor":"Gasolina"
},{
    "matricula":"1478-CCA",
    "modelo":"Astra",
    "precio":3200,
    "año":2015,
    "estado":"Bueno",
    "color":"Negro",
    "motor":"Diesel"
},{
    "matricula":"2222-AAA",
    "modelo":"A1 TDI",
    "precio":5000,
    "año":2017,
    "estado":"Bueno",
    "color":"Blanco",
    "motor":"Diesel"
},{
    "matricula":"5848-EEA",
    "modelo":"Saxo",
    "precio":4000,
    "año":2014,
    "estado":"Bueno",
    "color":"Rojo",
    "motor":"Diesel"
}]
print(lista_autos)

 # YO COMO EMPRESARIO DE AUTOS 
 # DESEO TENER LA LISTA DE MIS AUTOS
 # PARA PODER ACTUALIZAR MI LISTA  Y AGREGAR UN NUEVO VEHICULO

lista_autos [0]["precio"]
lista_autos [1]["precio"]
lista_autos [2]["precio"]
lista_autos [3]["precio"]
lista_autos [4]["precio"]

lista_autos.append({

})