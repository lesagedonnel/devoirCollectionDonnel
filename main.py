# QUESTION I

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