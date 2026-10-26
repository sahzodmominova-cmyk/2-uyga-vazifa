class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx


class Savat:
    def __init__(self, nom, mahsulotlar=None):
        self.nom = nom
        self.mahsulotlar = mahsulotlar if mahsulotlar is not None else []

    def __len__(self):
        return len(self.mahsulotlar)

    def __bool__(self):
        return len(self.mahsulotlar) > 0

    def umumiy_narx(self):
        jami = 0

        for mahsulot in self.mahsulotlar:
            jami += mahsulot.narx

        return jami

    def __str__(self):
        return f"{self.nom} — {len(self)} ta mahsulot"


mahsulot1 = Mahsulot("Klaviatura", 200000)
mahsulot2 = Mahsulot("Sichqoncha", 100000)
mahsulot3 = Mahsulot("Quloqchin", 300000)

savat = Savat("Mening savatim", [mahsulot1, mahsulot2, mahsulot3])
savat2 = Savat("Bo'sh savat")

print(savat)
print("Mahsulotlar soni:", len(savat))
print("Umumiy narx:", savat.umumiy_narx(), "so'm")

if savat:
    print("Savat bo'sh emas")
else:
    print("Savat bo'sh")

if savat2:
    print("Ikkinchi savat bo'sh emas")
else:
    print("Ikkinchi savat bo'sh")
