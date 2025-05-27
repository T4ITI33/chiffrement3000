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
    for j in range(4):  # Pour chaque colonne
        for i in range(4):  # Pour chaque ligne
            new_state[i][j] = format(
                galois_multiplication(0x02, int(state[0][j], 16)) ^
                galois_multiplication(0x03, int(state[1][j], 16)) ^
                int(state[2][j], 16) ^
                int(state[3][j], 16)
                if i == 0 else
                galois_multiplication(0x01, int(state[0][j], 16)) ^
                galois_multiplication(0x02, int(state[1][j], 16)) ^
                galois_multiplication(0x03, int(state[2][j], 16)) ^
                int(state[3][j], 16)
                if i == 1 else
                galois_multiplication(0x01, int(state[0][j], 16)) ^
                galois_multiplication(0x01, int(state[1][j], 16)) ^
                galois_multiplication(0x02, int(state[2][j], 16)) ^
                galois_multiplication(0x03, int(state[3][j], 16))
                if i == 2 else
                galois_multiplication(0x03, int(state[0][j], 16)) ^
                galois_multiplication(0x01, int(state[1][j], 16)) ^
                galois_multiplication(0x01, int(state[2][j], 16)) ^
                galois_multiplication(0x02, int(state[3][j], 16)),'02x'
            )
    return new_state

matrice_test = [
    ['87', 'f2', '4d', '97'],
    ['6e', '4c', '90', 'ec'],
    ['46', 'e7', '4a', 'c3'],
    ['a6', '8c', 'd8', '95']
]



resultat = MixColumns(matrice_test)
print("Résultat de MixColumns:")
print(resultat)