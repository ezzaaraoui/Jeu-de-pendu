def MotValide(mot):
    if len(mot)<4 or len(mot)>25 :
        return False
    for c in mot :
         if ord(c)<65 or ord(c)>90:
            return False
    return True


def convertirCH(mot, tcar):
    for i in range(0,len(mot)):
        tcar.append(mot[i])


def initialiserSolution(tcar, n):
    while True :
        mot=input("donner un mot en majuscule : ")
        if MotValide(mot) and len(mot)==n:
            break
    convertirCH(mot,tcar)


def creerEssai(tessai, n):
    for i in range(0,n):
        tessai.append("*")


def afficherC(tcar,n):
    for i in range(0,n):
        print(tcar[i], end='')
    print()

def jouer(tcar,tessai,char,n):
    t=False
    for i in range(0,n):
        if tcar[i]==char :
            tessai[i]=char
            t=True
    return t


def estFini(tessai, n):
    y=True
    for i in range(0,n):
        if tessai[i]=="*" :
            y=False
    return y



n=0
while True :
    n=int(input("donner la taille du mot : "))
    if n >= 4 and n <= 25 :
        break
tcar=[]
tessai=[]

initialiserSolution(tcar, n)
creerEssai(tessai, n)

essai=5
while essai>0 or not estFini(tessai,n):
    print("Mot actuel : ",end='')
    afficherC(tessai, n)
    char = input("Entrez un caractere : ")
    
    if jouer(tcar, tessai, char, n):
        print("Caractere trouve")
    else:
        essai -= 1
        print(f"Caractere non trouvé,{essai if essai>0 else "dernier"} essais.")
    
    if estFini(tessai, n):
        print("Vous avez gagné")
        break
    elif essai<0:
        print("Vous avez perdu")
        break


