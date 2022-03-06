class Mobil :
    def __init__(self, jendela, pintu, mesin) :
        self._jendela = jendela
        self._pintu = pintu 
        self._mesin = mesin

bmw = Mobil(4, 2, "Diesel")
#5210411229_Dicka Armadhany #Protected
class Truk(Mobil) :
    def __init__ (self, jendela, pintu, mesin, tipe) :
        super().__init__(jendela, pintu, mesin) 
        self.tipebak = tipe

truk = Truk(4, 2, "Diesel", "Bak Tertutup")
print(truk._mesin)
print(truk.tipebak)