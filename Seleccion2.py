def ordenamiento_seleccion_distancias(distancias):
    for i in range(len(distancias)):
        min_idx = i
        for j in range(i + 1, len(distancias)):
            if distancias[j] < distancias[min_idx]:
                min_idx = j
        distancias[i], distancias[min_idx] = distancias[min_idx], distancias[i]
        print(f"Paso {i}: {distancias}")
    return distancias

distancias = [12.3, 7.5, 5.8, 9.1]
print("Lista final ordenada:", ordenamiento_seleccion_distancias(distancias))
