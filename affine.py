#######################################################################################################################################################################

#rang renvoie le rang de la lettre en parametre dans l'ensemble {0..26}-->{a..z}
def rang(c):
    x = ord(c)-97
    return x

#lettre renvoie la lettre correspondante au rang de l'ensemble {0..26}-->{a..z}
def lettre(n):
    c = chr(n+97)
    return c

#inverse calcul l'inverse d'un entier a modulo p

def inverse(a,p) :
    u = 1
    v = 0
    u1 = 0
    v1 = 1
    r = 1
    x = p
    while ( a > 1 ) :
        q = p // a
        r = p % a
        p = a
        a = r
        s = u - u1*q
        u = u1
        u1 = s
        t = v -v1*q
        v = v1
        v1 = t
    return v1 % x

#######################################################################################################################################################################

def chiffrement_affine(ch,a,b):
    chaine=''
    i = 0
    while( i < len(ch)):
        if (ch[i] != ' ' ):
            x = (a*(rang(ch[i]))+b)%26
            y = lettre(x)
            chaine = chaine + str(y)
        else :
            chaine = chaine +' ' 
        i = i + 1
    return chaine


def dechiffrement_affine(ch,a,b):
    chaine = ''
    a = inverse(a,26)
    print(a)
    i = 0
    while (i< len(ch)):
        if (ch[i] != ' '):
            x = a*((rang(ch[i]))-b)%26
            y = lettre(x)
            chaine = chaine + str(y)
        else :
            chaine = chaine +' ' 
        i = i + 1
    return chaine

print(dechiffrement_affine('un texte a chiffrer',5,1))


    
