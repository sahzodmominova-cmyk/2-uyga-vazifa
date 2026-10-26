class Shakl:
    def yuza(self):
        return 0


class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon * self.tomon


class TogriTortburchak(Shakl):
    def __init__(self, uzunlik, kenglik):
        self.uzunlik = uzunlik
        self.kenglik = kenglik

    def yuza(self):
        return self.uzunlik * self.kenglik


kvadrat = Kvadrat(5)
tortburchak = TogriTortburchak(6, 4)

shakllar = [kvadrat, tortburchak]

for shakl in shakllar:
    print("Yuza:", shakl.yuza())
