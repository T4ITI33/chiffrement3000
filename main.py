import hashlib
import copy

# S-box de l'AES
#             00    01    02    03    04    05    06    07    08    09    0A    0B    0C    0D    0E    0F
# S-box AES standard
Sbox = [
    '63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76',
    'ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0',
    'b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15',
    '04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75',
    '09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84',
    '53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf',
    'd0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8',
    '51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2',
    'cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73',
    '60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db',
    'e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79',
    'e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08',
    'ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a',
    '70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e',
    'e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df',
    '8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16'
]

RCON = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36', '6c', 'd8', 'ab', '4d', '9a']

matrice_mixColumns = [
      [0x02, 0x03, 0x01, 0x01],
      [0x01, 0x02, 0x03, 0x01],
      [0x01, 0x01, 0x02, 0x03],
      [0x03, 0x01, 0x01, 0x02]
   ]

def print_en_matrice(texte):
    """affiche une matrice"""
    for matrice in texte:
        for ligne in matrice:
            print(ligne)
        print("\n")

""" les 4 fonctions principales """


def AddRoundKey128(matrice_phrase, matrice_cle): 
    phrase = copy.deepcopy(matrice_phrase)
    for i in range(0,4 ):
        for j in range(0,4):
            phrase[i][j] = xor(matrice_phrase[i][j], matrice_cle[i][j])
    return phrase

def KeyExpansion(key_hex, key_size_bits):
    """Génère toutes les clés de tour en AES pour des clés 128, 192 ou 256 bits"""
    
    print("test",key_hex)
    if key_size_bits == 128:
        Nk = 4
        Nr = 10
    elif key_size_bits == 192:
        Nk = 6
        Nr = 12
    elif key_size_bits == 256:
        Nk = 8
        Nr = 14
    else:
        raise ValueError("Invalid key length. Expected 16, 24, or 32 bytes.")

    Nb = 4  
    w = []

    # Initial key schedule
    for i in range(Nk):
        w.append(key_hex[4*i:4*i+4])

    for i in range(Nk, Nb * (Nr + 1)):
        temp = w[i - 1]
        if i % Nk == 0:
            temp = SubWord(RotWord(temp))
            temp[0] = format(int(temp[0], 16) ^ int(RCON[i // Nk - 1], 16), '02x')
        elif Nk > 6 and i % Nk == 4:
            temp = SubWord(temp)
        w.append(xor_words(w[i - Nk], temp))

    return w



# SubWord applies Sbox to each byte
def SubWord(word):
    return [Sbox[int(b, 16)] for b in word]

# RotWord rotates word left by one byte
def RotWord(word):
    return word[1:] + word[:1]

# XOR between two words
def xor_words(w1, w2):
    return [format(int(a, 16) ^ int(b, 16), '02x') for a, b in zip(w1, w2)]




def SubBytes(state):
    for i in range(4):
        for j in range(4):
            byte = state[i][j]
            row = int(byte[0], 16)
            col = int(byte[1], 16) 
            # print( byte , row , col)
            state[i][j] = format(S_BOX[row][col], '02x')
    return state


def ShiftRows(state):
    for i in range(1, 4): 
        # print( state[i][i:])
        # print(state[i][:i])
        state[i] = state[i][i:] + state[i][:i]
    return state

def galois_multiplication(a, b):
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        high_bit_set = a & 0x80
        a = (a << 1) & 0xFF
        if high_bit_set:
            a ^= 0x1B  # x^8 + x^4 + x^3 + x + 1
        b >>= 1
    return result

def MixColumns(state):
    new_state = [[None]*4 for _ in range(4)]
    for j in range(4):
        col = [int(state[i][j], 16) for i in range(4)]
        new_state[0][j] = format(galois_multiplication(0x02, col[0]) ^ galois_multiplication(0x03, col[1]) ^ col[2] ^ col[3], '02x')
        new_state[1][j] = format(col[0] ^ galois_multiplication(0x02, col[1]) ^ galois_multiplication(0x03, col[2]) ^ col[3], '02x')
        new_state[2][j] = format(col[0] ^ col[1] ^ galois_multiplication(0x02, col[2]) ^ galois_multiplication(0x03, col[3]), '02x')
        new_state[3][j] = format(galois_multiplication(0x03, col[0]) ^ col[1] ^ col[2] ^ galois_multiplication(0x02, col[3]), '02x')
    return new_state





"""
cette fonction découpe le message en matrice de taille 4x4. 
Chaque case correspond à un caractère. Si il manque des caractère dans la dernière matrice, on ajoute des espaces, 20 en hexadécimal.
la fonction retourne une liste de matrices
"""
def texte_en_matrice(phrase, taille_bloc=16):

    if len(phrase) % taille_bloc != 0:
        phrase = phrase.ljust((len(phrase) // taille_bloc + 1) * taille_bloc)
    blocs = [phrase[i:i+taille_bloc] for i in range(0, len(phrase), taille_bloc)]
    liste_matrices = []
    for bloc in blocs:
        matrice = [[bloc[i + j*4] for i in range(4)] for j in range(4)]
        liste_matrices.append(matrice)
    return liste_matrices


""" pareil mais pour la clé """
def cle_en_matrice(phrase, taille_bloc=32):

    if len(phrase) % taille_bloc != 0:
        phrase = phrase.ljust((len(phrase) // taille_bloc + 1) * taille_bloc)
    blocs = [phrase[i:i+taille_bloc] for i in range(0, len(phrase), taille_bloc)]
    liste_matrices = []
    for bloc in blocs:
        matrice = [[bloc[(i*8) + (j*2):(i*8) + (j*2) + 2] for j in range(4)] for i in range(4)]
        liste_matrices.append(matrice)
    return liste_matrices





""" cette fonction transforme chaque caractere d'une matrice en hexadécimal. """
def matrice_en_hexa(text):
    hex_matrice = [[format(ord(char), '02x') for char in row] for row in text]
    return hex_matrice

""" cette fonction appel matrice_en_hexa pour chaque matrice d'un texte """
def texte_en_hexa(texte):
    hexadecimal = [] 
    for matrice in texte:
        hexadecimal.append(matrice_en_hexa(matrice)) 
    return hexadecimal



""" cette fonction applique l'opération xor entre 2 caractère en hexadécimal """
def xor(phrase, cle):
    resultat = int(phrase, 16) ^ int(cle, 16) # Convertie les caractere hexadécimals en entiers et effectue le XOR
    return format(resultat, f'0{len(phrase)}x') # Formate le résultat en hexadécimal



""" cette fonction retourne le hash de 128 bits pour la clé en utilisant MD5 """
def hash_128bit(cle):
    hash_object = hashlib.md5(cle.encode()) # on met dans 'hash_object' le hash en MD5 de la clé
    return hash_object.hexdigest() # on retourne le résultat en hexadécimal



""" cette fonction retourne le hash de 192 bits pour la clé en tronquant SHA-384 """
def hash_192bit(password):
    hash_object = hashlib.sha384(password.encode()) # on met dans 'hash_object' le hash en SHA-384 de la clé
    return hash_object.hexdigest()[:48]  # on retourne le résultat en hexadécimal en enlevant 48 caractères 



""" cette fonction retourne le hash de 256 bits pour la clé en utilisant SHA-256 """
def hash_256bit(password):
    hash_object = hashlib.sha256(password.encode()) # on met dans 'hash_object' le hash en SHA-256 de la clé
    return hash_object.hexdigest() # on retourne le résultat en hexadécimal 



"""
#fonction de chiffrement, c'est la fonction principale 
- on commence par prendre le hash de la clé en fonction de la taille demandé
- ensuite on le met en matrice (1 matrice 4x4 pour une clé 128bits)
- on met le texte en matrice
- ensuite on le transforme en hexadécimal
- on peut appliquer l'algorithme c'est à dire
    - addRoundKey(cle)
    - pendant x tour:
        - subBytes
        - shiftRows
        - mixColumns
        - addRoundKey(roundKey)
    - puis dernier tous sans mixColumns
-on affiche le texte chiffré
"""

def chiffrement(texte_en_clair, cle, taille_cle):
    cyper_text = []
    """ on hash la clé en fonction de la taille souhaité """
    """ pour la clé il faut d'abord la transformer en hexa avec la fonction de hash puis la mettre en matrice avec cle_en_matrice() """
    if taille_cle == 128:
        cle_hash = hash_128bit(cle)
        cle_hash = '00000000000000000000000000000000'   #test
        key_bytes = [cle_hash[i:i+2] for i in range(0, len(cle_hash), 2)]
        print("test",key_bytes)
        print("taille de la clé: 128 bits")
        nb_tour = 10
        round_keys = KeyExpansion(key_bytes, 128)
    elif taille_cle == 192:
        cle_hash = hash_192bit(cle)
        cle_hash = '00000000000000000000000000000000'   #test
        key_bytes = [cle_hash[i:i+2] for i in range(0, len(cle_hash), 2)]
        print("taille de la clé: 192 bits")
        nb_tour = 12
        round_keys = KeyExpansion(key_bytes, 192)
    elif taille_cle == 256:
        cle_hash = hash_256bit(cle)
        cle_hash = '00000000000000000000000000000000'   #test
        key_bytes = [cle_hash[i:i+2] for i in range(0, len(cle_hash), 2)]
        print("taille de la clé: 256 bits")
        nb_tour = 14
        round_keys = KeyExpansion(key_bytes, 256)
    else:
        print("pas la bonne taille pour la clé")
        return 0
    
   
    print("Clé hashé:\n",cle_hash)
    cle_hash = cle_en_matrice(cle_hash)
    print("\nClé en matrice:")
    print_en_matrice(cle_hash)
    print("cle étendue:")
    print(round_keys)
 


    """ pour le texte il faut d'abord le mettre en matrice avec texte_en_matrice() puis le transformer en hexa avec texte_en_hexa()"""
    print("Texte normal:\n",texte_en_clair)

    texte_matrice = texte_en_matrice(texte_en_clair) 
    print("\nTexte en matrice:")
    print_en_matrice(texte_matrice)

    hexadecimal = texte_en_hexa(texte_matrice)
    print("Texte en hexadécimal:\n")
    print_en_matrice(hexadecimal)

    #hexadecimal correspond au texte en hexa en matrice
    
    for current_matrice in hexadecimal:
        print("----------------------------------------")
        print("current matrice")
        print(current_matrice)
        print("cle", cle_hash)
        current_matrice = AddRoundKey128(current_matrice, round_keys[0])
        print("apres addRoundKey")
        print(current_matrice)
        
        for i in range(1,nb_tour):
            current_matrice = SubBytes(current_matrice)
            print("apres SubBytes", current_matrice)
            current_matrice = ShiftRows(current_matrice)
            print("apres shiftRows", current_matrice)
            current_matrice = MixColumns(current_matrice)
            print("apres MixColumns", current_matrice)
            current_matrice = AddRoundKey128(current_matrice, round_keys[i])
            print("apres AddRoundKey", current_matrice)

        # Dernier tour sans MixColumns
        current_matrice = SubBytes(current_matrice)
        print("apres SubBytes", current_matrice)
        current_matrice = ShiftRows(current_matrice)
        print("apres shiftRows", current_matrice)
        current_matrice = AddRoundKey128(current_matrice, round_keys[nb_tour])
        print("apres AddRoundKey", current_matrice)   
        cyper_text.append(current_matrice)

    return cyper_text



#fonction de déchiffrement
def déchiffrement(text_chiffré, clé,taille):
    # return text_dechiffre   
    return 0


def main():
    texte_a_chiffrer = "Bonjour AES test!"
    cle_secrete = "cleAES128bittest"
    test = chiffrement(texte_a_chiffrer, cle_secrete, 128)
    print("\nTexte d'origine:", texte_a_chiffrer)
    print("Clé secrète:", cle_secrete)
    print("\nTexte chiffré:")
    print(test)


if __name__ == "__main__":
    main()