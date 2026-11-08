prix_achat=float(input("donner le prix d'achat:"))
prix_vente=float(input("donner le prix de vente:")) 
marge=prix_vente-prix_achat
taux_marge = (marge / prix_achat) * 100
print("La marge est:",marge)
print("Le taux de marge est :", taux_marge, "%")
