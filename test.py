def print_en_matrice(texte):
    """affiche une matrice"""
    for matrice in texte:
        for ligne in matrice:
            print(ligne)
        print("\n")


def matrice_en_hexa(text):
    hex_matrice = [[format(ord(char), '02x') for char in row] for row in text]
    return hex_matrice


def texte_en_hexa(texte):
    hexadecimal = [] 
    for matrice in texte:
        hexadecimal.append(matrice_en_hexa(matrice)) 
    return hexadecimal


texte =[[['V', 'o', 'i', 'c'], ['i', ' ', 'u', 'n'], [' ', 'e', 'x', 'e'], ['m', 'p', 'l', 'e']], [[' ', 'd', 'e', ' '], ['t', 'e', 'x', 't'], ['e', ' ', 'à', ' '], ['c', 'h', 'i', 'f']], [['f', 'r', 'e', 'r'], ['.', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]]

hexa_texte = texte_en_hexa(texte)

print_en_matrice(hexa_texte)