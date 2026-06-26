import gestion_personas

op = None
continuar = True
telefonos = []

# Carga la lista con personas
gestion_personas.precargar_datos()

while continuar:
    gestion_personas.imprimir_menu()

    op = int(input("Ingrese una opción: "))

    if op == 1:
        gestion_personas.registrar_persona()

    elif op == 2:
        gestion_personas.imprimir_personas()
        gestion_personas.eliminar_persona()

    elif op == 4:        
        gestion_personas.buscar_persona_por_id()

    elif op == 6:
        gestion_personas.imprimir_personas()

    elif op == 7:
        print("Ha salido de a aplicación")
        input("Presione una tecla para continuar...")
        continuar = False