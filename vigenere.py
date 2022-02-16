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

#chaine_v renvoie le sous-texte chiffre en vigenere
def chaine_v(chaine,cle):
    i = 0
    ch=''
    while(i<len(chaine)):
        ch = ch + lettre((rang(chaine[i])+rang(cle[i]))%26)
        i = i + 1
    return ch

#chaine_v_d renvoie le sous-texte dechiffre en vigenere
def chaine_v_d(chaine,cle):
    i = 0
    ch=''
    while(i<len(chaine)and i< len(cle)):
        ch = ch + lettre((rang(chaine[i])-rang(cle[i]))%26)
        i = i + 1
    return ch

#######################################################################################################################################################################
def decouper(texte,cle):
    len_cle = len(cle)
    len_texte = len(texte)
    l=[]
    j = 0
    i = 0
    ch =''
    while (j<len_texte) :
        if(texte[j] != ' '):
            if (i == len_cle):
                l=l+[ch]
                ch = ''
                i = 0
            ch=ch+texte[j]
            i = i + 1
        j = j + 1
    l = l +[ch]
    return l

#chiffrement_vigenere chiffre le message selon vigenere et la cle donnée en parametre
def chiffrement_vigenere(texte,cle):
    l = decouper(texte,cle)
    i = 0
    ch='';
    while(i<len(l)):
        ch=ch+chaine_v(l[i],cle)+' '
        i = i + 1
    return ch



#dechiffrement_vigenere dechiffre le message selon vigenere et la cle donnée en parametre
def dechiffrement_vigenere(texte,cle):
    l = decouper(texte,cle)
    i = 0
    ch='';
    while(i<len(l)):
        ch=ch+chaine_v_d(l[i],cle)
        i = i + 1
    return ch

######################################################################################################################################################################

#decouper_avec_dico decoupe le texte et ceci en utilisant un dictionnaire
def decouper_avec_dico(texte,n):
    dico = {}
    dic = {}
    i = 0
    tmp = ''
    while(i<len(texte)):
        t = texte[i:i+n]
        if (t in dico) :
            dico[t] = dico[t]+[i]
            dic[t] = dic[t]+1
        else:
            dico[t] = [i]
            dic[t] = 1
        i = i + 1
    liste = []
    nb = []
    s = max(dic.values())
    for k,v in dico.items():
        if len(v) == s :
            liste = liste +[k]
            nb = nb + [dico[k]]
    return liste[0],nb[0]

#lettre_plus_frequente renvoie la lettre la plus frequente dans une chaine de caractere
def lettre_plus_frequente(ch):
    dico = {}
    for l in ch.lower():
        dico[l] = ch.count(l)
    for l, occurrence in dico.items():
        if occurrence == max(dico.values()):
            return l

#######################################################################################################################################################################

#calcul du pgcd de deux entiers
def pgcd1(a,b) :
    while b != 0 :
        r = a % b
        a,b=b,r
    return a

#calcul du pgcd d'une suite d'entiers
def pgcd_liste(l):
    pg = pgcd1(l[0],l[1])
    i = 2
    while(i<len(l)) :
        pg = pgcd1(pg,l[i])
        i = i + 1
    return pg

#calcul de la distance entre les positions
def distance(l):
    s = []
    i = len(l)-1
    x= 1
    while(i>0):
        j = len(l)-1-x
        while(j>=0):
            s = s +[l[i]-l[j]]
            j = j -1
        x = x + 1
        i = i - 1
    return s

#######################################################################################################################################################################

#dans cette partie nous rappelons le code de cesar qu'on utilisera apres
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

def analyse_frequentielle(ch,c):
    plus_frequente = lettre_plus_frequente(ch)
    x = rang(plus_frequente)
    y = rang(c)
    z = x - y
    return dechiffrement_cesar(ch,z)

######################################################################################################################################################################

#enfin la cryptanalyse de vigenere

def cryptanalyse(texte,n,c):
    position_cle = (decouper_avec_dico(texte,n))[1]
    dist = pgcd_liste(distance(position_cle))
    l=[]
    k = 0
    ch=''
    cryp=[]
    x = 0
    j = 0
    i = 0
    while(j < dist):
        i = j
        while(i<len(texte)):
            ch=ch+texte[i]
            i = i + dist
        l = l +[ch]
        ch=''
        j = j + 1
    s = []
    for el in l :
        s = s +[analyse_frequentielle(el,c)]
    chaine=''
    i = 0
    while(i<len(s[len(s)-1])):
        j = 0
        while(j<len(s)):
            chaine=chaine+s[j][i]
            j = j + 1
        i = i + 1
    return chaine

def cle_cryptanalyse(clair,n,c):
    chiffré = cryptanalyse(clair,n,c)
    position_cle = (decouper_avec_dico(clair,n))[1]
    dist = pgcd_liste(distance(position_cle))
    i = 0
    cle = ''
    while(i<dist):
        cle = cle +lettre((rang(chiffré[i])-rang(clair[i]))%26)
        i = i + 1
    return cle

    
#voici quelques exemples qu'on peut tester prouvant que la cryptanalyse marche bien

#print(cryptanalyse('tseuweepniigwvlkanwbzrnidbdruemiuaggcbtxvkwlwqayvekmgvvtnfnijsdmaednhvzummwgtegmtmbmsgmbwpzrsdwvtbpxvvjqteepqvkiymsoepeilbicaloavqfvlavtnfnijgsdwlsnpwrzgqjiaenitseuwmovgxdiemuxqhkijxhmmmegtigpmasmrbeivrsgsgtccvcisdwvtbwwcikzsrefgxksmadxsgqruyklwlcnotjhwkggcrpxielqggaiggcivmjgirtgfvhalkeowgyefbvxsnhjiimawlfvnijhwvmbtrvfismqdeaefiejavlhmogwfyktwlceqwjikinxcygwyyabeblygjiefksbsruulmfmkhngrejvwdwguruhvwtiygefczvgdivxrakiiixmefezqvkiszsoeaufiyushhueczfmjlggnrcwzpwidnnqgweslzwleavvvenmueecgygpwvwweyqqsvwmlwifreiysdwveyniesknjxrruhrrktgkdeghvpsvmbtpqqdiewjtngneeradwksnkvvhwtseiogvrxawfweccvzwbmvbsnkwvggclxcruszvbmmgefuiuiewfialupvwutgvhruhrrfqnxrfcmiiicaloapiisfbuhmzggvpdmkwiyaehysbgkzrcrjtmqklefvytilbwyovupvwwvlxnqtivpdmkooavwfrfmjiohtxfmdpgfmniiuemrgnrqjyzrsxhxlygulidmuaaavulmnikxlrxiiqsqfmeacrkgwkztngfijtszlbsnpwhywrsbeaviehmumkmhtiigguexuaelrrllwvozrpzgabwiuvutjedugwirthrrktwurbwmcpszvwefxsjkwawmlruffmklsesneididmsncektvvvcvxszqyksfavxsgcffvkymtnqnijfshghknuhvggzjxzrczrruiaxngcprvwvuhngtiuikkztrffiiyfalxdgneegwavxnbwzvemkggtegwkvsathueiitsmbwtuwqyihzcacehpijwwlwyrnpgvgwymbfhvtfyjvgnsyggyefbvnmnnlvyjkwltycqrvupwyuagfiivmkveafvvwicwoovemrggbwwepgpciklwvaepskenmueefuschsbkweycrzmvmuxlygwuinqumoejyxssdwvlruqzwwzsulruhvgwtdxsqgnryjmkoevnpvikxsklnlyjxakwjurnpvwjmhhsrpxrzwkdxuensekuwjmetghfqtzwldrhmxyjmwlahlslvvpmbjrwrvwkmhnifuijxmxwgsrtetilpgfmresdqwbmtuecmjehxjhcugxvweiagsqgwrtscnkescgvmfngkmrfyuijvaxrwqyihwawllrxvvwicagaicmvrlxslpntpvgwrgnrycicpwmltignimmkiyxdrnewvsvux',3,'e'))
#print(cryptanalyse('cyttprimnwcnshbrvgxtqcrhgaeucrvuomayewfppnpeiuoirutebtrjmqiecediawnpttcqwfpqjmpspyenmfepnixwbqopmquvqgomwyrrhlmyfntnftflghgdpnpeiuyssnweolmxygiqfzjlgwnpwuucmgcwxiaxrzywfntnftflghgdrtnrwrcmxyfwwcpjpvjfptzcfpcnlfnqiepxyyfeezgmyrxuzryjyyuavtwuiuoiquqiezquifmvtssgnmuaewzbmutprygpgyiexrhcywjnfeofwjxnzqtvzhwswcizxrwkoijmnyudmlyamcwixoaixzmyoeixprfcghccvnprvfppfogvgnsyyqinlfflemgcizhrtgcwthaiuzvycgypxmqcgekcinfrxctxhizqgoesmyiuqmqgfhgryjleirprxuqexthqyfhgnswugmqywwyztntwxuvipepfpnrvoixuiiueinfferavtwuefppfpbmvfvjihwgevtoiekehfpvhnpgmuhjhpywihzttxqusippxwypinlvjmfiompfcgewikwifstomsugiwcwvorhcgmiuieketzpbmtoesmqiuqmqgfhgdgnyaggqmhnvspmifopswahjjrxkeixfhqkpvjmvrftuzuvipeuzcyivlmyyajqygycbrcwegufiwyixiexgoevonvkfqfpnmvpxjcawvlpqygsweeznbytniwnnmppqjhgpgdcxnrqgoiwysvqthnmfioprywnvfpwgoypgdqthgekprymnrunixmrttpyaydygwiforxctxjhrfwwpnnvspdszxnmpoeacqvgdxfvbyesigyryppztckgcgiwhryupwtlgmgoixypvcywtoiiplmyxrwcqjnwuitwirigttppzxrpcdgjhfiwchjgnvtlxtogwgfpfjeiubyjfntqcxjmrwqtxkyeqgpmqxrwepriuvxkwrfleivlmyjnwfphjmpipovjjhmutpxuevgeejhsmpweuiexgdszpemvpxiuimfpyyfnwvftjoehgdeacrhggesnyykdiiycpqjennhrezqufrbgtrkieqcemvoryppznhtxctrjxrtgcwthaiudiiycpcnenyaxffruifxglpfogvgciluehcyxfoceudelyyiupgwuawipesnfqwcezrfmvfixuhjqyhiyyeulpqyvpalzfcgfkprzhrgkyuzuaxctrjxbvftrfnrytdgnhdiecesmticyxxygwkeyjyaxtppjmrgtlrxarepewjnyiuzvicaevpywmhrgxehbvrgcmjczttpwxcbrplryyyeunismrytoiruevcesznfiwweulrwsfiqucsteixyfskejjlzigtpiyfggyhfcgmnyewlrxctxuufhgoixwrrfciuovwkwwfleivliszvrnlttlgiuzyalvxgehfpvhgfxqufxwaizlqiulznyqixlryfhmuphjjysalmyoagqxtqykikyjtlzevtuzyhrggmsagekyiiycitdsshrwuphjjyeelmjhghwyttmgicwezneitpkflqepeezjnwulkjfrwgnvfhfkglrymzytlycmvxwpwfosspohjfnwcwpjcyccgennomgyysypmpbyfhgekyiiiehkyeyyhvunmskrgtlrxarepewjnfmvfijhgvgwixypvcywlynrvdiyfrwqchnhnxgfvxoaiolgmcaittingcvgdwniarcyxj',3,'e'))
print(cryptanalyse('rawiabenamiraamiraamiraamiraamiradivbrdiv',3,'e'))
#print(cryptanalyse('pbcjbjcrgwisiixrbrgxwquplcptgfiaeeamcftxqbnvisiyceteadxxfqwxgbsvnrzhkyjoeoxrqpckwrbummquvbskmcbwrngfijenxxqrgwyjeuledeeeefrrxyqswbzxnvlemoubxfopweksexpriebiqrgkijpntgbertvaeueiqttxwaihyioepmipcqgxoakkijepmernurwqeoxhbcjbjcrgfiktohrlanilxbgmmnugvsjmgeizhkyjoefxgbsckurinnxflklizerxraapmglmoxglmrhwxnvnraeetpxgg',3,'e'))
#print(cle_cryptanalyse('cyttprimnwcnshbrvgxtqcrhgaeucrvuomayewfppnpeiuoirutebtrjmqiecediawnpttcqwfpqjmpspyenmfepnixwbqopmquvqgomwyrrhlmyfntnftflghgdpnpeiuyssnweolmxygiqfzjlgwnpwuucmgcwxiaxrzywfntnftflghgdrtnrwrcmxyfwwcpjpvjfptzcfpcnlfnqiepxyyfeezgmyrxuzryjyyuavtwuiuoiquqiezquifmvtssgnmuaewzbmutprygpgyiexrhcywjnfeofwjxnzqtvzhwswcizxrwkoijmnyudmlyamcwixoaixzmyoeixprfcghccvnprvfppfogvgnsyyqinlfflemgcizhrtgcwthaiuzvycgypxmqcgekcinfrxctxhizqgoesmyiuqmqgfhgryjleirprxuqexthqyfhgnswugmqywwyztntwxuvipepfpnrvoixuiiueinfferavtwuefppfpbmvfvjihwgevtoiekehfpvhnpgmuhjhpywihzttxqusippxwypinlvjmfiompfcgewikwifstomsugiwcwvorhcgmiuieketzpbmtoesmqiuqmqgfhgdgnyaggqmhnvspmifopswahjjrxkeixfhqkpvjmvrftuzuvipeuzcyivlmyyajqygycbrcwegufiwyixiexgoevonvkfqfpnmvpxjcawvlpqygsweeznbytniwnnmppqjhgpgdcxnrqgoiwysvqthnmfioprywnvfpwgoypgdqthgekprymnrunixmrttpyaydygwiforxctxjhrfwwpnnvspdszxnmpoeacqvgdxfvbyesigyryppztckgcgiwhryupwtlgmgoixypvcywtoiiplmyxrwcqjnwuitwirigttppzxrpcdgjhfiwchjgnvtlxtogwgfpfjeiubyjfntqcxjmrwqtxkyeqgpmqxrwepriuvxkwrfleivlmyjnwfphjmpipovjjhmutpxuevgeejhsmpweuiexgdszpemvpxiuimfpyyfnwvftjoehgdeacrhggesnyykdiiycpqjennhrezqufrbgtrkieqcemvoryppznhtxctrjxrtgcwthaiudiiycpcnenyaxffruifxglpfogvgciluehcyxfoceudelyyiupgwuawipesnfqwcezrfmvfixuhjqyhiyyeulpqyvpalzfcgfkprzhrgkyuzuaxctrjxbvftrfnrytdgnhdiecesmticyxxygwkeyjyaxtppjmrgtlrxarepewjnyiuzvicaevpywmhrgxehbvrgcmjczttpwxcbrplryyyeunismrytoiruevcesznfiwweulrwsfiqucsteixyfskejjlzigtpiyfggyhfcgmnyewlrxctxuufhgoixwrrfciuovwkwwfleivliszvrnlttlgiuzyalvxgehfpvhgfxqufxwaizlqiulznyqixlryfhmuphjjysalmyoagqxtqykikyjtlzevtuzyhrggmsagekyiiycitdsshrwuphjjyeelmjhghwyttmgicwezneitpkflqepeezjnwulkjfrwgnvfhfkglrymzytlycmvxwpwfosspohjfnwcwpjcyccgennomgyysypmpbyfhgekyiiiehkyeyyhvunmskrgtlrxarepewjnfmvfijhgvgwixypvcywlynrvdiyfrwqchnhnxgfvxoaiolgmcaittingcvgdwniarcyxj',3,'e'))
#print(chiffrement_vigenere('tseuweepniigwvlkanwbzrnidbdruemiuaggcbtxvkwlwqayvekmgvvtnfnijsdmaednhvzummwgtegmtmbmsgmbwpzrsdwvtbpxvvjqteepqvkiymsoepeilbicaloavqfvlavtnfnijgsdwlsnpwrzgqjiaenitseuwmovgxdiemuxqhkijxhmmmegtigpmasmrbeivrsgsgtccvcisdwvtbwwcikzsrefgxksmadxsgqruyklwlcnotjhwkggcrpxielqggaiggcivmjgirtgfvhalkeowgyefbvxsnhjiimawlfvnijhwvmbtrvfismqdeaefiejavlhmogwfyktwlceqwjikinxcygwyyabeblygjiefksbsruulmfmkhngrejvwdwguruhvwtiygefczvgdivxrakiiixmefezqvkiszsoeaufiyushhueczfmjlggnrcwzpwidnnqgweslzwleavvvenmueecgygpwvwweyqqsvwmlwifreiysdwveyniesknjxrruhrrktgkdeghvpsvmbtpqqdiewjtngneeradwksnkvvhwtseiogvrxawfweccvzwbmvbsnkwvggclxcruszvbmmgefuiuiewfialupvwutgvhruhrrfqnxrfcmiiicaloapiisfbuhmzggvpdmkwiyaehysbgkzrcrjtmqklefvytilbwyovupvwwvlxnqtivpdmkooavwfrfmjiohtxfmdpgfmniiuemrgnrqjyzrsxhxlygulidmuaaavulmnikxlrxiiqsqfmeacrkgwkztngfijtszlbsnpwhywrsbeaviehmumkmhtiigguexuaelrrllwvozrpzgabwiuvutjedugwirthrrktwurbwmcpszvwefxsjkwawmlruffmklsesneididmsncektvvvcvxszqyksfavxsgcffvkymtnqnijfshghknuhvggzjxzrczrruiaxngcprvwvuhngtiuikkztrffiiyfalxdgneegwavxnbwzvemkggtegwkvsathueiitsmbwtuwqyihzcacehpijwwlwyrnpgvgwymbfhvtfyjvgnsyggyefbvnmnnlvyjkwltycqrvupwyuagfiivmkveafvvwicwoovemrggbwwepgpciklwvaepskenmueefuschsbkweycrzmvmuxlygwuinqumoejyxssdwvlruqzwwzsulruhvgwtdxsqgnryjmkoevnpvikxsklnlyjxakwjurnpvwjmhhsrpxrzwkdxuensekuwjmetghfqtzwldrhmxyjmwlahlslvvpmbjrwrvwkmhnifuijxmxwgsrtetilpgfmresdqwbmtuecmjehxjhcugxvweiagsqgwrtscnkescgvmfngkmrfyuijvaxrwqyihwawllrxvvwicagaicmvrlxslpntpvgwrgnrycicpwmltignimmkiyxdrnewvsvux','jwisihanyw'))
#print(cle_cryptanalyse('tseuweepniigwvlkanwbzrnidbdruemiuaggcbtxvkwlwqayvekmgvvtnfnijsdmaednhvzummwgtegmtmbmsgmbwpzrsdwvtbpxvvjqteepqvkiymsoepeilbicaloavqfvlavtnfnijgsdwlsnpwrzgqjiaenitseuwmovgxdiemuxqhkijxhmmmegtigpmasmrbeivrsgsgtccvcisdwvtbwwcikzsrefgxksmadxsgqruyklwlcnotjhwkggcrpxielqggaiggcivmjgirtgfvhalkeowgyefbvxsnhjiimawlfvnijhwvmbtrvfismqdeaefiejavlhmogwfyktwlceqwjikinxcygwyyabeblygjiefksbsruulmfmkhngrejvwdwguruhvwtiygefczvgdivxrakiiixmefezqvkiszsoeaufiyushhueczfmjlggnrcwzpwidnnqgweslzwleavvvenmueecgygpwvwweyqqsvwmlwifreiysdwveyniesknjxrruhrrktgkdeghvpsvmbtpqqdiewjtngneeradwksnkvvhwtseiogvrxawfweccvzwbmvbsnkwvggclxcruszvbmmgefuiuiewfialupvwutgvhruhrrfqnxrfcmiiicaloapiisfbuhmzggvpdmkwiyaehysbgkzrcrjtmqklefvytilbwyovupvwwvlxnqtivpdmkooavwfrfmjiohtxfmdpgfmniiuemrgnrqjyzrsxhxlygulidmuaaavulmnikxlrxiiqsqfmeacrkgwkztngfijtszlbsnpwhywrsbeaviehmumkmhtiigguexuaelrrllwvozrpzgabwiuvutjedugwirthrrktwurbwmcpszvwefxsjkwawmlruffmklsesneididmsncektvvvcvxszqyksfavxsgcffvkymtnqnijfshghknuhvggzjxzrczrruiaxngcprvwvuhngtiuikkztrffiiyfalxdgneegwavxnbwzvemkggtegwkvsathueiitsmbwtuwqyihzcacehpijwwlwyrnpgvgwymbfhvtfyjvgnsyggyefbvnmnnlvyjkwltycqrvupwyuagfiivmkveafvvwicwoovemrggbwwepgpciklwvaepskenmueefuschsbkweycrzmvmuxlygwuinqumoejyxssdwvlruqzwwzsulruhvgwtdxsqgnryjmkoevnpvikxsklnlyjxakwjurnpvwjmhhsrpxrzwkdxuensekuwjmetghfqtzwldrhmxyjmwlahlslvvpmbjrwrvwkmhnifuijxmxwgsrtetilpgfmresdqwbmtuecmjehxjhcugxvweiagsqgwrtscnkescgvmfngkmrfyuijvaxrwqyihwawllrxvvwicagaicmvrlxslpntpvgwrgnrycicpwmltignimmkiyxdrnewvsvux',3,'e'))

#print(chiffrement_vigenere('cyttprimnwcnshbrvgxtqcrhgaeucrvuomayewfppnpeiuoirutebtrjmqiecediawnpttcqwfpqjmpspyenmfepnixwbqopmquvqgomwyrrhlmyfntnftflghgdpnpeiuyssnweolmxygiqfzjlgwnpwuucmgcwxiaxrzywfntnftflghgdrtnrwrcmxyfwwcpjpvjfptzcfpcnlfnqiepxyyfeezgmyrxuzryjyyuavtwuiuoiquqiezquifmvtssgnmuaewzbmutprygpgyiexrhcywjnfeofwjxnzqtvzhwswcizxrwkoijmnyudmlyamcwixoaixzmyoeixprfcghccvnprvfppfogvgnsyyqinlfflemgcizhrtgcwthaiuzvycgypxmqcgekcinfrxctxhizqgoesmyiuqmqgfhgryjleirprxuqexthqyfhgnswugmqywwyztntwxuvipepfpnrvoixuiiueinfferavtwuefppfpbmvfvjihwgevtoiekehfpvhnpgmuhjhpywihzttxqusippxwypinlvjmfiompfcgewikwifstomsugiwcwvorhcgmiuieketzpbmtoesmqiuqmqgfhgdgnyaggqmhnvspmifopswahjjrxkeixfhqkpvjmvrftuzuvipeuzcyivlmyyajqygycbrcwegufiwyixiexgoevonvkfqfpnmvpxjcawvlpqygsweeznbytniwnnmppqjhgpgdcxnrqgoiwysvqthnmfioprywnvfpwgoypgdqthgekprymnrunixmrttpyaydygwiforxctxjhrfwwpnnvspdszxnmpoeacqvgdxfvbyesigyryppztckgcgiwhryupwtlgmgoixypvcywtoiiplmyxrwcqjnwuitwirigttppzxrpcdgjhfiwchjgnvtlxtogwgfpfjeiubyjfntqcxjmrwqtxkyeqgpmqxrwepriuvxkwrfleivlmyjnwfphjmpipovjjhmutpxuevgeejhsmpweuiexgdszpemvpxiuimfpyyfnwvftjoehgdeacrhggesnyykdiiycpqjennhrezqufrbgtrkieqcemvoryppznhtxctrjxrtgcwthaiudiiycpcnenyaxffruifxglpfogvgciluehcyxfoceudelyyiupgwuawipesnfqwcezrfmvfixuhjqyhiyyeulpqyvpalzfcgfkprzhrgkyuzuaxctrjxbvftrfnrytdgnhdiecesmticyxxygwkeyjyaxtppjmrgtlrxarepewjnyiuzvicaevpywmhrgxehbvrgcmjczttpwxcbrplryyyeunismrytoiruevcesznfiwweulrwsfiqucsteixyfskejjlzigtpiyfggyhfcgmnyewlrxctxuufhgoixwrrfciuovwkwwfleivliszvrnlttlgiuzyalvxgehfpvhgfxqufxwaizlqiulznyqixlryfhmuphjjysalmyoagqxtqykikyjtlzevtuzyhrggmsagekyiiycitdsshrwuphjjyeelmjhghwyttmgicwezneitpkflqepeezjnwulkjfrwgnvfhfkglrymzytlycmvxwpwfosspohjfnwcwpjcyccgennomgyysypmpbyfhgekyiiiehkyeyyhvunmskrgtlrxarepewjnfmvfijhgvgwixypvcywlynrvdiyfrwqchnhnxgfvxoaiolgmcaittingcvgdwniarcyxj','gnwypwv'))

