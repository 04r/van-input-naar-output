croissant = input("Hoeveel kost een croissant: ") #0.39

stokbrood = input("Hoeveel kost een stokbrood: ") #2.78

kortingsbon = input("Hoeveel is de kortingsbon: ") #0.50

print(f"ik wil 17 croissantjes die {croissant} per stuk kost, ook wil ik 2 stokbroden die {stokbrood} per stuk kosten.\nEn, ik heb 3 kortingsbonnen ter waarde van {kortingsbon}.")

a = croissant * 17
b = stokbrood * 2
c = 3 * kortingsbon

print("Ik moet betalen:")
print(int(a + b - c))
print("\n\n")
print("Tweede opdracht\n\n")




# Tweede opdr

ticket = input("Hoeveel is de ticket: ")#7.45

vrienden = input("Hoeveel vrienden?: ")#3 

jij = 1

iedereen = vrienden + jij

vr_gameseat = input("Hoeveel is de gameseat: ")#0.37 #Per 5 min

totaal = iedereen * ticket

minuten = vr_gameseat * 9

alles = totaal + minuten

print(f"ik moet {alles} betalen")