#les 4 fonctions principales
def AddRoundKey():
def SubBytes():
def ShiftRows():
def MixColumns():


#cette fonction découpe le message en bloc de 16 octets. Si le message est plus court ou si le dernier bloc fait moins de 16 octets, on remplace ce qu'il manque par des epaces, 20 en hexadécimal.
def decoupe_en_blocs(text, taille_bloc=16):
    # Découper la phrase en blocs de taille_bloc
    blocs = [text[i:i+taille_bloc] for i in range(0, len(text), taille_bloc)]
    # Compléter le dernier bloc avec des espaces si nécessaire
    if len(blocs[-1]) < taille_bloc:
        blocs[-1] = blocs[-1].ljust(taille_bloc)
    return blocs

#cette fonction transforme le texte en hexadécimal.
def text_en_hex(text):
    return ''.join(format(ord(char), '02X') for char in text)


#cette fonction transforme l'hexadécimalen binaire.
def hexa_en_bin(chiffre):
    binaire=""
    while chiffre!=0:
        binaire=str(chiffre%2)+binaire
        chiffre=chiffre//2
    while len(binaire)<8:
        binaire="0"+binaire
    return binaire

#cette fonction transforme le binaire en hexadécimal.
def bin_en_hexa():

#cette fonction applique l'opération xor en 2 ou 3 éléments
def xor(phrase,cle_secret):
    texte1=texte_en_bin(phrase)
    texte2=texte_en_bin(cle_secret)
    combine=""
    if len(texte1)>len(texte2):       
        for bit in range(len(texte2)):
            if texte1[bit]==texte2[bit]:
                combine=combine+"0"
            else:
                combine=combine+"1"
        return combine+texte1[len(texte2):]
    elif len(texte2)>len(texte1):
        for bit in range(len(texte1)):
            if texte1[bit]==texte2[bit]:
                combine=combine+"0"
            else:
                combine=combine+"1"
        return combine+texte2[len(texte1):]
    for bit in range(len(texte1)):
        print(texte1[bit],texte2[bit])
        if texte1[bit]==texte2[bit]:
            combine=combine+"0"
        else:
            combine=combine+"1"
    return combine

#fonction de chiffrement
def chiffrement(texte_en_clair, clé):


    
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



