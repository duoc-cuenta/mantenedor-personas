personas = []

def imprimir_menu():
    print("1) Registrar persona")
    print("2) Eliminar persona (por ID)")
    print("3) Editar persona (por ID)")
    print("4) Buscar persona (por ID)")
    print("5) Buscar personas por edad")
    print("6) Imprimir todas las personas")
    print("7) Salir")    

def registrar_persona():
    id = int(input("Ingrese ID de persona: "))
    nombre = input("Ingrese nombre de persona: ")
    edad = int(input("Ingrese edad de persona: "))
    estatura = float(input("Ingrese estatura de persona: "))

    estado_int = int(input("Ingrese estado de persona [1-Activo | 2-Inactivo]: "))
    estado_bool = False
    if estado_int == 1:
        estado_bool = True
    elif estado_int == 2:
        estado_bool = False
    else:
        print("¡Opción no válida!")
    
    telefonos = [] # Resetear los teléfonos anteriores
    cant_telefonos = int(input("¿Cuántos teléfonos desea ingresar?: "))                 
    for i in range(cant_telefonos):
        nro_telefono = int(input("Ingrese número de teléfono: "))
        telefonos.append(nro_telefono)
        print("¡Teléfono registrado!")
    
    # Se crea el diccionario con los datos de la persona
    persona = {'id':id,
        'nombre':nombre,
        'edad':edad,
        'estatura':estatura,
        'estado':estado_bool,
        'telefonos': telefonos
    }

    # Agregar diccionario a lista de personas
    personas.append(persona)
    print("¡Persona registrada!")

def imprimir_personas():
    for p in personas:
        print(f"ID: {p["id"]}") 
        print(f"Nombre: {p["nombre"]}") 
        print(f"Edad: {p["edad"]}") 
        print(f"Estatura: {p["estatura"]}") 
        print(f"Estado: {p["estado"]}")
        
        lista_telefonos = p["telefonos"]
        for t in lista_telefonos:
            print(f"+56 {t}")
        
        print("---------------------------------")

def eliminar_persona():
    id_para_eliminar = int(input("Ingrese el ID de la persona que desea eliminar: "))        
    i = 0
    while i < len(personas):
        id_recuperado = personas[i]["id"]

        # Preguntar si id existe
        if id_para_eliminar == id_recuperado:
            # Eliminar persona encontrada
            personas.pop(i)
            print("¡Persona eliminada!")

        i = i + 1

def precargar_datos():
    persona1 = {'id':111,
           'nombre':'Anita',
           'edad':22,
           'estatura':1.68,
           'estado':True,
           'telefonos': [992225587, 993336587]
    }
    persona2 = {'id':112,
           'nombre':'Juanito',
           'edad':21,
           'estatura':1.70,
           'estado':False,
           'telefonos': [998885557]
    }
    persona3 = {'id':113,
           'nombre':'Pedrito',
           'edad':20,
           'estatura':1.8,
           'estado':True,
           'telefonos': [985552224, 963332227]
    }
    personas.append(persona1)
    personas.append(persona2)
    personas.append(persona3)

# Construir función y subirla al repositorio remoto
# def buscar_personas_por_edad(edad):


def buscar_persona_por_id():
    id = int(input('Ingrese el id de la persona que desea buscar: '))
    persona_encontrada = obtener_persona_por_id(id)
    if persona_encontrada is None:
        print("No se encontró la persona")
    else:
        print(f"Nombre: {persona_encontrada['nombre']}")
        print(f"Edad: {persona_encontrada['edad']}")
        print(f"Estatura: {persona_encontrada['estatura']}")
        print(f"Estado: {persona_encontrada['estado']}")
        
        for t in persona_encontrada['telefonos']:
            print(f"+56 {t}")

def obtener_persona_por_id(id_persona):
    for p in personas:
        if p["id"] == id_persona:
            return p
    return None