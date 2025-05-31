def blocks_to_text(blocks):
    # Concatène tous les hex en une seule liste plate
    flat_hex = [byte for block in blocks for row in block for byte in row]
    
    # Convertit chaque hex en entier, puis crée des bytes
    byte_array = bytes(int(h, 16) for h in flat_hex)

    # Décode en UTF-8 en ignorant les erreurs non imprimables
    try:
        return byte_array.decode('utf-8')
    except UnicodeDecodeError:
        # Si certains caractères ne sont pas UTF-8 valides, affiche en latin-1
        return byte_array.decode('latin-1', errors='replace')
def blocks_to_hex_string(blocks):
    # Concatène tous les hex en une seule liste plate
    flat_hex = [byte for block in blocks for row in block for byte in row]
    
    # Rejoint tous les hex en une seule chaîne
    return ''.join(flat_hex)



text_chiffre = [[['75', 'a6', 'e3', 'de'], ['cd', '98', '96', '9e'], ['ef', 'cd', 'd9', '22'], ['cc', '34', '69', '75']], [['5d', '2e', 'e3', 'f1'], ['b9', 'a0', '41', '58'], ['c5', '20', '62', '01'], ['d3', '39', 'b4', 'f9']], [['ad', '0f', 'b5', '17'], ['be', '98', '37', 'dd'], ['f2', '74', 'e4', 'da'], ['7c', '1b', '5b', '78']]]

test = blocks_to_hex_string(text_chiffre)
print(test)