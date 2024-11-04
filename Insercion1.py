def ordenamiento_insercion(calificaciones):
    for i in range(1, len(calificaciones)):
        clave = calificaciones[i]
        j = i - 1
        while j >= 0 and clave < calificaciones[j]:
            calificaciones[j + 1] = calificaciones[j]
            j -= 1
        calificaciones[j + 1] = clave
        print(f"Paso {i}: {calificaciones}") 
    return calificaciones

calificaciones = [85, 90, 78, 92, 88]
print("Lista final ordenada:", ordenamiento_insercion(calificaciones))
