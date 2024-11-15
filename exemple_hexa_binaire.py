

def decoupe_en_matrices(phrase, taille_bloc=16):
    # Étape 1 : Compléter le texte pour qu'il soit un multiple de 16
    if len(phrase) % taille_bloc != 0:
        phrase = phrase.ljust((len(phrase) // taille_bloc + 1) * taille_bloc)
    
    # Étape 2 : Découper la phrase en blocs de 16 caractères
    blocs = [phrase[i:i+taille_bloc] for i in range(0, len(phrase), taille_bloc)]
    
    # Étape 3 : Convertir chaque bloc en une matrice 4x4
    matrices = []
    for bloc in blocs:
        matrice = [[bloc[i + j*4] for i in range(4)] for j in range(4)]
        matrices.append(matrice)
    
    return matrices


def text_en_hex(text):
    hex_matrix = [[format(ord(char), '02x') for char in row] for row in text]
    return hex_matrix




def hex_matrix_to_binary(hex_matrix):
    binary_matrix = [[format(int(hex_code, 16), '08b') for hex_code in row] for row in hex_matrix]
    return binary_matrix



def binary_matrix_to_hex(binary_matrix):
    hex_matrix = [[format(int(binary_code, 2), '02x') for binary_code in row] for row in binary_matrix]
    return hex_matrix




phrase = "Voici un exemple de phrase à chiffrer."
print(phrase)
#découpe la phrace en matrice
matrices = decoupe_en_matrices(phrase)

#transforme le texte des matrices en hexadécimal
hex_matrice= []
for matrice in matrices:
    hex_matrice.append(text_en_hex(matrice))

print("hexadécimal de la phrase")
for matrice in hex_matrice:
    for ligne in matrice:
        print(ligne)
    print('')

#transforme l'hexadécimal des matrice en binaire
binary_matrice = []
for matrice in hex_matrice:
    binary_matrice.append(hex_matrix_to_binary(matrice))

print("binaire de la phrase")
for matrice in binary_matrice:
    for ligne in matrice:
        print(ligne)
    print('')


hex_matrice2 = []
for matrice in binary_matrice:
    hex_matrice2.append(binary_matrix_to_hex(matrice))

print("retour à l'hexadecimal")
for matrice in hex_matrice2:
    for ligne in matrice:
        print(ligne)
    print('')

