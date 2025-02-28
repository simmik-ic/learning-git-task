#Zadanie 1
zakupy = {
    "piekarnia": ["chleb", "bułki", "pączek", "rogal", "bagietka", "drożdżówka"],
    "warzywniak": ["marchew", "seler", "rukola", "szczypiorek gruby", "papryka"]
}

print("LISTA ZAKUPÓW")
for sklep, produkty in zakupy.items():
    produkty = [produkt.capitalize() for produkt in produkty]
    print(f"Idę do {sklep.capitalize()} i kupuję tam {produkty}")

liczbaproduktow = sum(len(produkty) for produkty in zakupy.values())
print(f"W sumie kupuję {liczbaproduktow} produktów.")

print("Miłego dnia!")