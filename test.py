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

# Rcon AES standard (max needed for AES-256)
Rcon = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36', '6c', 'd8', 'ab', '4d', '9a']

# SubWord applies Sbox to each byte
def SubWord(word):
    return [Sbox[int(b, 16)] for b in word]

# RotWord rotates word left by one byte
def RotWord(word):
    return word[1:] + word[:1]

# XOR between two words
def xor_words(w1, w2):
    return [format(int(a, 16) ^ int(b, 16), '02x') for a, b in zip(w1, w2)]

# Main Key Expansion function
def KeyExpansion(key, size):
    print("test",key)
    if size == 128:
        Nk = 4
        Nr = 10
    elif size == 192:
        Nk = 6
        Nr = 12
    elif size == 256:
        Nk = 8
        Nr = 14
    else:
        raise ValueError("Invalid key length. Expected 16, 24, or 32 bytes.")

    Nb = 4
    w = []
    print("test",w)
    # Initial key schedule
    for i in range(Nk):
        w.append(key[4*i:4*i+4])

    print("test",w)
    print("test1111",Nk, Nb, Nr)
    for i in range(Nk, Nb * (Nr + 1)):
        temp = w[i - 1]
        print("test2222",temp)
        if i % Nk == 0:
            temp = SubWord(RotWord(temp))
            print("test3333",temp)
            temp[0] = format(int(temp[0], 16) ^ int(Rcon[i // Nk - 1], 16), '02x')
        elif Nk > 6 and i % Nk == 4:
            temp = SubWord(temp)
        w.append(xor_words(w[i - Nk], temp))

    return w



cle_hash = '00000000000000000000000000000000'  # AES-128
key_bytes = [cle_hash[i:i+2] for i in range(0, len(cle_hash), 2)]
round_keys = KeyExpansion(key_bytes, 128)

# Affichage des clés de chaque round
for i in range(0, len(round_keys), 4):
    round_key = round_keys[i:i+4]
    print(f"Round {i//4}: {''.join(sum(round_key, []))}")
