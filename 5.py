class Kitob:
    def __init__(self, nom, muallif, sahifa_soni):
        self.nom = nom
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def malumot(self):
        print(f"Kitob: {self.nom}")
        print(f"Muallif: {self.muallif}")
        print(f"Sahifalar: {self.sahifa_soni}")


class ElektronKitob(Kitob):
    def __init__(self, nom, muallif, sahifa_soni, format, fayl_hajmi):
        super().__init__(nom, muallif, sahifa_soni)
        self.format = format
        self.fayl_hajmi = fayl_hajmi

    def malumot(self):
        super().malumot()
        print(f"Format: {self.format}")
        print(f"Fayl hajmi: {self.fayl_hajmi} MB")


kitob = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 300)
elektron = ElektronKitob("Python", "Ali", 200, "PDF", 5)

kitob.malumot()
print()
elektron.malumot()
