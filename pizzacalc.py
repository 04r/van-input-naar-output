# Seyit aydin opdracht: Pizza calculator

plarge = 7
pmed = 5
psmall = 3

metingl = 1
metingm = 0.5
metings = 0.25

print("Pizzalarge : 5 euro, meting : 1\nPizzamedium : 5 euro, meting : 0.5\nPizzasmall : 3 euro, meting : 0.25 ")


hvl = int(input("Hoeveel pizzas wilt u? "))

welke = str(input("Welke pizza(s) wilt u? "))

welkelower = welke.lower()


if welkelower == "pizzalarge":
    print("Goede keuze, dat wordt dan ")
    print(plarge * hvl)
if welkelower == "pizzamedium":
    print("Goede keuze, dat wordt dan ")
    print(pmed * hvl)
if welkelower == "pizzasmall":
    str(print("Goede keuze, dat wordt dan "))
    print(psmall * hvl)