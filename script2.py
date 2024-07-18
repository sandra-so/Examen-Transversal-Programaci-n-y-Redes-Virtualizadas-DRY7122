from geopy.distance import geodesic

def obtener_coordenadas(pais):
    coordenadas = {
        "chile": (-33.4489, -70.6693),  # Santiago, Chile
        "peru": (-12.0464, -77.0428)    # Lima, Perú
    }
    return coordenadas[pais]

def calcular_distancia(pais_origen, pais_destino):
    coordenadas_origen = obtener_coordenadas(pais_origen)
    coordenadas_destino = obtener_coordenadas(pais_destino)
    distancia_km = geodesic(coordenadas_origen, coordenadas_destino).kilometers
    distancia_mi = geodesic(coordenadas_origen, coordenadas_destino).miles
    return distancia_km, distancia_mi

def calcular_duracion(distancia_km, medio_transporte):
    velocidades = {
        "auto": 100,
        "avion": 800
    }
    duracion_horas = distancia_km / velocidades[medio_transporte]
    return duracion_horas

if __name__ == "__main__":
    while True:
        pais_origen = input("Ingrese el País de Origen (chile o peru) o 'e' para salir: ")
        if pais_origen.lower() == 'e':
            break

        pais_destino = input("Ingrese el País de Destino (chile o peru) o 'e' para salir: ")
        if pais_destino.lower() == 'e':
            break

        if pais_origen not in ["chile", "peru"] or pais_destino not in ["chile", "peru"]:
            print("Por favor, ingrese 'chile' o 'peru' como países válidos.")
            continue

        medio_transporte = input("Ingrese el medio de transporte (auto, avion) o 'e' para salir: ")
        if medio_transporte.lower() == 'e':
            break

        if medio_transporte not in ["auto", "avion"]:
            print("Por favor, ingrese un medio de transporte válido ('auto' o 'avion').")
            continue

        distancia_km, distancia_mi = calcular_distancia(pais_origen, pais_destino)
        duracion_horas = calcular_duracion(distancia_km, medio_transporte)

        print(f"\nLa distancia entre {pais_origen} y {pais_destino} es de aproximadamente {distancia_km:.2f} kilómetros ({distancia_mi:.2f} millas).")
        print(f"Duración estimada del viaje en {medio_transporte}: {duracion_horas:.2f} horas.")
        print(f"Narrativa del viaje: Viajar desde {pais_origen} hasta {pais_destino} en {medio_transporte} cubre una distancia de {distancia_km:.2f} kilómetros, lo que tomaría aproximadamente {duracion_horas:.2f} horas.\n")

        continuar = input("¿Desea calcular otra distancia? (si/no): ")
        if continuar.lower() != 'si':
            break

    print("Gracias por usar el calculador de distancias. ¡Hasta luego!")
