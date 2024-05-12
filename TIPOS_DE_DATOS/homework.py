#hacer un programa que me permita agregar nombre del producto cantidad precio unitario y total del pago
#al final mostrar el igv y el subtotal
#agregar el nombre del producto
nombre:str = input("Ingrese el nombre del producto: ")
#agregar la cantidad del producto
cantidad:int = int(input("Ingrese la cantidad del producto: "))
#agregar el presio unitario del producto
precio_unitario:int = float(input("Ingrese el precio unitario del producto: "))
#sacar el pago total 
total_pago:int=precio_unitario*cantidad
#igv
igv:int=0.18*total_pago
#subtotal
subtotal:int=total_pago-igv
#mostrar por pantalla
print("igv:",igv,"subtotal:",subtotal,"total a pagar:",total_pago)