import hashlib


""" les 4 fonctions principales """
def AddRoundKey():
def SubBytes():
def ShiftRows():
def MixColumns():



"""
cette fonction découpe le message en matrice de taille 4x4. 
Chaque case correspond à un caractère. Si il manque des caractère dans la dernière matrice, on ajoute des espaces, 20 en hexadécimal.
la fonction retourne une liste de matrices
"""
def decoupe_en_matrices(phrase, taille_bloc=16):
    """ Étape 1 : Compléter le texte pour qu'il soit un multiple de 16 """
    if len(phrase) % taille_bloc != 0:
        phrase = phrase.ljust((len(phrase) // taille_bloc + 1) * taille_bloc)
    
    """ Étape 2 : Découper la phrase en blocs de 16 caractères """
    blocs = [phrase[i:i+taille_bloc] for i in range(0, len(phrase), taille_bloc)]
    
    """ Étape 3 : Convertir chaque bloc en une matrice 4x4 """
    matrices = []
    for bloc in blocs:
        matrice = [[bloc[i + j*4] for i in range(4)] for j in range(4)]
        matrices.append(matrice)
    
    return matrices



""" cette fonction transforme chaque caractere d'une matrice en hexadécimal. """
def text_en_hex(text):
    hex_matrix = [[format(ord(char), '02x') for char in row] for row in text]
    return hex_matrix



#cette fonction transforme chaque hexadécimal d'une matrice en binaire.
#plus nécessaire
def hex_matrix_to_binary(hex_matrix):
    binary_matrix = [[format(int(hex_code, 16), '08b') for hex_code in row] for row in hex_matrix]
    return binary_matrix



#cette fonction transforme chaque binaire d'une matrice en hexadécimal.
#plus nécessaire
def binary_matrix_to_hex(binary_matrix):
    hex_matrix = [[format(int(binary_code, 2), '02x') for binary_code in row] for row in binary_matrix]
    return hex_matrix



""" cette fonction applique l'opération xor en 2 caractère en hexadécimal """
def xor(phrase, cle):
    resultat = int(phrase, 16) ^ int(cle, 16) # Convertie les caractere hexadécimals en entiers et effectue le XOR
    return format(resultat, f'0{len(phrase)}x') # Formate le résultat en hexadécimal



""" cette fonction retourne le hash de 128 bits pour la clé en utilisant MD5 """
def hash_128bit(cle):
    hash_object = hashlib.md5(cle.encode()) # on met dans 'hash_object' le hash en MD de la clé
    return hash_object.hexdigest() # on retourne le résultat en hexadécimal



""" cette fonction retourne le hash de 192 bits pour la clé en tronquant SHA-384 """
def hash_192bit(password: str) -> str:
    hash_object = hashlib.sha384(password.encode()) # on met dans 'hash_object' le hash en SHA-384 de la clé
    return hash_object.hexdigest()[:48]  # on retourne le resultat en hexadécimal en enlevant 48 caractères 



""" fonction de chiffrement, c'est la fonction principale """
def chiffrement(texte_en_clair, cle, taille):

    msg = decoupe_en_matrices(texte_en_clair) # dans la variable 'msg' il y a le texte découpé en matrice 4x4

    hexadecimal = [] # dans la variable 'hexadecimal' on va mettre les matrice avec l'hexadécimal
    for matrice in msg: # on parcourt les matrice de 'msg'
        hexadecimal.append(text_en_hex(matrice)) # on la transforme en hexadécimal et on l'ajoute à 'hexadecimal'
    


    #ici il doit y avoir la partie concernant la clé
    #il faut faire en sorte que celle ci soit de taille 128bit, 192bit ou 256bit en fonction de la demande de l'utilisateur
    #on pourrait avoir un mdp qui est rentré, puis on prend le hash de celui-ci avec la taille demandé
    #par exemple, si on veut un clé de 128bit on peut prendre du MD5 ou bien si on veut 256bit on peut prendre du SHA256


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
def déchiffrement(text_chiffré, clé,taille):

return text_dechiffre