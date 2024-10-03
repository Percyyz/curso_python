class Banco:
    def __init__(self,nombre,apellido,dni,numero_cuenta,saldo_inicial):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.numero_cuenta=numero_cuenta
        self.saldo_inicial=saldo_inicial
    
    def depositar(self,monto):
        self.saldo_inicial+=monto

    def retirar(self,monto):
        if monto<self.saldo_inicial:
            self.saldo_inicial-=monto

    def ver_estado_cuenta(self):
        respuesta=f"""
        ----------bienvenido al banco "tepincha y estafa"-------------
        cliente: {self.nombre}, {self.apellido} numerocuenta: {self.numero_cuenta}.
        en estos momentos tienes un saldo de: s/.{self.saldo_inicial},
        fin del vaucher:
        ______________________________________________________________________________
        """
        return respuesta
        

percy=Banco("Percy","Yarihuaman",71500856,4111112333,200)
print(percy.ver_estado_cuenta())
percy.depositar(20)
print(percy.ver_estado_cuenta())
percy.retirar(30)
print(percy.ver_estado_cuenta())s