#######################################################################################################################################################################

#rang renvoie le rang de la lettre en parametre dans l'ensemble {0..26}-->{a..z}
def rang(c):
    x = ord(c)-97
    return x

#lettre renvoie la lettre correspondante au rang de l'ensemble {0..26}-->{a..z}
def lettre(n):
    c = chr(n+97)
    return c


#######################################################################################################################################################################

#dans cette partie nous effectuons le chiffrement et le dechiffrement selon le code de cesar
def chiffrement_cesar(ch,n):
    chaine=''
    i = 0
    while( i < len(ch)):
        if (ch[i] != ' ' ):
            x = (rang(ch[i])+n)%26
            y = lettre(x)
            chaine = chaine + str(y)
        else :
            chaine = chaine +' ' 
        i = i + 1
    return chaine

def dechiffrement_cesar(ch,n):
    chaine = ''
    i = 0
    while (i< len(ch)):
        if (ch[i] != ' '):
            x = (rang(ch[i])-n)%26
            y = lettre(x)
            chaine = chaine + str(y)
        else :
            chaine = chaine +' ' 
        i = i + 1
    return chaine

def determiner_cle(clair,chiffré) :
    cl = rang(clair[0])
    ch = rang(chiffré[0])
    cle = (ch - cl)%26
    return cle


#######################################################################################################################################################################

#lettre_plus_frequente renvoie la lettre la plus frequente dans une chaine de caractere
def lettre_plus_frequente(ch):
    dico = {}
    for l in ch.lower():
        dico[l] = ch.count(l)
    for l, occurrence in dico.items():
        if occurrence == max(dico.values()):
            return l
            
def analyse_frequentielle_cesar(ch,c):
    plus_frequente = lettre_plus_frequente(ch)
    x = rang(plus_frequente)
    y = rang(c)
    z = x - y
    return dechiffrement_cesar(ch,z)

def determiner_cle_frequentielle(ch,c):
    plus_frequente = lettre_plus_frequente(ch)
    x = rang(plus_frequente)
    y = rang(c)
    z = x - y
    return z
    

#######################################################################################################################################################################
#voici quelques exemples pour tester le bon fontionnement de l'algorithme de l'analyse frequentielle
print(analyse_frequentielle_cesar('fypgztefcpgpylteolcctgpcopwlfecpnzepopwlmlcctpcpfypapcdzyypdzcetefyxtwteltcptwpeltenzxxpolydwpdqtwxdoprfpccpapydlolgtowpdopnzcletzydcpxawtddltpyewlglyeopdlgpdeptwdlaacznslopwlgztefcpzfdpeczfglteolgtowpnslfqqpfczfgctewlqpypecp','e'))
#print(analyse_frequentielle_cesar('hjhnjxyzsywjxgjfzyjcyj','e'))
