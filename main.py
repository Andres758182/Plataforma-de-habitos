# ------------------------
# MENU
# ------------------------
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Crear base de datos")
        print("2. Insertar datos")
        print("3. Estadísticas y Rendimiento General")
        print("4. Red Social y Amigos")
        print("5. Historiales y Seguimiento de Actividad")
        print("6. Hábitos, Retos y Exploración")
        print("7. Ubicación, Rankings y Logros")
        print("8. Salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            print("Opción 1 seleccionada: Crear base de datos")
            # Agregar aquí la lógica para crear la base de datos
        elif option == "2":
            print("Opción 2 seleccionada: Insertar datos")
            # Agregar aquí la lógica para insertar datos
        elif option == "3":
            while True:
                print("\n--- Submenú de Estadísticas y Rendimiento General ---")
                print("1. Consultar estadísticas mensuales generales de un usuario")
                print("2. Visualizar la comparativa mensual de estadísticas por categoría")
                print("3. Ver las categorías con mayor inscripción de hábitos por parte del usuario")
                print("4. Consultar las ciudades con mayor actividad global durante el mes pasado")
                print("5. Salir del submenú de estadísticas y rendimiento general")

                sub_option = input("Selecciona una opción del submenú: ")

                if sub_option == "1":
                    print("Sub-opción 1 seleccionada: Consultar estadísticas mensuales generales de un usuario")
                    # Agregar aquí la lógica para consultar estadísticas mensuales generales de un usuario
                elif sub_option == "2":
                    print("Sub-opción 2 seleccionada: Visualizar la comparativa mensual de estadísticas por categoría")
                    # Agregar aquí la lógica para visualizar la comparativa mensual de estadísticas por categoría
                elif sub_option == "3":
                    print("Sub-opción 3 seleccionada: Ver las categorías con mayor inscripción de hábitos por parte del usuario")
                    # Agregar aquí la lógica para ver las categorías con mayor inscripción de hábitos por parte del usuario
                elif sub_option == "4":
                    print("Sub-opción 4 seleccionada: Consultar las ciudades con mayor actividad global durante el mes pasado")
                    # Agregar aquí la lógica para consultar las ciudades con mayor actividad global durante el mes pasado
                elif sub_option == "5":
                    print("Saliendo del submenú de estadísticas y rendimiento general...")
                    break

        elif option == "4":
            while True:
                print("\n--- Submenú de Red Social y Amigos ---")
                print("1. Consultar la lista de amigos de un usuario")
                print("2. Ver la actividad reciente de los amigos")
                print("3. Explorar los retos de amigos en la categoría principal del usuario")
                print("4. Obtener el historial y métricas de uso de un hábito público específico por parte de los amigos")
                print("5. Ver los logros asociados a los hábitos de los amigos")
                print("6. Salir del submenú de red social y amigos")

                sub_option = input("Selecciona una opción del submenú: ")

                if sub_option == "1":
                    print("Sub-opción 1 seleccionada: Consultar la lista de amigos de un usuario")
                    # Agregar aquí la lógica para consultar la lista de amigos de un usuario
                elif sub_option == "2":
                    print("Sub-opción 2 seleccionada: Ver la actividad reciente de los amigos")
                    # Agregar aquí la lógica para ver la actividad reciente de los amigos
                elif sub_option == "3":
                    print("Sub-opción 3 seleccionada: Explorar los retos de amigos en la categoría principal del usuario")
                    # Agregar aquí la lógica para explorar los retos de amigos en la categoría principal del usuario
                elif sub_option == "4":
                    print("Sub-opción 4 seleccionada: Obtener el historial y métricas de uso de un hábito público específico por parte de los amigos")
                    # Agregar aquí la lógica para obtener el historial y métricas de uso de un hábito público específico por parte de los amigos
                elif sub_option == "5":
                    print("Sub-opción 5 seleccionada: Ver los logros asociados a los hábitos de los amigos")
                    # Agregar aquí la lógica para ver los logros asociados a los hábitos de los amigos
                elif sub_option == "6":
                    print("Saliendo del submenú de red social y amigos...")
                    break

        elif option == "5":
            while True:
                print("\n--- Submenú de Historiales y Seguimiento de Actividad ---")
                print("1. Consultar el historial de hábitos cumplidos de un usuario")
                print("2. Ver las entradas recientes de un hábito específico en el último mes")
                print("3. Consultar las rachas pasadas de un hábito específico")
                print("4. Obtener las entradas diarias de un usuario filtradas por una fecha específica.")
                print("5. Consultar el progreso histórico y diario en un reto específico")
                print("6. Salir del submenú de historiales y seguimiento de actividad")

                sub_option = input("Selecciona una opción del submenú: ")

                if sub_option == "1":
                    print("Sub-opción 1 seleccionada: Consultar el historial de hábitos cumplidos de un usuario")
                    # Agregar aquí la lógica para consultar el historial de hábitos cumplidos de un usuario
                elif sub_option == "2":
                    print("Sub-opción 2 seleccionada: Ver las entradas recientes de un hábito específico en el último mes")
                    # Agregar aquí la lógica para ver las entradas recientes de un hábito específico en el último mes
                elif sub_option == "3":
                    print("Sub-opción 3 seleccionada: Consultar las rachas pasadas de un hábito específico")
                    # Agregar aquí la lógica para consultar las rachas pasadas de un hábito específico
                elif sub_option == "4":
                    print("Sub-opción 4 seleccionada: Obtener las entradas diarias de un usuario filtradas por una fecha específica")
                    # Agregar aquí la lógica para obtener las entradas diarias de un usuario filtradas por una fecha específica
                elif sub_option == "5":
                    print("Sub-opción 5 seleccionada: Consultar el progreso histórico y diario en un reto específico")
                    # Agregar aquí la lógica para consultar el progreso histórico y diario en un reto específico
                elif sub_option == "6":
                    print("Saliendo del submenú de historiales y seguimiento de actividad...")
                    break

        elif option == "6":
            while True:
                print("\n--- Submenú de Exploración y Análisis de Datos ---")
                print("1. Buscar los 5 hábitos más populares del mes pasado por categoría.")
                print("2. Identificar los 3 hábitos con menor rendimiento o actividad del usuario en el último mes.")
                print("3. Consultar los 5 retos de una categoría con mayor tasa de cumplimiento.")
                print("4. Buscar retos relacionados con la categoría del último hábito iniciado.")
                print("5. Explorar los retos disponibles por categoría no empezados en el último mes.")
                print("6. Salir del submenú de exploración y análisis de datos.")

                sub_option = input("Selecciona una opción del submenú: ")

                if sub_option == "1":
                    print("Sub-opción 1 seleccionada: Buscar los 5 hábitos más populares del mes pasado por categoría.")
                    # Agregar aquí la lógica para buscar los 5 hábitos más populares del mes pasado por categoría
                elif sub_option == "2":
                    print("Sub-opción 2 seleccionada: Identificar los 3 hábitos con menor rendimiento o actividad del usuario en el último mes.")
                    # Agregar aquí la lógica para identificar los 3 hábitos con menor rendimiento o actividad del usuario en el último mes
                elif sub_option == "3":
                    print("Sub-opción 3 seleccionada: Consultar los 5 retos de una categoría con mayor tasa de cumplimiento.")
                    # Agregar aquí la lógica para consultar los 5 retos de una categoría con mayor tasa de cumplimiento
                elif sub_option == "4":
                    print("Sub-opción 4 seleccionada: Buscar retos relacionados con la categoría del último hábito iniciado.")
                    # Agregar aquí la lógica para buscar retos relacionados con la categoría del último hábito iniciado
                elif sub_option == "5":
                    print("Sub-opción 5 seleccionada: Explorar los retos disponibles por categoría no empezados en el último mes (ordenados por registros).")
                    # Agregar aquí la lógica para explorar los retos disponibles por categoría no empezados en el último mes (ordenados por registros)
                elif sub_option == "6":
                    print("Saliendo del submenú de exploración y análisis de datos...")
                    break

        elif option == "7":
            while True:
                print("\n--- Submenú de Ubicación, Rankings y Logros ---")
                print("1. Consultar el top de los 10 usuarios con mayor racha filtrados por ciudad.")
                print("2. Encontrar usuarios residentes en la misma ciudad de referencia.")
                print("3. Buscar retos de una categoría específica inscritos por usuarios de una ciudad dada.")
                print("4. Ver los logros recientes ganados por un usuario en el último mes.")
                print("5. Consultar el ranking de los top 5 usuarios en cumplir un reto específico (ordenados por tiempo de culminación).")
                print("6. Salir del submenú de ubicación, rankings y logros.")

                sub_option = input("Selecciona una opción del submenú: ")

                if sub_option == "1":
                    print("Sub-opción 1 seleccionada: Consultar el top de los 10 usuarios con mayor racha filtrados por ciudad.")
                    # Agregar aquí la lógica para consultar el top de los 10 usuarios con mayor racha filtrados por ciudad
                elif sub_option == "2":
                    print("Sub-opción 2 seleccionada: Encontrar usuarios residentes en la misma ciudad de referencia.")
                    # Agregar aquí la lógica para encontrar usuarios residentes en la misma ciudad de referencia
                elif sub_option == "3":
                    print("Sub-opción 3 seleccionada: Buscar retos de una categoría específica inscritos por usuarios de una ciudad dada.")
                    # Agregar aquí la lógica para buscar retos de una categoría específica inscritos por usuarios de una ciudad dada
                elif sub_option == "4":
                    print("Sub-opción 4 seleccionada: Ver los logros recientes ganados por un usuario en el último mes.")
                    # Agregar aquí la lógica para ver los logros recientes ganados por un usuario en el último mes
                elif sub_option == "5":
                    print("Sub-opción 5 seleccionada: Consultar el ranking de los top 5 usuarios en cumplir un reto específico (ordenados por tiempo de culminación).")
                    # Agregar aquí la lógica para consultar el ranking de los top 5 usuarios en cumplir un reto específico (ordenados por tiempo de culminación)
                elif sub_option == "6":
                    print("Saliendo del submenú de ubicación, rankings y logros...")
                    break

        elif option == "8":
            print("Saliendo del programa...")
            break

# ------------------------
# MAIN
# ------------------------
def main():
    menu()


if __name__ == "__main__":
    main()

