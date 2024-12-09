KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:

    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti or KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or OLETUSKASVATUS

        if self.kapasiteetti < 1 or self.kasvatuskoko < 1:
            raise ValueError("Kapasiteetin ja kasvatuskoon on oltava positiivisia kokonaislukuja.")

        self.alkiot = self._luo_lista(self.kapasiteetti)
        self.alkioiden_maara = 0

    def kuuluu(self, numero):
        return numero in self.alkiot[:self.alkioiden_maara]

    def lisaa(self, numero):
        if not self.kuuluu(numero):
            if self.alkioiden_maara >= len(self.alkiot):
                self._kasvata_listaa()
            self.alkiot[self.alkioiden_maara] = numero
            self.alkioiden_maara += 1
            return True
        return False

    def _kasvata_listaa(self):
        uusi_lista = [0] * (len(self.alkiot) + self.kasvatuskoko)
        self._kopioi_lista(self.alkiot, uusi_lista)
        self.alkiot = uusi_lista

    def poista(self, numero):
        if self.kuuluu(numero):
            index = self.alkiot.index(numero)
            self.alkiot[index:self.alkioiden_maara - 1] = self.alkiot[index + 1:self.alkioiden_maara]
            self.alkioiden_maara -= 1
            return True
        return False

    def _kopioi_lista(self, vanha, uusi):
        uusi[:len(vanha)] = vanha

    def mahtavuus(self):
        return self.alkioiden_maara

    def to_int_list(self):
        return self.alkiot[:self.alkioiden_maara]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z
        

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"
