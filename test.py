def print_en_matrice(texte):
    """affiche une matrice"""
    for matrice in texte:
        for ligne in matrice:
            print(ligne)
        print("\n")



""" cette fonction applique l'opération xor entre 2 caractère en hexadécimal """
def xor(phrase, cle):
    resultat = int(phrase, 16) ^ int(cle, 16) # Convertie les caractere hexadécimals en entiers et effectue le XOR
    return format(resultat, f'0{len(phrase)}x') # Formate le résultat en hexadécimal

def AddRoundKey128(matrice_phrase, matrice_cle): 
    phrase = matrice_phrase
    print(phrase)
    for i in range(0,4 ):
        for j in range(0,4):
            phrase[i][j] = xor(matrice_phrase[i][j], matrice_cle[i][j])
    return phrase


text =[   ['56', '6f', '69', '63'],
                ['69', '20', '75', '6e'],
                ['20', '65', '78', '65'],
                ['6d', '70', '6c', '65']]



texte =[    [   ['56', '6f', '69', '63'],
                ['69', '20', '75', '6e'],
                ['20', '65', '78', '65'],
                ['6d', '70', '6c', '65']],

            [   ['20', '64', '65', '20'],
                ['74', '65', '78', '74'],
                ['65', '20', 'e0', '20'],
                ['63', '68', '69', '66']],  


            [   ['66', '72', '65', '72'],
                ['2e', '20', '20', '20'],
                ['20', '20', '20', '20'],
                ['20', '20', '20', '20']]]

cle =[  ['a0', 'ea', '25', 'f1'],
        ['e5', 'a8', 'b0', 'bc'],
        ['0c', '79', '92', '60'],
        ['d2', '27', '1f', '42']]

resultat = AddRoundKey128(text, cle)

print(resultat)

# print(xor('a0', 'ea'))  # Exemple d'utilisation de la fonction xor