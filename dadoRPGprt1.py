import random

def inicio():
    print("El rey Raldor te ha encomendado una misión urgente: detener los ataques orcos que han devastado el reino.")
    print("El líder de los orcos, Grumak el Cazador, se esconde en lo profundo del Bosque Oscuro.")
    print("Tu misión es cazarlo y eliminarlo. Los aldeanos te proporcionan una poción de curación (+10 HP).")

def seleccionar_clase():
    print("Elige tu clase:")
    print("1. **Guerrero** - HP: 30, Habilidad: Golpe Poderoso (+5 de daño, recarga cada 3 turnos)")
    print("2. **Mago** - HP: 20, Habilidad: Bola de Fuego (daño a múltiples enemigos, recarga cada 3 turnos)")
    print("3. **Pícaro** - HP: 25, Habilidad: Ataque Furtivo (doble de daño si emboscas, recarga cada 2 turnos)")
    
    clase = input("Selecciona el número de tu clase: ")
    if clase == '1':
        return {"clase": "Guerrero", "HP": 30, "habilidad": "Golpe Poderoso", "recarga": 3, "atributo": "FUE"}
    elif clase == '2':
        return {"clase": "Mago", "HP": 20, "habilidad": "Bola de Fuego", "recarga": 3, "atributo": "INT"}
    elif clase == '3':
        return {"clase": "Pícaro", "HP": 25, "habilidad": "Ataque Furtivo", "recarga": 2, "atributo": "DES"}
    else:
        print("Selección inválida. Inténtalo de nuevo.")
        return seleccionar_clase()

def distribuir_atributos():
    print("Reparte 6 puntos entre Fuerza (FUE), Destreza (DES) e Inteligencia (INT) para personalizar tu personaje.")
    print("Puedes poner un máximo de 4 puntos en un solo atributo.")
    
    puntos = 6
    atributos = {"FUE": 0, "DES": 0, "INT": 0}
    
    while puntos > 0:
        for atributo in atributos:
            print(f"Tienes {puntos} puntos restantes.")
            puntos_a_asignar = int(input(f"¿Cuántos puntos quieres asignar a {atributo}? "))
            if puntos_a_asignar <= puntos and puntos_a_asignar <= 4:
                atributos[atributo] += puntos_a_asignar
                puntos -= puntos_a_asignar
            else:
                print("Número de puntos inválido. Inténtalo de nuevo.")
    return atributos

def tirar_dado(lados):
    return random.randint(1, lados)

def tirar_d20_con_modificador(atributo, modificador):
    resultado = tirar_dado(20) + modificador
    print(f"Tirada de D20: {resultado - modificador} + Modificador ({modificador}) = {resultado}")
    return resultado

def combate(jugador, enemigo):
    print(f"¡Comienza el combate contra {enemigo['nombre']}!")
    while jugador['HP'] > 0 and enemigo['HP'] > 0:
        print(f"\nHP del Jugador: {jugador['HP']} | HP del {enemigo['nombre']}: {enemigo['HP']}")
        print("\n¿Qué quieres hacer?")
        print("1. Atacar")
        print("2. Usar habilidad")
        print("3. Ignorar")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            resultado_dado = tirar_d20_con_modificador(jugador['atributo'], jugador['atributos'][jugador['atributo']])
            if resultado_dado == 1:
                print("¡Fallaste el ataque y recibes daño del enemigo!")
                jugador['HP'] -= enemigo['ataque']
            elif resultado_dado >= 2 and resultado_dado <= 10:
                print("¡Ataque débil!")
                enemigo['HP'] -= jugador['daño'] // 2
            elif resultado_dado >= 11 and resultado_dado <= 19:
                print("¡Ataque exitoso!")
                enemigo['HP'] -= jugador['daño']
            elif resultado_dado == 20:
                print("¡Ataque crítico!")
                enemigo['HP'] -= jugador['daño'] * 2
        
        elif opcion == '2':
            if jugador['recarga'] == 0:
                print(f"Usas tu habilidad especial: {jugador['habilidad']}!")
                enemigo['HP'] -= jugador['daño'] + 5  # Ejemplo de daño adicional por habilidad
                jugador['recarga'] = 3  # Reinicia el contador de recarga
            else:
                print(f"Tu habilidad especial está en recarga. {jugador['recarga']} turnos restantes.")
        
        elif opcion == '3':
            print("Decides ignorar el combate por este turno.")
        
        else:
            print("Opción inválida. Pierdes tu turno.")
        
        if enemigo['HP'] > 0:
            resultado_dado_enemigo = tirar_d20_con_modificador("modificador", enemigo['modificador'])
            if resultado_dado_enemigo >= jugador['CA']:
                jugador['HP'] -= enemigo['ataque']
                print(f"{enemigo['nombre']} te ha golpeado y te ha hecho {enemigo['ataque']} de daño.")
            else:
                print(f"{enemigo['nombre']} falló su ataque.")
        
        if jugador['recarga'] > 0:
            jugador['recarga'] -= 1
    
    if jugador['HP'] > 0:
        print(f"¡Has derrotado a {enemigo['nombre']}!")
    else:
        print(f"Has sido derrotado por {enemigo['nombre']}. Fin del juego.")
        exit()

def main():
    inicio()
    jugador = seleccionar_clase()
    jugador['atributos'] = distribuir_atributos()
    jugador['daño'] = 5  # Daño base del jugador
    jugador['CA'] = 15  # Clase de armadura base del jugador
    jugador['recarga'] = 0  # Inicializa la recarga de la habilidad especial
    
    print("Te adentras en el Bosque Oscuro en busca de Grumak el Cazador.")
    
    # Ejemplo de combate
    orco = {"nombre": "Orco", "HP": 10, "ataque": 5, "modificador": 2, "CA": 12}
    combate(jugador, orco)
    
    if jugador['HP'] > 0:
        print("¡Has sobrevivido al combate inicial y continúas tu misión!")
    else:
        print("Has muerto en combate. Fin del juego.")
        exit()

if __name__ == "__main__":
    main()