string_zahl = "99.99"
zahl = float(string_zahl)
print(zahl)
def berechne_gesamtpreis(nettopreis):
 nettopreis
 mehrwertsteuer = nettopreis * 0,19 
 gesamtpreis = nettopreis + mehrwertsteuer
 return gesamtpreis
preis_ohne_mehrwertsteuer = float(input("bitte geben sie den nettopreis ein: "))
gesamtpreis = berechne_gesamtpreis
print(f"der gesamtpreis beträgt:{gesamtpreis} Euro")
print(f"der gesamtpreis beträgt: {gesamtpreis:.2f} euro")