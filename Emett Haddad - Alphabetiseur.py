# Alphabetiseur 1.0
# Createur Emett Haddad
NB_LETTRES = 30
MAX_L = 6

def lire_alphabet():
    fichier_alphabet = open("alphabet 1.0.txt", "r")
    alphabet = fichier_alphabet.read()
    fichier_alphabet.close()
    return alphabet


def traitement_alphabet(alphabet):
    alphabet = alphabet.split("\n")
    liste = [lettre for lettre in alphabet[1]]
    (alphabet, new_alphabet, n) = (alphabet[2:], [], 0)
    MAX_LIGNE =  max(map(len,alphabet))
    
    for i in range(NB_LETTRES):
        new_alphabet.append([])
        N, max_ligne = n, 0
        while alphabet[N][0]!="-":
            max_ligne = max(max_ligne,len(alphabet[N]))
            N+=1
        nb_ligne= N-n
        for _ in range(MAX_L - nb_ligne):
            new_alphabet[i].append("".join([" " for _ in range(max_ligne)]))
        while alphabet[n][0]!="-":
            ligne = alphabet[n]
            ligne += "".join([" " for _ in range(max_ligne - len(ligne))])
            new_alphabet[i].append(ligne)
            n+=1
        n+=1
    return new_alphabet, MAX_LIGNE, liste

def fonction_lettre(lettre,liste, alphabet):
    index_lettre = liste.index(lettre)
    LETTRE = alphabet[index_lettre]
    return LETTRE
    
def main():
    alphabet = lire_alphabet()
    alphabet, max_ligne,liste = traitement_alphabet(alphabet)
    texte = input()
    liste_texte = []
    for lettre in texte:
        if lettre in liste:
            liste_texte.append(lettre)
    TEXTE = [["" for _ in range(len(liste_texte))] for _ in range(MAX_L)]
    for n,lettre in enumerate(liste_texte):
        LETTRE = fonction_lettre(lettre,liste, alphabet)
        for i,LIGNE_TEXTE in enumerate(LETTRE):
            TEXTE[i][n] = LIGNE_TEXTE
    for l in TEXTE:
        for i in l:
            print(i, end="")
        print()
while 1:
    main()
