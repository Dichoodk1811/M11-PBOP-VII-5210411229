class Mobil() :
    def __init__(self, jendela, pintu, mesin) :
        self.__jendela = jendela
        self.__pintu = pintu
        self.__mesin = mesin
#5210411229_Dicka Armadhany     #Private
    def Tampil(self) :
        print("Jendela :", self.__jendela)
        print("Pintu :", self.__pintu)
        print("Mesin :", self.__mesin)

bmw = Mobil(4,2,"Diesel")
bmw.Tampil()