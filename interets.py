capital=float(input("donner le capital:"))
taux=float(input("donner le taux d'interet:"))
duree=float(input("donner la durée en année:"))
interets = capital * taux * duree / 100
montant_total = capital + interets
print("Les intérets sont:", interets)
print("Le montant total est :", montant_total)
