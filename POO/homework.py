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

