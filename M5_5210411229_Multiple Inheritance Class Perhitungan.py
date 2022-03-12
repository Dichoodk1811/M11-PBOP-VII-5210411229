#Multiple Inheritance
        #Dicka Armadhany    
        #5210411229

class Perhitungan1 :
    def penjumlahan(self, a, b) :
        return a + b
                        #5210411229
#Parent 2
class Perhitungan2 :
    def perkalian(self, a, b) :
        return a * b    

#Anak Class (Child)
class Hitung(Perhitungan1, Perhitungan2) :
    def pembagian(self, a, b):
        return a / b    
                    #5210411229
#Objek
h = Hitung()    
print(h.penjumlahan(20, 30))
print(h.perkalian(5, 4))
print(h.pembagian(6, 12))