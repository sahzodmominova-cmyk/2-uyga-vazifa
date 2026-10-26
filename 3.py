class Transport:
    def harakatlanish(self):
        print("Transport harakatlanmoqda")


class Mashina(Transport):
    def harakatlanish(self):
        print("Mashina yo'lda yurmoqda")


class Velosiped(Transport):
    def harakatlanish(self):
        print("Velosiped pedal yordamida yurmoqda")


class Poyezd(Transport):
    def harakatlanish(self):
        print("Poyezd relsda yurmoqda")


mashina = Mashina()
velosiped = Velosiped()
poyezd = Poyezd()

transportlar = [mashina, velosiped, poyezd]

for transport in transportlar:
    transport.harakatlanish()
