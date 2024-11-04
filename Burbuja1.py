def ordenamiento_burbuja(edades):
    n = len(edades)
    for i in range(n):
        for j in range(0, n - i - 1):
            if edades[j] > edades[j + 1]:
                edades[j], edades[j + 1] = edades[j + 1], edades[j]
            print(f"Paso {i}-{j}: {edades}") 
    return edades

edades = [29, 34, 22, 27, 19]
print("Lista final ordenada:", ordenamiento_burbuja(edades))
