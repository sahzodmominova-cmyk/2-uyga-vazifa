class Karta:
    def __init__(self, egasi, raqam_oxiri, balans):
        self.egasi = egasi
        self.raqam_oxiri = raqam_oxiri
        self.balans = balans

    def __str__(self):
        return f"{self.egasi} — {self.balans:,} so'm".replace(",", " ")

    def __gt__(self, boshqa):
        return self.balans > boshqa.balans

    def __lt__(self, boshqa):
        return self.balans < boshqa.balans


karta1 = Karta("Ali", "1234", 500000)
karta2 = Karta("Vali", "5678", 800000)

print(karta1)
print(karta2)

if karta1 > karta2:
    print("Alining kartasida ko'proq pul bor")
elif karta1 < karta2:
    print("Valining kartasida ko'proq pul bor")
else:
    print("Kartalardagi pullar teng")
