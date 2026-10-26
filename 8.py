class FilmKutubxonasi:
    def __init__(self, nom, filmlar=None):
        self.nom = nom
        self.filmlar = filmlar if filmlar is not None else []

    def __len__(self):
        return len(self.filmlar)

    def __getitem__(self, indeks):
        return self.filmlar[indeks]

    def __contains__(self, film):
        return film in self.filmlar


kutubxona1 = FilmKutubxonasi(
    "Sevimli filmlar",
    ["Avatar", "Titanic", "Interstellar"]
)

kutubxona2 = FilmKutubxonasi(
    "Multfilmlar",
    ["Shrek", "Madagaskar"]
)

print("Birinchi kutubxona:", len(kutubxona1))
print("Birinchi film:", kutubxona1[0])
print("Avatar bormi?", "Avatar" in kutubxona1)
print("Ikkinchi kutubxona:", len(kutubxona2))
print("Shrek bormi?", "Shrek" in kutubxona2)
