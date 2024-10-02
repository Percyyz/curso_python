# crear una clase banco 
# sus atributos seran nombre, apellido, dni, numero de cuenta y saldo inicial
# como metodos podremos hacer deposito retirar dinero y ver estado de cuenta.

class Banco:
    def __init__(self,nombre,apellido,dni,numero_cuenta,saldo_inicial):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.numero_cuenta=numero_cuenta
        self.saldo_inicial=saldo_inicial
    
    def depositar(self,monto):
        if monto>0:
            self.saldo_inicial=self.saldo_inicial+monto
            resultado=f"deposito realizado: {self.saldo_inicial}"
            return resultado

    def retirar(self,monto):
        if monto>0:
            self.saldo_inicial=self.saldo_inicial-monto
            resultado=f"retiro realizado con exito: {self.saldo_inicial}"
            return resultado

percy=Banco("Percy","Yarihuaman",71500856,4111112333,200)
print(percy.depositar(20))
print(percy.saldo_inicial)


# EJERCICIO 2
# Crear una clase agencia 
# con sua atributos nombre y apellidos del pasajero dni numero de asiento fecha de viaje
# sus metodos seran ingresar origen, ingresar destino, cancelar viaje y ver estado de pasaje

class Agencia:
    def __init__(self, nombre, apellidos, dni, numero_asiento, fecha_viaje):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.numero_asiento = numero_asiento
        self.fecha_viaje = fecha_viaje

    def ingresar_origen(self, origen):
        self.origen = origen
        print(f"Origen del viaje: {self.origen}")

    def ingresar_destino(self, destino):
        self.destino = destino
        print(f"Destino del viaje: {self.destino}")

    def cancelar_viaje(self):
        self.estado = "Cancelado"
        print("El viaje ha sido cancelado.")
    
    def ver_estado_pasaje(self):
        return f"Estado de pasaje: {self.estado}"


pasajero = Agencia("Percy", "Yarihuaman", "71500856", "25A", "05-10-2024")
pasajero.ingresar_origen("Lima")
pasajero.ingresar_destino("Cusco")
pasajero.cancelar_viaje()
print(pasajero.ver_estado_pasaje())
