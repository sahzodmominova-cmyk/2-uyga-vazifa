class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh


class Talaba(Inson):
    def __init__(self, ism, yosh, universitet, baho):
        super().__init__(ism, yosh)
        self.universitet = universitet
        self.baho = baho

    def natija(self):
        if 86 <= self.baho <= 100:
            daraja = "A'lo"
        elif 71 <= self.baho <= 85:
            daraja = "Yaxshi"
        elif 56 <= self.baho <= 70:
            daraja = "Qoniqarli"
        else:
            daraja = "Qoniqarsiz"

        print(f"{self.ism}: {self.baho} ball — {daraja}")
        print(f"Universitet: {self.universitet}")


talaba1 = Talaba("Ali", 19, "TATU", 95)
talaba2 = Talaba("Vali", 20, "TATU", 75)

talaba1.natija()
talaba2.natija()
