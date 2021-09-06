import pyfiglet

vraag = pyfiglet.figlet_format("Wat is jouw naam?")
print(vraag)

name = input("Jouw naam: ")
adres = input("Adres: ")
postcode = input("Post code: ")
woonplaats = input("Woonplaats: ")


test = pyfiglet.figlet_format(f"Naam: {name}\nAdres: {adres}\nPostcode: {postcode}\nWoonplaats: {woonplaats}")

print(test)