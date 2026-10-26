class Telefon:
    def __init__(self, brend, model, narx):
        self.brend = brend
        self.model = model
        self.narx = narx

    def __str__(self):
        return f"{self.brend} {self.model} — {self.narx:,} so'm".replace(",", " ")

    def __eq__(self, boshqa):
        return self.narx == boshqa.narx


telefon1 = Telefon("Samsung", "A54", 4500000)
telefon2 = Telefon("Redmi", "Note 13", 4500000)

print(telefon1)
print(telefon2)
print("Narxlari tengmi?", telefon1 == telefon2)
