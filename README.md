# Chiffrement3000
Code pour algo de chiffrement du projet tuteuré

Par **PRESLE-JONC Thibault** et **WANG Alex**

## Projet tuteuré
Ce projet s'incrit dans le cadre de notre cours projet tuteuré. Nous avons pour objectif de réaliser un projet tout au long de l'année pour le présenter devant un jury en fin d'année.



## Sujet:
Développer algo de chiffrement de chiffrement symétrique(AES) et le tester.
Possiblement ajouter signature électronique et stéganographie.

## Objectif final idéal:
Envoyer un message chiffré, signé électroniquement et caché.



## Fonctionnement du ciffreùent AES

Le chiffrement AES s'eefectue en plusieur tours. Ces tours sont déterminés par la taille de la clé de ciffrement.
* 128 bit : 10 tours
* 192 bit : 12 tours
* 256 bit : 14 tours

A chaque tour on applique on applique des transformations au texte. Il y a 4 étapes à réaliser à chaque tours.
Il y a aussi une sous-clé qui est généré à chaque tours(10 tours = 10 clés) et utilisé pour réaliser les transformations.

Ces sous-clés appelés **Round Keys** sont obtenues grâce à un processus de dérivation de clé **Key expansion**.

Le chiffrement AES fonctionne en bloc de 16 octets, ce qui veut dire que texte est découpé et réparti dans des matrice de 16 octets.


### 1.AddRoundKey

On ajoute la **RoundKey** (la clé du tour actuel) au texte.

### 2.SubBytes

Chaque octets est remplacé par un autre en utilisant la S-Box.

### 3.ShiftRows

Les lignes sont décalés vers la gauche.

### 4.MixCollums

Les colonnes sont transformées pour mélanger les octets.
