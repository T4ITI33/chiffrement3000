def galois_multiplication(x):
    return ((x << 1) ^ 0x1b) & 0xFF if (x & 0x80) else (x << 1) & 0xFF

def mixColumns(matrix):
    # Aplatir la matrice en une liste d'entiers
    state = [int(cell, 16) for row in matrix for cell in row]

    for i in range(4):
        idx = i * 4
        a = state[idx]
        b = state[idx + 1]
        c = state[idx + 2]
        d = state[idx + 3]

        state[idx]     = galois_multiplication(a) ^ galois_multiplication(b) ^ b ^ c ^ d
        state[idx + 1] = a ^ galois_multiplication(b) ^ galois_multiplication(c) ^ c ^ d
        state[idx + 2] = a ^ b ^ galois_multiplication(c) ^ galois_multiplication(d) ^ d
        state[idx + 3] = galois_multiplication(a) ^ a ^ b ^ c ^ galois_multiplication(d)

    # Reformater en matrice 4x4 de chaînes hexadécimales
    new_matrix = [[f'{state[row * 4 + col]:02x}' for col in range(4)] for row in range(4)]
    return new_matrix

input_matrix = [
    ['63', '7b', 'c0', 'd2'],
    ['7b', '76', 'd2', '7c'],
    ['76', '75', '7c', 'c5'],
    ['75', '63', 'c5', 'c0']
]

result_matrix = mixColumns(input_matrix)

print(result_matrix)
