"""
Sistema de Gestión de Avances en el Gimnasio
"""

# Base de datos principal
gym_data = {}

print("\nBienvenido a tu Sistema de Gestión de Gym")

# Bucle principal del programa
while True:
    # Mostrar menú
    print("\nMENU PRINCIPAL")
    print("1. Añadir registro")
    print("2. Editar registro")
    print("3. Eliminar registro")
    print("4. Ver todos los registros")
    print("5. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    # Opción 1: AÑADIR REGISTRO
    if opcion == "1":
        print("\nAÑADIR NUEVO REGISTRO")
        
        # Pedir semana
        while True:
            try:
                semana = int(input("Qué semana quieres añadir? (ej: 1, 2, 3...): "))
                if semana >= 1:
                    break
                else:
                    print("Debe ser un número mayor a 0")
            except:
                print("Ingresa un número válido")
        
        # Pedir día
        print("\nDías disponibles:")
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        for i in range(len(dias)):
            print(f"{i+1}. {dias[i].capitalize()}")
        
        while True:
            try:
                opcion_dia = int(input("Selecciona el día (1-7): "))
                if 1 <= opcion_dia <= 7:
                    dia = dias[opcion_dia - 1]
                    break
                else:
                    print("Debe ser un número entre 1 y 7")
            except:
                print("Ingresa un número válido")
        
        # Inicializar estructura si no existe
        if semana not in gym_data:
            gym_data[semana] = {}
        
        # Verificar si ya existe
        if dia in gym_data[semana]:
            print(f"\nYa existe un registro para Semana {semana}, {dia.capitalize()}")
            sobrescribir = input("Deseas sobrescribir? (s/n): ").lower()
            if sobrescribir != 's':
                print("Operación cancelada")
                continue
        
        # Crear lista de ejercicios
        gym_data[semana][dia] = []
        
        print(f"\nRegistrando ejercicios para Semana {semana}, {dia.capitalize()}")
        
        # Añadir ejercicios
        while True:
            print("\nAÑADIR EJERCICIO")
            nombre = input("Nombre del ejercicio: ").strip()
            
            if nombre == "":
                print("El nombre no puede estar vacío")
                continue
            
            while True:
                try:
                    series = int(input("Número de series: "))
                    if series >= 1:
                        break
                    else:
                        print("Debe ser mayor a 0")
                except:
                    print("Ingresa un número válido")
            
            while True:
                try:
                    repeticiones = int(input("Repeticiones por serie: "))
                    if repeticiones >= 1:
                        break
                    else:
                        print("Debe ser mayor a 0")
                except:
                    print("Ingresa un número válido")
            
            while True:
                try:
                    peso = float(input("Peso utilizado (kg): "))
                    break
                except:
                    print("Ingresa un número válido")
            
            print("\nComodidad (1-5):")
            print("1 = Muy difícil | 5 = Muy cómodo")
            while True:
                try:
                    comodidad = int(input("Nivel de comodidad: "))
                    if 1 <= comodidad <= 5:
                        break
                    else:
                        print("Debe ser entre 1 y 5")
                except:
                    print("Ingresa un número válido")
            
            notas = input("Notas adicionales (opcional): ").strip()
            
            # Crear diccionario del ejercicio
            ejercicio = {
                "nombre": nombre,
                "series": series,
                "repeticiones": repeticiones,
                "peso": peso,
                "comodidad": comodidad,
                "notas": notas
            }
            
            # Añadir a la lista con append
            gym_data[semana][dia].append(ejercicio)
            print(f"Ejercicio '{nombre}' añadido correctamente")
            
            continuar = input("\nAñadir otro ejercicio? (s/n): ").lower()
            if continuar != 's':
                break
        
        print(f"\nRegistro completado para Semana {semana}, {dia.capitalize()}")
    
    # Opción 2: EDITAR REGISTRO
    elif opcion == "2":
        print("\nEDITAR REGISTRO")
        
        if len(gym_data) == 0:
            print("No hay registros disponibles")
            continuar = input("\nDeseas realizar otra operación? (s/n): ").lower()
            if continuar != 's':
                print("\nHasta luego!")
                break
            continue
        
        # Mostrar registros
        print("\nREGISTROS DISPONIBLES")
        for semana in sorted(gym_data.keys()):
            print(f"\nSEMANA {semana}")
            for dia, ejercicios in gym_data[semana].items():
                print(f"  {dia.capitalize()} ({len(ejercicios)} ejercicios)")
                for idx in range(len(ejercicios)):
                    ej = ejercicios[idx]
                    print(f"     {idx+1}. {ej['nombre']} - {ej['series']}x{ej['repeticiones']} @ {ej['peso']}kg")
        
        # Seleccionar semana
        while True:
            try:
                semana = int(input("\nQué semana quieres seleccionar?: "))
                if semana in gym_data:
                    break
                else:
                    print("Esa semana no existe")
            except:
                print("Ingresa un número válido")
        
        # Seleccionar día
        print(f"\nDías disponibles en Semana {semana}:")
        dias_disponibles = list(gym_data[semana].keys())
        for i in range(len(dias_disponibles)):
            print(f"{i+1}. {dias_disponibles[i].capitalize()}")
        
        while True:
            try:
                opcion_dia = int(input("Selecciona el día: "))
                if 1 <= opcion_dia <= len(dias_disponibles):
                    dia = dias_disponibles[opcion_dia - 1]
                    break
                else:
                    print(f"Debe ser entre 1 y {len(dias_disponibles)}")
            except:
                print("Ingresa un número válido")
        
        # Seleccionar ejercicio
        print(f"\nEjercicios en {dia.capitalize()}:")
        ejercicios = gym_data[semana][dia]
        for i in range(len(ejercicios)):
            ej = ejercicios[i]
            print(f"{i+1}. {ej['nombre']} - {ej['series']}x{ej['repeticiones']} @ {ej['peso']}kg")
        
        while True:
            try:
                idx_ejercicio = int(input("Selecciona el ejercicio: "))
                if 1 <= idx_ejercicio <= len(ejercicios):
                    idx_ejercicio = idx_ejercicio - 1
                    break
                else:
                    print(f"Debe ser entre 1 y {len(ejercicios)}")
            except:
                print("Ingresa un número válido")
        
        # Editar ejercicio
        ejercicio = gym_data[semana][dia][idx_ejercicio]
        
        print(f"\nEditando: {ejercicio['nombre']}")
        print("Deja en blanco para mantener el valor actual")
        
        nuevo_nombre = input(f"Nombre [{ejercicio['nombre']}]: ").strip()
        if nuevo_nombre != "":
            ejercicio['nombre'] = nuevo_nombre
        
        entrada = input(f"Series [{ejercicio['series']}]: ").strip()
        if entrada != "":
            ejercicio['series'] = int(entrada)
        
        entrada = input(f"Repeticiones [{ejercicio['repeticiones']}]: ").strip()
        if entrada != "":
            ejercicio['repeticiones'] = int(entrada)
        
        entrada = input(f"Peso [{ejercicio['peso']}]: ").strip()
        if entrada != "":
            ejercicio['peso'] = float(entrada)
        
        entrada = input(f"Comodidad (1-5) [{ejercicio['comodidad']}]: ").strip()
        if entrada != "":
            ejercicio['comodidad'] = int(entrada)
        
        entrada = input(f"Notas [{ejercicio['notas']}]: ").strip()
        if entrada != "":
            ejercicio['notas'] = entrada
        
        print(f"\nEjercicio '{ejercicio['nombre']}' actualizado correctamente")
    
    # Opción 3: ELIMINAR REGISTRO
    elif opcion == "3":
        print("\nELIMINAR REGISTRO")
        print("1. Eliminar un ejercicio específico")
        print("2. Eliminar un día completo")
        print("3. Eliminar una semana completa")
        
        opcion_eliminar = input("Selecciona una opción: ")
        
        if opcion_eliminar == "1":
            if len(gym_data) == 0:
                print("No hay registros disponibles")
                continuar = input("\nDeseas realizar otra operación? (s/n): ").lower()
                if continuar != 's':
                    print("\nHasta luego!")
                    break
                continue
            
            # Mostrar registros
            print("\nREGISTROS DISPONIBLES")
            for semana in sorted(gym_data.keys()):
                print(f"\nSEMANA {semana}")
                for dia, ejercicios in gym_data[semana].items():
                    print(f"  {dia.capitalize()} ({len(ejercicios)} ejercicios)")
                    for idx in range(len(ejercicios)):
                        ej = ejercicios[idx]
                        print(f"     {idx+1}. {ej['nombre']} - {ej['series']}x{ej['repeticiones']} @ {ej['peso']}kg")
            
            # Seleccionar
            while True:
                try:
                    semana = int(input("\nQué semana?: "))
                    if semana in gym_data:
                        break
                    else:
                        print("Esa semana no existe")
                except:
                    print("Ingresa un número válido")
            
            dias_disponibles = list(gym_data[semana].keys())
            print(f"\nDías disponibles:")
            for i in range(len(dias_disponibles)):
                print(f"{i+1}. {dias_disponibles[i].capitalize()}")
            
            while True:
                try:
                    opcion_dia = int(input("Selecciona el día: "))
                    if 1 <= opcion_dia <= len(dias_disponibles):
                        dia = dias_disponibles[opcion_dia - 1]
                        break
                except:
                    print("Ingresa un número válido")
            
            ejercicios = gym_data[semana][dia]
            print(f"\nEjercicios:")
            for i in range(len(ejercicios)):
                print(f"{i+1}. {ejercicios[i]['nombre']}")
            
            while True:
                try:
                    idx = int(input("Selecciona el ejercicio: "))
                    if 1 <= idx <= len(ejercicios):
                        idx = idx - 1
                        break
                except:
                    print("Ingresa un número válido")
            
            # Eliminar con pop
            ejercicio_eliminado = gym_data[semana][dia].pop(idx)
            print(f"\nEjercicio '{ejercicio_eliminado['nombre']}' eliminado")
            
            # Si no quedan ejercicios, eliminar el día
            if len(gym_data[semana][dia]) == 0:
                del gym_data[semana][dia]
                print(f"El día {dia} quedó vacío y fue eliminado")
            
            # Si no quedan días, eliminar la semana
            if len(gym_data[semana]) == 0:
                del gym_data[semana]
                print(f"La semana {semana} quedó vacía y fue eliminada")
        
        elif opcion_eliminar == "2":
            if len(gym_data) == 0:
                print("No hay registros disponibles")
                continuar = input("\nDeseas realizar otra operación? (s/n): ").lower()
                if continuar != 's':
                    print("\nHasta luego!")
                    break
                continue
            
            while True:
                try:
                    semana = int(input("Qué semana?: "))
                    if semana in gym_data:
                        break
                    else:
                        print("Esa semana no existe")
                except:
                    print("Ingresa un número válido")
            
            print(f"\nDías en Semana {semana}:")
            dias = list(gym_data[semana].keys())
            for i in range(len(dias)):
                print(f"{i+1}. {dias[i].capitalize()}")
            
            while True:
                try:
                    idx_dia = int(input("Selecciona el día a eliminar: "))
                    if 1 <= idx_dia <= len(dias):
                        dia_eliminar = dias[idx_dia - 1]
                        break
                except:
                    print("Ingresa un número válido")
            
            del gym_data[semana][dia_eliminar]
            print(f"\nDía {dia_eliminar} eliminado")
            
            if len(gym_data[semana]) == 0:
                del gym_data[semana]
                print(f"La semana {semana} quedó vacía y fue eliminada")
        
        elif opcion_eliminar == "3":
            if len(gym_data) == 0:
                print("No hay registros disponibles")
                continuar = input("\nDeseas realizar otra operación? (s/n): ").lower()
                if continuar != 's':
                    print("\nHasta luego!")
                    break
                continue
            
            while True:
                try:
                    semana = int(input("Qué semana quieres eliminar?: "))
                    if semana in gym_data:
                        break
                    else:
                        print("Esa semana no existe")
                except:
                    print("Ingresa un número válido")
            
            confirmar = input(f"Seguro que quieres eliminar toda la Semana {semana}? (s/n): ").lower()
            if confirmar == 's':
                del gym_data[semana]
                print(f"\nSemana {semana} eliminada completamente")
    
    # Opción 4: VER REGISTROS
    elif opcion == "4":
        if len(gym_data) == 0:
            print("\nNo hay registros disponibles")
        else:
            print("\nREGISTROS DISPONIBLES")
            
            for semana in sorted(gym_data.keys()):
                print(f"\nSEMANA {semana}")
                for dia, ejercicios in gym_data[semana].items():
                    print(f"  {dia.capitalize()} ({len(ejercicios)} ejercicios)")
                    for idx in range(len(ejercicios)):
                        ej = ejercicios[idx]
                        print(f"     {idx+1}. {ej['nombre']} - {ej['series']}x{ej['repeticiones']} @ {ej['peso']}kg")
                        print(f"        Comodidad: {ej['comodidad']}/5")
                        if ej['notas'] != "":
                            print(f"        Notas: {ej['notas']}")
    
    # Opción 5: SALIR
    elif opcion == "5":
        print("\nGracias por usar el sistema!")
        break
    
    else:
        print("Opción no válida")
        continue
    
    # Preguntar si quiere continuar
    if opcion != "5":
        continuar = input("\nDeseas realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("\nHasta luego!")
            break