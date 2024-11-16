#les 4 fonctions principales
def AddRoundKey():
def SubBytes():
def ShiftRows():
def MixColumns():


#cette fonction découpe le message en matrice de taille 4x4. Chaque case correspond à un caractère. Si il manque des caractère dans la derniere matrice on ajoute des espace. 20 en hexadécimal
#la fonction retourne une liste de matrices
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



#cette fonction transforme chaque caractere d'une matrice en hexadécimal.
def text_en_hex(text):
    hex_matrix = [[format(ord(char), '02x') for char in row] for row in text]
    return hex_matrix




#cette fonction transforme chaque hexadécimal d'une matrice en binaire.
def hex_matrix_to_binary(hex_matrix):
    binary_matrix = [[format(int(hex_code, 16), '08b') for hex_code in row] for row in hex_matrix]
    return binary_matrix



#cette fonction transforme chaque binaire d'une matrice en hexadécimal.
def binary_matrix_to_hex(binary_matrix):
    hex_matrix = [[format(int(binary_code, 2), '02x') for binary_code in row] for row in binary_matrix]
    return hex_matrix

#cette fonction applique l'opération xor en 2 ou 3 éléments
def xor(phrase,cle_secret):
    texte1=texte_en_bin(phrase)
    texte2=texte_en_bin(cle_secret)
    combine=""
    if len(texte1)>len(texte2):       
        for bit in range(len(texte2)):
            if texte1[bit]==texte2[bit]:
                combine=combine+"0"
            else:
                combine=combine+"1"
        return combine+texte1[len(texte2):]
    elif len(texte2)>len(texte1):
        for bit in range(len(texte1)):
            if texte1[bit]==texte2[bit]:
                combine=combine+"0"
            else:
                combine=combine+"1"
        return combine+texte2[len(texte1):]
    for bit in range(len(texte1)):
        print(texte1[bit],texte2[bit])
        if texte1[bit]==texte2[bit]:
            combine=combine+"0"
        else:
            combine=combine+"1"
    return combine




#fonction de chiffrement
def chiffrement(texte_en_clair, clé):


    

    AddRoundKey(clé):

    #x dépend de la taille de la clé
    for x tours:
        SubBytes():
        ShiftRows():
        MixColumns():
        AddRoundKey(RoundKey):
    fin for

    SubBytes():
    ShiftRows():
    AddRoundKey(LastRoundKey):


return text_chiffre




#fonction de déchiffrement
def déchiffrement(text_chiffré, clé):

return text_dechiffre


