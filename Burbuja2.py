def ordenamiento_burbuja_precios(precios):
    n = len(precios)
    for i in range(n):
        for j in range(0, n - i - 1):
            if precios[j] > precios[j + 1]:
                precios[j], precios[j + 1] = precios[j + 1], precios[j]
            print(f"Paso {i}-{j}: {precios}") 
    return precios

precios = [10.5, 2.99, 5.25, 3.75]
print("Lista final ordenada:", ordenamiento_burbuja_precios(precios))
