

texto = input("ingresa una frase: ")
vocales = "AEIOU"
j = 0
for i in texto:
    if i in vocales:
        j = j + 1

print(f"la frase tiene {j} vocales")
