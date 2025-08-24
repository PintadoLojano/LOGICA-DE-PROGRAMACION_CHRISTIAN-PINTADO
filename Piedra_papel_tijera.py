def jugar(): # def Es una palabra reservada de Python que se usa para definir una función.

    # Pedir nombres de los jugadores
    while True:
        Nombre1 = input("😎 Ingrese su nombre Jugador No 1: ").strip() or "jugador No 1"
        if Nombre1.isalpha():
            break
        else:
            print ("⚠️ Error: el nombre solo debe contener letras.")

    while True:
        Nombre2 = input("😃 Ingrese su nombre Jugador No 2: ").strip() or "jugador No 2"
        if Nombre2.isalpha ():
            break
        else:
                print ("⚠️ Error: el nombre solo debe contener letras.")

    # Inicializar puntos
    Puntos_jugadorNo1= 0 #Inicianda el puntaja del JugadorNo1 en 0
    Puntos_jugadorNo2= 0 #Iniciando el puntaje del JugadorNo2 en 0
    Juego_Activo = True ## Variable booleana que controla si el juego sigue o se detiene
    Ronda = 0 # Inicia el contador de rondas

    while Juego_Activo: # Bucle principal del juego
        Ronda +=1 # Aumentamos el contador de rondas
        print(f"\n ✔ Ronda {Ronda}") # Muestra el numero de la ronda

        # Solicitar la elección de ambos jugadores y convertir a minúsculas
        Eleccion_jugadorNo1=input(f"{Nombre1}, elige: Piedra, Papel o Tijera: ").lower()
        Eleccion_jugadorNo2=input(f"{Nombre2}, elige: Piedra, Papel o Tijera: ").lower()

        # Validar que las elecciones sean correctas
        if Eleccion_jugadorNo1 not in ["piedra","papel","tijera"] or Eleccion_jugadorNo2 not in ["piedra","papel","tijera"]:
            print("!⚠ Error! elige entre: Piedra, Papel o Tijera") 
            Ronda-= 1 # No contar ronda si existe error.
            continue  # Si la elección no es válida, vuelve al inicio del bucle para pedir otra vez

        # Comparar las elecciones
        if Eleccion_jugadorNo1 == Eleccion_jugadorNo2:
            print("!🤝Empate sigue jugando !")
        else:
             # Condiciones en las que gana el JugadorNo1
            if  Eleccion_jugadorNo1=="piedra"and Eleccion_jugadorNo2 =="tijera":
                print(f"{Nombre1} !gana🎉!")
                Puntos_jugadorNo1+=1
                
            elif Eleccion_jugadorNo1 == "papel"and Eleccion_jugadorNo2 == "piedra":
                print(f"{Nombre1} !gana🎉!")
                Puntos_jugadorNo1+=1

            elif Eleccion_jugadorNo1 == "tijera"and Eleccion_jugadorNo2 == "papel":
                print(f"{Nombre1} !gana🎉!")
                Puntos_jugadorNo1+=1
             # Condiciones en las que gana el JugadorNo2
            elif Eleccion_jugadorNo2 == "piedra"and Eleccion_jugadorNo1 == "tijera":
                print(f"{Nombre2} !gana🎉!")
                Puntos_jugadorNo2+=1

            elif Eleccion_jugadorNo2 == "papel"and Eleccion_jugadorNo1 == "piedra":
                print(f"{Nombre2} !gana🎉!")
                Puntos_jugadorNo2+=1
                
            elif Eleccion_jugadorNo2 == "tijera"and Eleccion_jugadorNo1 == "papel":
                print(f"{Nombre2} !gana🎉!")
                Puntos_jugadorNo2+=1

        # Mostrar puntaje actual de ambos jugadores
        print(f"Puntaje -> {Nombre1}: {Puntos_jugadorNo1}, {Nombre2}: {Puntos_jugadorNo2}")

        # Preguntar si desean jugar otra vez
        respuesta=input("Jugar otra vez? (si/no):").lower()
        if respuesta != "si":
            Juego_Activo= False # Terminar el juego.

    # Mostrar puntaje final y numeros de rondas jugadas.
    print ("🏁 !juego terminado!")
    print (f"☑ Total de rondas jugadas: {Ronda}")
    print(f"📊 Puntaje final -> {Nombre1}: {Puntos_jugadorNo1}, {Nombre2}: {Puntos_jugadorNo2}")

#Llamar a la funcion para iniciar el juego
jugar()