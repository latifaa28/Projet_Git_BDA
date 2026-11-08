prix_ht = float(input("donner le prix hors taxe : "))
taux_tva = float(input("donner le taux de TVA :"))
montant_tva = prix_ht * taux_tva /100
prix_ttc = prix_ht + montant_tva
print("Montant TVA :", montant_tva)
print("prix TTC:",prix_ttc)
print("Prix hors taxe :", prix_ht)