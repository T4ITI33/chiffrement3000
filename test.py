def xtime(x):
    return ((x << 1) ^ 0x1b) & 0xFF if (x & 0x80) else (x << 1) & 0xFF

def mix_columns(state):
    for i in range(4):
        idx = i * 4
        a = state[idx]
        b = state[idx + 1]
        c = state[idx + 2]
        d = state[idx + 3]

        state[idx]     = xtime(a) ^ xtime(b) ^ b ^ c ^ d
        state[idx + 1] = a ^ xtime(b) ^ xtime(c) ^ c ^ d
        state[idx + 2] = a ^ b ^ xtime(c) ^ xtime(d) ^ d
        state[idx + 3] = xtime(a) ^ a ^ b ^ c ^ xtime(d)
    return state

# Entrée hexadécimale sous forme de matrice
matrice = [
    ['63', '7b', 'c0', 'd2'],
    ['7b', '76', 'd2', '7c'],
    ['76', '75', '7c', 'c5'],
    ['75', '63', 'c5', 'c0']
]

# Aplatir la matrice et convertir en entiers
flat_state = [int(cell, 16) for row in matrice for cell in row]

# Appliquer MixColumns
result = mix_columns(flat_state)

# Afficher le résultat en hexadécimal
print(''.join(f'{x:02x}' for x in result))
