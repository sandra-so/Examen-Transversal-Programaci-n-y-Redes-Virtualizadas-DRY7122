from geopy.distance import geodesic

def obtener_coordenadas(pais):
    # Coordenadas aproximadas de los centros de chile y peru
    coordenadas = {
        "chile": (-33.4489, -70.6693),  # Santiago, chile
        "peru": (-12.0464, -77.0428)    # Lima, peru
    }
    return coordenadas.get(pais, None)

def calcular_distancia(pais_origen, pais_destino):
    coordenadas_origen = obtener_coordenadas(pais_origen)
    coordenadas_destino = obtener_coordenadas(pais_destino)
    
    if coordenadas_origen and coordenadas_destino:
        # Calcular la distancia utilizando geopy
        distancia = geodesic(coordenadas_origen, coordenadas_destino).kilometers
        return distancia
    else:
        return None

if __name__ == "__main__":
    print("Bienvenido al calculador de distancias entre chile y peru")

    pais_origen = input("Ingrese el Pais de Origen (chile o peru): ")
    pais_destino = input("Ingrese el Pais de Destino (chile o peru): ")

    if pais_origen not in ["chile", "peru"] or pais_destino not in ["chile", "peru"]:
        print("Por favor, ingrese 'chile' o 'Peru' como paises validos.")
    else:
        print(f"Calculando distancia entre {pais_origen} y {pais_destino}...")

        distancia = calcular_distancia(pais_origen, pais_destino)

        if distancia:
            print(f"La distancia entre {pais_origen} y {pais_destino} es de aproximadamente {distancia:.2f} kilometros.")
        else:
            print("No se pudo calcular la distancia. Verifique los paises ingresados.")
