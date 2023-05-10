"""# QUESTION I

  #1.Creation d'une liste contenant 10 elements

    voitures = ['Toyota', 'Nissan', 'Jeep', 'Suzuki', 'Duster', 'Tesla', 'Mercedes', 'Porsche', 'Mustang', 'Bentley']

    #Affichage de ces elements

    print("-----Les elements se trouvant sur notre liste sont:-----")
    for i in voitures:
        print(i)
        
        
    # 2.Changement du 5eme element dans notre liste

voitures[5-1] = 'Veroster'

#.Affichage du nouveau element dans notre liste

for i in voitures:
    print (i)
    
    #3.Affichage de la liste contenant les elements contenant la lettre "a"

Newlist=[]
for n in voitures :
    if "a" in n:
        Newlist.append(n)
        print(Newlist)
        
#4.Ajout et affichage d'un élément à la fin de notre liste

voitures.append("Acura")
for a in voitures :
    print(a)
    
    #5.Ajout d'un élément à l’index numéro 2

voitures.insert(2,"Lincoln")
for i in voitures:
     print(i)
     
     #6.Supprimer l'élément numéro 3 et afficher la liste restante

del voitures[3-1]
for i in voitures:
    print(i)
    
    #7.Ordonner la liste

voitures.sort()
print(voitures)

#8.Afficher la liste au sens inverse

reversed(voitures)

#9.Vider la liste

voitures.clear()

#10.Supprimer la liste

del(voitures)"""

# Question II

#0.Creation d'une tuple de 10 éléments de type entier 

nombres = (0,1,2,3,4,5,6,7,8,9)
for i in nombres:
    print(i)

#1.afficher le nombre de fois 3 est apparut
print(nombres.count(3))

#2.Afficher le contenu de l'élément numéro 5

print(nombres[4])

#3.Ordonner la tuple
nombres = tuple(sorted(nombres))
print(nombres)

#4.Ajouter un élément à la fin de la tuple

liste = list(nombres)
liste.append(10)
nombres = tuple(liste)
print(nombres)





