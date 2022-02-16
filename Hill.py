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
#fonctions d'algebre de base utiles dans le chiffrement de hill

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

#pgcd calcul de plus grand commun diviseur

def pgcd(a,b):
    while b!=0:
            a,b=b,a%b
    return a

#multiplication calcule le produit d'une matrice par un vecteur %26
def multiplication(m1,m2):
    n = len(m1)
    m = len(m2)
    l = []
    i = 0
    s = 0 
    while i < n:
        j = 0
        while j < m  :
            s = s +m1[i][j]*m2[j]
            j = j + 1
        l = l + [s%26]
        s =0
        i = i + 1
    return l

#######################################################################################################################################################################

def decouper(texte,m):
    len_cle = len(m)
    len_texte = len(texte)
    l=[]
    j = 0
    i = 0
    ch =[]
    while (j<len_texte) :
        if(texte[j] != ' '):
            if (i == len_cle):
                l=l+[ch]
                ch = []
                i = 0
            ch.append(rang(texte[j]))
            i = i + 1
        j = j + 1
    l=l+[ch]
    return l

#generer matrice identite renvoie la matrice identite n*n
def generer_matrice_identite(n):
    l = []
    i = 0
    while i < n :
        tmp = [0]*n
        tmp[i] = 1
        l = l +[tmp]
        i = i + 1
    return l



#inversion renvoie la matrice inverse de A apres les changements de gauss et ceci modulo 29

def inversion(A):
    M = generer_matrice_identite(len(A))
    #la premiere partie renvoie la matrice A et M apres les transformations de gauss
    # qui transforme la matrice en matrice triangulaire inferieur
    signe = 1
    d = 1
    p = 1
    j = 0
    while j < (len(A)-1):
        k = j
        while (k < len(A)) and (A[k][j] == 0):
            k = k + 1
        if (k != j):
            A[k],A[j] = A[j], A[k]
            M[k],M[j] = M[j], M[k]
            signe = -signe
        d = d * A[j][j]
        for k in range(j+1,len(A)):
            p = p * A[j][j]
            s = A[k][j]
            for c in range(0,len(A)):
                A[k][c]=A[k][c]*A[j][j]-A[j][c]*s
                M[k][c]=M[k][c]*M[j][j]-M[j][c]*s
        j = j + 1
    #la deuxieme partie renvoie la matrice A et M apres les transformations de gauss
    # qui transforme la matrice en matrice triangulaire superieur
    signe = 1
    d = 1
    p = 1
    j = len(A) - 1
    while (j >= 0) :
        d = d * A[j][j]
        k = j - 1
        while(k >= 0):
            p = p * A[j][j]
            s = A[k][j]
            c = len(A) - 1
            while(c>=0):
                A[k][c]=(A[k][c]*A[j][j]-A[j][c]*s)%29
                M[k][c]=(M[k][c]*M[j][j]-M[j][c]*s)%29
                c = c - 1
            k = k -1
        j = j - 1
    i = 0
    while(i<len(A)):
        A[len(A)-1][i] = A[len(A)-1][i] % 29
        M[len(M)-1][i] = M[len(M)-1][i] % 29
        i = i + 1
        liste =[]
    n = 0
    x = 1
    liste = []
    while(n<len(A)):
        x = x * A[n][n]
        liste = liste+[A[n][n]]      
        n = n + 1
    j = 0
    while (j < len(liste)):
        i = 0
        while ( i < len(liste)):
            A[j][j] = (A[j][j]*liste[i])
            M[j][j] = (M[j][j]*liste[i])
            i = i + 1
        A[j][j]=(A[j][j]/(liste[j]*x))%29
        M[j][j]=(M[j][j]/(liste[j]*x))%29
        j = j + 1 
    return A,M

#######################################################################################################################################################################
def Chiffrement_Hill(texte,m):
    l = decouper(texte,m)
    print(l)
    i = 0
    mat=[]
    while(i<len(l)):
        mat = mat + [multiplication(m,l[i])]
        i = i + 1
    ch = ''
    j = 0
    while(j<len(mat)):
        k = 0
        while(k<len(mat[j])):
            ch=ch+lettre(mat[j][k])
            k = k + 1
        j = j + 1        
    return ch



def dehiffrement_Hill(texte,m):
    m = inversion(m)
    l = decouper(texte,m)
    i = 0
    mat=[]
    while(i<len(l)):
        mat = mat + [multiplication(m,l[i])]
        i = i + 1
    ch = ''
    j = 0
    mat = transformer_int(mat)
    while(j<len(mat)):
        k = 0
        while(k<len(mat[j])):
            ch=ch+lettre(mat[j][k])
            k = k + 1
        j = j + 1        
    return ch
print(inversion([[19,6,13],[5,14,2],[10,9,1]]))
#print(Dechiffrement_Hill('rjhcbrqgkjzsiummntxknnqajjklgu',[[19,6,13],[5,14,2],[10,9,1]]))

#######################################################################################################################################################################

def cryptanalyse(texte,m,c,n):
    m=transpose(m)
    print(m)

    m = modMatInv(m,n)
    m = transformer_int(m)
    print(m)
    c=transpose(c)
    print(c)
    mat = multiplication_mod_n(m,c,n)
    print(mat)
    ch = Chiffrement_Hill(texte,mat)
    return ch


























    
