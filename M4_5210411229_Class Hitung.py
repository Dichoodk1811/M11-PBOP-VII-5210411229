class Hitung:
    def __init__(self):
        self.__angkarahasia=0

    def tampilkanhitungan(self):
        self.__angkarahasia +=1
        print (self.__angkarahasia)

hitungan=Hitung()
hitungan.tampilkanhitungan()