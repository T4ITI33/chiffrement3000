import hashlib
import copy


def hexa_to_text(hex_string):
    return bytes.fromhex(hex_string).decode('latin-1')


""" cette fonction retourne le hash de 128 bits pour la clé en utilisant MD5 """
def hash_128bit(cle):
    hash_object = hashlib.md5(cle.encode()) # on met dans 'hash_object' le hash en MD5 de la clé
    return hash_object.hexdigest() # on retourne le résultat en hexadécimal

def KeyExpansion(key_hex, key_size_bits):
    """Génère toutes les clés de tour en AES pour des clés 128, 192 ou 256 bits"""
    
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


# S-box de l'AES
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

inv_sbox = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d,
]

RCON = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36', '6c', 'd8', 'ab', '4d', '9a']


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

def print_en_matrice(texte):
    """affiche une matrice"""
    for matrice in texte:
        for ligne in matrice:
            print(ligne)
        print("\n")



def AddRoundKey128(matrice_phrase, matrice_cle):
    phrase = copy.deepcopy(matrice_phrase)
    for i in range(0,4 ):
        for j in range(0,4):
            phrase[i][j] = xor(matrice_phrase[i][j], matrice_cle[i][j])
    return phrase


""" cette fonction applique l'opération xor entre 2 caractère en hexadécimal """
def xor(phrase, cle):
    resultat = int(phrase, 16) ^ int(cle, 16) # Convertie les caractere hexadécimals en entiers et effectue le XOR
    return format(resultat, f'0{len(phrase)}x') # Formate le résultat en hexadécimal


def texte_en_matrice(phrase, taille_bloc=32):
    # Complète avec des espaces si le texte n'est pas un multiple de la taille du bloc
    if len(phrase) % taille_bloc != 0:
        phrase = phrase.ljust((len(phrase) // taille_bloc + 1) * taille_bloc)

    blocs = [phrase[i:i+taille_bloc] for i in range(0, len(phrase), taille_bloc)]
    liste_matrices = []

    for bloc in blocs:
        # Regroupe le texte en paires de caractères
        paires = [bloc[i:i+2] for i in range(0, len(bloc), 2)]
        # Construit une matrice 4x4 colonne par colonne
        matrice = [[paires[i + j*4] for i in range(4)] for j in range(4)]
        liste_matrices.append(matrice)

    return liste_matrices

def InvSubBytes(state):
    return [[format(inv_sbox[int(byte, 16)], '02x') for byte in row] for row in state]


def inv_shift_rows(state):
    return [
        state[0],
        state[1][-1:] + state[1][:-1],
        state[2][-2:] + state[2][:-2],
        state[3][-3:] + state[3][:-3],
    ]

def InvShiftRows(state):
    state[0][0] = state[0][0]  # inchangé
    tmp1 = state[3][1]
    state[3][1] = state[2][1]
    state[2][1] = state[1][1]
    state[1][1] = state[0][1]
    state[0][1] = tmp1

    tmp2 = state[2][2]
    state[2][2] = state[0][2]
    state[0][2] = tmp2
    tmp3 = state[3][2]
    state[3][2] = state[1][2]
    state[1][2] = tmp3

    tmp4 = state[1][3]
    state[1][3] = state[2][3]
    state[2][3] = state[3][3]
    state[3][3] = state[0][3]
    state[0][3] = tmp4

    return state


def galois_multiplication(x):
    return ((x << 1) ^ 0x1b) & 0xFF if (x & 0x80) else (x << 1) & 0xFF

def multiply(a, b):
    """Multiplication dans GF(2^8)"""
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        a = galois_multiplication(a)
        b >>= 1
    return result & 0xFF

def InvMixColumns(matrix):
    # Aplatir la matrice en une liste d'entiers
    state = [int(cell, 16) for row in matrix for cell in row]

    for i in range(4):
        idx = i * 4
        a = state[idx]
        b = state[idx + 1]
        c = state[idx + 2]
        d = state[idx + 3]

        state[idx]     = multiply(a, 0x0e) ^ multiply(b, 0x0b) ^ multiply(c, 0x0d) ^ multiply(d, 0x09)
        state[idx + 1] = multiply(a, 0x09) ^ multiply(b, 0x0e) ^ multiply(c, 0x0b) ^ multiply(d, 0x0d)
        state[idx + 2] = multiply(a, 0x0d) ^ multiply(b, 0x09) ^ multiply(c, 0x0e) ^ multiply(d, 0x0b)
        state[idx + 3] = multiply(a, 0x0b) ^ multiply(b, 0x0d) ^ multiply(c, 0x09) ^ multiply(d, 0x0e)

    # Reformater en matrice 4x4 de chaînes hexadécimales
    new_matrix = [[f'{state[row * 4 + col]:02x}' for col in range(4)] for row in range(4)]
    return new_matrix


def matrice_to_hexa(blocks):
    # Concatène tous les hex en une seule liste plate
    flat_hex = [byte for block in blocks for row in block for byte in row]
    
    # Rejoint tous les hex en une seule chaîne
    return ''.join(flat_hex)



#fonction de déchiffrement
def déchiffrement(text_chiffre, cle,taille_cle):
    plain_text = []

    if taille_cle == 128:
        cle_hash = hash_128bit(cle)
        # cle_hash = "00000000000000000000000000000000" #test
        key_bytes = [cle_hash[i:i+2] for i in range(0, len(cle_hash), 2)]
        print("taille de la clé: 128 bits")
        nb_tour = 10
        round_keys = KeyExpansion(key_bytes, 128)
    elif taille_cle == 192:
        cle_hash = hash_192bit(cle)
        key_bytes = [cle_hash[i:i+2] for i in range(0, len(cle_hash), 2)]
        print("taille de la clé: 192 bits")
        nb_tour = 12
        round_keys = KeyExpansion(key_bytes, 192)
    elif taille_cle == 256:
        cle_hash = hash_256bit(cle)
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


    print("\nTexte chiffré:", text_chiffre)

    text_chiffre = texte_en_matrice(text_chiffre,32)
    print("\nTexte en matrice:")
    print_en_matrice(text_chiffre)

    for current_matrice in text_chiffre:
        print("matriche initiale:")
        print(current_matrice)
        text_chiffre = AddRoundKey128(current_matrice, round_keys[nb_tour * 4 : (nb_tour + 1) * 4])
        print("\nAprès AddRoundKey:", text_chiffre)

        for i in range(nb_tour - 1, 0, -1):
            print("\nTour:", i + 1)
            text_chiffre = InvShiftRows(text_chiffre)
            # print("\nAprès InvShiftRows:", text_chiffre) #test
            text_chiffre = InvSubBytes(text_chiffre) 
            # print("\nAprès InvSubBytes:", text_chiffre) #test
            text_chiffre = AddRoundKey128(text_chiffre, round_keys[i * 4 : (i + 1) * 4])
            # print("\nAprès AddRoundKey:", text_chiffre) #test
            text_chiffre = InvMixColumns(text_chiffre)
            # print("\nAprès InvMixColumns:", text_chiffre) #test 
        
        print("\nTour: 1")
        text_chiffre = InvShiftRows(text_chiffre)
        text_chiffre = InvSubBytes(text_chiffre)
        text_chiffre = AddRoundKey128(text_chiffre, round_keys[0:4])
        plain_text.append(text_chiffre)

    return plain_text



def main():
 
    test = "75a6e3decd98969eefcdd922cc3469755d2ee3f1b9a04158c5206201d339b4f9ad0fb517be9837ddf274e4da7c1b5b78"
    cle_secrete = "cle128bittest"
    # Déchiffrement
    texte_dechiffre = déchiffrement(test, cle_secrete, 128)
    texte_dechiffre = matrice_to_hexa(texte_dechiffre)
    texte_dechiffre = hexa_to_text(texte_dechiffre)
    print("\nTexte déchiffré:")
    print(texte_dechiffre)


if __name__ == "__main__":
    main()