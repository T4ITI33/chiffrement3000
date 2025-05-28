def galois_multiplication(a, b):
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1b
        a &= 0xFF
        b >>= 1
    return result


def MixColumns(state):
    for j in range(4):
        s0 = int(state[0][j], 16)
        s1 = int(state[1][j], 16)
        s2 = int(state[2][j], 16)
        s3 = int(state[3][j], 16)

        t0 = galois_multiplication(0x02, s0) ^ galois_multiplication(0x03, s1) ^ s2 ^ s3
        t1 = s0 ^ galois_multiplication(0x02, s1) ^ galois_multiplication(0x03, s2) ^ s3
        t2 = s0 ^ s1 ^ galois_multiplication(0x02, s2) ^ galois_multiplication(0x03, s3)
        t3 = galois_multiplication(0x03, s0) ^ s1 ^ s2 ^ galois_multiplication(0x02, s3)

        state[0][j] = format(t0, '02x')
        state[1][j] = format(t1, '02x')
        state[2][j] = format(t2, '02x')
        state[3][j] = format(t3, '02x')

    return state



matrice = [
    ['db', '13', '53', '45'],
    ['f2', '0a', '22', '5c'],
    ['01', '01', '01', '01'],
    ['c6', 'c6', 'c6', 'c6']
]
attendu = [["59","1c","ee","a1"],["c2","86","36","d1"],["ca","dd","af","02"],["4a","27","dc","a2"]]

result = MixColumns(matrice)
print(result)

