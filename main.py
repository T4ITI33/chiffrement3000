#les 4 fonctions principales
def AddRoundKey():
def SubBytes():
def ShiftRows():
def MixColumns():


#cette fonction découpe le message en bloc de 16 octets. Si le message est plus court ou si le dernier bloc fait moins de 16 octets, on remplace ce qu'il manque par des epaces, 20 en hexadécimal.
def decoupe_en_blocs(phrase, taille_bloc=16):
    # Découper la phrase en blocs de taille_bloc
    blocs = [phrase[i:i+taille_bloc] for i in range(0, len(phrase), taille_bloc)]
    # Compléter le dernier bloc avec des espaces si nécessaire
    if len(blocs[-1]) < taille_bloc:
        blocs[-1] = blocs[-1].ljust(taille_bloc)
    return blocs

#cette fonction transforme le texte en hexadécimal.
def text_en_hex(text):
    return ''.join(format(ord(char), '02X') for char in text)



#cette fonction transforme l'hexadécimalen binaire.
def hexa_en_bin():

#cette fonction transforme le binaire en hexadécimal.
def bin_en_hexa():

#cette fonction applique l'opération xor en 2 ou 3 éléments
def xor():


#fonction de chiffrement
def chiffrement(texte_en_clair, clé):

    phrase="Voici un exemple de texte à chiffrer."
    phrase_decoupe = decoupe_en_blocs(phrase)
    print(phrase_decoupe)
    for i in phrase_decoupe:
        resultat = text_en_hex(i)
        print(resultat)


    
    def taille_clé():

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

#fonction de déchiffrement
def déchiffrement(text_chiffré, clé):



