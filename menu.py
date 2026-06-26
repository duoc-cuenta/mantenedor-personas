import gestion_personas

op = None
continuar = True
telefonos = []

# Carga la lista con personas
gestion_personas.precargar_datos()

while continuar:
    print("1) Registrar persona")
    print("2) Eliminar persona (por ID)")
    print("3) Editar persona (por ID)")
    print("4) Buscar persona (por ID)")
    print("5) Buscar personas por edad")
    print("6) Imprimir todas las personas")
    print("7) Salir")
    op = int(input("Ingrese una opción: "))

    if op == 1:
        gestion_personas.registrar_persona()

    elif op == 2:
        gestion_personas.imprimir_personas()
        gestion_personas.eliminar_persona()

    elif op == 4:
        id = int(input('Ingrese el id de la persona que desea buscar: '))
        gestion_personas.buscar_persona_por_id(id)

    elif op == 6:
        gestion_personas.imprimir_personas()