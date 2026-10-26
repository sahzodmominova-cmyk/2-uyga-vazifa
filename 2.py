class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh


class Oqituvchi(Xodim):
    def __init__(self, ism, maosh, fan):
        super().__init__(ism, maosh)
        self.fan = fan


class Farrosh(Xodim):
    def __init__(self, ism, maosh, qavat):
        super().__init__(ism, maosh)
        self.qavat = qavat


oqituvchi = Oqituvchi("Ali", 4000000, "Matematika")
farrosh = Farrosh("Vali", 2500000, 2)

print(oqituvchi.ism, oqituvchi.maosh, oqituvchi.fan)
print(farrosh.ism, farrosh.maosh, farrosh.qavat)
