#les 4 fonctions principales
def AddRoundKey():
def SubBytes():
def ShiftRows():
def MixColumns():


#cette fonction découpe le message en bloc de 16 octets. Si le message est plus court ou si le dernier bloc fait moins de 16 octets, on remplace ce qu'il manque par des epaces, 20 en hexadécimal.
def decoupage_bloc():

#cette fonction transforme le texte en hexadécimal.
def text_en_hexa():

#cette fonction transforme l'hexadécimalen binaire.
def hexa_en_bin():

#cette fonction transforme le binaire en hexadécimal.
def bin_en_hexa():

#cette fonction applique l'opération xor en 2 ou 3 éléments
def xor():


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