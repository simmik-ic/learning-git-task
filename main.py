#Zadanie 1
zakupy = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

print("LISTA ZAKUPÓW")
for sklep, produkty in zakupy.items():
    produkty = [produkt.capitalize() for produkt in produkty]
    print(f"Idę do {sklep.capitalize()} i kupuję tam {produkty}")

liczbaproduktow = sum(len(produkty) for produkty in zakupy.values())
print(f"W sumie kupuję {liczbaproduktow} produktów.")