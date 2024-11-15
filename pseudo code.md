```#les 4 fonctions principales
    fonction AddRoundKey():
    fonction SubBytes():
    fonction ShiftRows():
    fonction MixColumns():


#cette fonction découpe le message en bloc de 16 octets. Si le message est plus court ou si le dernier bloc fait moins de 16 octets, on remplace ce qu'il manque par des epaces, 20 en hexadécimal.
fonction decoupage_bloc():

#cette fonction transforme le texte en hexadécimal.
fonction text_en_hexa():

#cette conftion transforme l'hexadécimalen binaire.
fonction hexa_en_bin():

#cette fonction transforme le binaire en hexadécimal.
fonction bin_en_hexa():

#cette fonction applique l'opération xor en 2 ou 3 éléments
fonction xor():


#fonction de chiffrement
fonction chiffrement(texte_en_clair, clé):
    
    fonction taille_clé():

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
fonction déchiffrement(text_chiffré, clé):
```