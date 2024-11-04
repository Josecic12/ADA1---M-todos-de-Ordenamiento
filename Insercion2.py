def ordenamiento_insercion_alturas(alturas):
    for i in range(1, len(alturas)):
        clave = alturas[i]
        j = i - 1
        while j >= 0 and clave < alturas[j]:
            alturas[j + 1] = alturas[j]
            j -= 1
        alturas[j + 1] = clave
        print(f"Paso {i}: {alturas}") 
    return alturas

alturas = [3.5, 5.2, 4.8, 6.1]
print("Lista final ordenada:", ordenamiento_insercion_alturas(alturas))
