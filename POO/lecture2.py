class personaje:
    # atributos
    def __init__(self,nombre,edad,usuario,bando,raza):
        self.nombre=nombre
        self.edad=edad
        self.usuario=usuario
        self.bando=bando
        self.raza=raza
    def mostar_personaje(self):
        return{
            "nombre":self.nombre,
            "edad":self.edad,
            "usuario":self.usuario,
            "bando":self.bando,
            "raza":self.raza
        }
luffy=personaje("luffy",18,"gomu gomu no mi","pirata","humano")
print(luffy.nombre)
print(luffy.mostar_personaje())
cobby=personaje("cobby",15,"no","swort","humano")
print(cobby.bando)
print(cobby.mostar_personaje())
king=personaje("king",40,"zoan mitologica","pirata","lunaria")
print(king.raza)
print(king.mostar_personaje())