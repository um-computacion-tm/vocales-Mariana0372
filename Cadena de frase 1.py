

def obtener_vocales(frase):
    vocales="AEIOU"

    return set([c for c in frase if c in vocales])


texto= input("ingresa la frase:")

print(obtener_vocales(texto))
print(len(obtener_vocales(texto)))


