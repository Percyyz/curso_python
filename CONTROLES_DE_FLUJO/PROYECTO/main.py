recervas= True
while recervas:
    print("\nMenú de opciones")
    print("1. Horarios disponibles.")
    print("2. Horas disponibles para la reservacion del gras.")
    print("3. pague el alquiler de la reserva realizada")
    opciones=input("ingrese una opcion del menu :")
    if opciones=="1":
        print("los horarios disponibles son:")
        print("A. LUNES    :03:00 PM - 04:00 PM")
        print("B. MARTES   :02:00 PM - 03:00 PM")
        opciones=input("ingrese una opcion del horario disponible para realizar la recerva :")
        if "A"<= opciones:
           print("hora reservada con exito")
           

