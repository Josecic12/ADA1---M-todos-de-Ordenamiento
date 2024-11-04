def ordenamiento_seleccion(puntuaciones):
    for i in range(len(puntuaciones)):
        min_idx = i
        for j in range(i + 1, len(puntuaciones)):
            if puntuaciones[j] < puntuaciones[min_idx]:
                min_idx = j
        puntuaciones[i], puntuaciones[min_idx] = puntuaciones[min_idx], puntuaciones[i]
        print(f"Paso {i}: {puntuaciones}") 
    return puntuaciones

puntuaciones = [56, 74, 45, 89, 63]
print("Lista final ordenada:", ordenamiento_seleccion(puntuaciones))
