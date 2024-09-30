# crear una clase de alumnos con los atributos que usted crea por comviniencia
# luego instanciara a 4 alumnos

class alumno:
    def __init__(self,nombre,dni,sexo,edad,programa_estudios="Apsti"):
        self.nombre=nombre
        self.dni=dni
        self.sexo=sexo
        self.edad=edad
        self.programa_estudios=programa_estudios
    def mostar_alumnos(self):
        return{
            "nombre":self.nombre,
            "dni":self.dni,
            "sexo":self.sexo,
            "edad":self.edad,
            "programa_estudios":self.programa_estudios
        }
    # metodos
    def escribir(self):
        print("estoy escribiendo")
    
    def tarea(self,nombre_docente):
        print("haciendo la tarea de:",nombre_docente)
    
    def terminar_tarea(self):
        print("terminando tarea anterior")


Percy=alumno("Percy",71500856,"Masculino",21)
Percy.tarea("Alicia")
Percy.terminar_tarea()
print(Percy.mostar_alumnos())

Bretmer=alumno("Bretmer",72566654,"Masculino",20)
print(Bretmer.mostar_alumnos())
Kelly=alumno("Kelly",65300856,"Femenino",23)
print(Kelly.mostar_alumnos())
Ana=alumno("Ana",63333546,"Femenino",21)
print(Ana.mostar_alumnos())