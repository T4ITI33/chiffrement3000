phrase = [['56', '6f', '69', '63'],
['69', '20', '75', '6e'],
['20', '65', '78', '65'],
['6d', '70', '6c', '65']]



def xor(phrase, cle):
    # Convertir les chaînes hexadecimal en entiers, effectuer le XOR, puis reconvertir en hexadécimal
    resultat = int(phrase, 16) ^ int(cle, 16)
    # Formater le résultat en hexadécimal
    return format(resultat, f'0{len(phrase)}x')



# Exemple d'utilisation

cle = ['20', '63', '68', '69']

for ligne in phrase:
    for i in range(len(ligne)-1):
        ligne[i] = xor(ligne[i], cle[i])
    print(ligne)