print (" ")
print (" Ordonez Martinez Valeria")
print (" ")

def contar_princesas(clasicas, modernas, /, *, princesas_adicionales=0):
    total_princesas = clasicas + modernas + princesas_adicionales
    print("Total de princesas de Disney: ", total_princesas)


contar_princesas(5, 3, princesas_adicionales=2)

