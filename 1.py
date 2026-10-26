class Hayvon:
    def __init__(self, nomi, yoshi):
        self.nomi = nomi
        self.yoshi = yoshi

    def ovoz(self):
        print(f"{self.nomi} ovoz chiqaryapti")


class It(Hayvon):
    def qorqlash(self):
        print(f"{self.nomi} uyni qo'riqlayapti")


class Mushuk(Hayvon):
    def sichqon_tutish(self):
        print(f"{self.nomi} sichqon tutyapti")


it = It("Olapar", 3)
mushuk = Mushuk("Momiq", 2)

it.ovoz()
it.qorqlash()

mushuk.ovoz()
mushuk.sichqon_tutish()
