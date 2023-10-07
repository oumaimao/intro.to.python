def exo1():
    A = int(input("donner le nombre A:"))
    B = int(input("donner le nombre B:"))
    X = A
    A = B
    B = X
    print("le nombre A est devenu:",A)
    print("le nombre B est devenu:",B)

def exo2():
    A = int(input("donner le nmbre A:"))
    B = int(input("donner le nmbre B:"))
    somme = A+B
    sous = A-B
    mul = A*B
    moy = somme/2
    print("la somme de A et B:",somme)
    print("la soustraction de A moins B:",sous)
    print("la multiplication de A fois B:",mul)
    print("la moyenne de A et B:",moy)

def exo3():
    A = int(input("donner le premier nombre:"))
    B = int(input("donner le deuxieme nombre:"))
    C = int(input("donner le troixieme nombre:"))
    if A == B+C:
        print("A est la somme de B et C:")
    elif B == A+C:
        print("B est la somme de A et C:")
    elif C == B+A:
        print("C est la somme de B et A:")
    else:
        print("aucun nombre est egale a la somme des autres nombres:")


def exo4():
    a = int(input("donner le nombre a :"))
         
    b = int(input("donner le nombre b:"))
    c = int(input("donner le nombre c:"))
    if a>=b>=c:
        print("le plus grand est: a")
    elif b>=a>=c:
        print("le plus grand est: b")
    else:
        print("le plus grand est: c")


def exo5():
    a = int(input("donnez le premier nombre:"))
    b = int(input("donner le deuxieme nombre:"))
    if a == 0 or b == 0:
        print("c'est un produit nul",0)
    elif a>=0 and b<=0 or a<=0 and b>=0:
        print("le signe de ce produit est negatif")
    else:
        print("le signe de ce produit est positif")

def exo6():
    j = int(input("donner la date du jour:"))
    while j<=0 or j>31:
           j = int(input("donner la date du jour:"))

    m = int(input("donner la date du mois:"))
    while m<=0 or m>12:
           m = int(input("donner la date du mois:"))

    a = int(input("donner la date de l'annee:"))
    while a<1600:
           a = int(input("donner la date de l'annee:"))
    if (m == 2 and a%4 == 0 and j == 29) or (m == 2 and a%4 != 0 and j == 28):
        j = 1
        m = m+1
    elif m == 12 and j == 31:
        j == 1
        a == a+1
    elif ((m == 4 or m == 6 or m == 9 or m == 11) and j == 30) or ((m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10) and j == 31):
        j = 1
        m = m+1
    else:
        j = j+1
    print(j,"/",m,"/",a)


def exo7():

    a = int(input("donner un nbre:"))
    b = int(input("donner un autre nbre:"))

    X = 0
    if a>0 or b<0 and a<0 or b>0:
        X = 1

    if b<0:
        b = b*(-1)
    if a<0:
        a = a*(-1)

    S=0
    for i in range(b):
        S=S+a
    if X == 1:
        S=S*-1
    print(S)


def exo8():

    x = int(input("entrez le nombre de la population:"))

    j = 0
    a = 0
    g = 0
    for i in range(1, x + 1):
        age = int(input("entrez l'age qui existe:"))
        if age > 0 and age < 19:
            j = j + 1
        elif age >= 19 and age < 66:
            a = a + 1
        elif age > 65:
            g = g + 1
    pj = (j / x) * 100
    pa = (a / x) * 100
    pg = (g / x) * 100
    print("le nombre des jeunes est", j, "son pourcentage est", pj)
    print("le nombre des adultes est", a, "son pourcentage est", pa)
    print("le nombre des gens agees est", g, "son pourcentage est", pg)




















