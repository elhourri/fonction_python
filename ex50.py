def somme(tab):
    s=0
    for i in range(10):
        s+=tab[i]
    return s

def produit(tab):
    p=1
    for i in range(10):
     p*=tab[i]
    return p

def moyenne(tab):
 s=somme(tab)
 m=s/10
 return m

def p_n(tab):
   print("les nombres positif sont:")
   for i in range(10):
    if tab(i)>0:
       print(tab(i))

    print("les nombres negative sont")  
    for i in range(10):
       if tab(i)<0: 
        print(tab(i))

tab=[0]*10
for i in range(10):
   tab[i]=int(input("veuillez entrer la valeur {i+1}:"))

print("la somme est:",somme(tab))
print("le produit est",produit(tab))
print("la moyenne est",moyenne(tab))


