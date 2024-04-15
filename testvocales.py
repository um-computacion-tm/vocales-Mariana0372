import unittest


# def contar_vocales(mi_string):
#     resultado = {}
#     for letra in mi_string:
#         if letra == 'A':
#             if 'A' not in resultado:
#                 resultado['A'] = 0
#             resultado['A'] = resultado['A'] + 1
#         if letra == 'E':
#             if 'E' not in resultado:
#                 resultado['E'] = 0
#             resultado['E'] = resultado['E'] + 1
#     return resultado

def contar_vocales(mi_string):
    vocales = ('A', 'E', 'I', 'O', 'U')
    resultado = {}
    for letra in mi_string:
        # if letra in 'AEIOU':
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('ZZZ')
        self.assertEqual(resultado, {})

    def test_contar_a(self):
        resultado = contar_vocales('cAs')
        self.assertEqual(resultado, {'A': 1})

    def test_contar_aa(self):
        resultado = contar_vocales('cAsA')
        self.assertEqual(resultado, {'A': 2})

    def test_contar_bese(self):
        resultado = contar_vocales('bEsE')
        self.assertEqual(resultado, {'E': 2})

    def test_contar_besa(self):
        resultado = contar_vocales('bEsA')
        self.assertEqual(resultado, {'A': 1, 'E': 1})

    def test_contar_casanova(self):
        resultado = contar_vocales('cAsAnOvA')
        self.assertEqual(resultado, {'A': 3, 'O': 1})

    def test_contar_mUrciElago(self):
        resultado = contar_vocales('mUrciElago')
        self.assertEqual(resultado, {'U': 1, 'E': 1})
    
    def test_contar_mUrciElago(self):
        resultado = contar_vocales('holAA')
        self.assertEqual(resultado, {'A': 2})

unittest.main()

# while(True):
#     palabra = input('Ingrese palabra: ')
#     print(contar_vocales(palabra))





