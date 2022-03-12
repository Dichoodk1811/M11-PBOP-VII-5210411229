#Multilevel Inheritance
            #Dicka Armadhany
            #5210411229

#Class Parents(Orangtua)
class Hewan :
    def bersuara(self) :
        print("Kucing Bersuara")

#Child(Anak) class mewarisi class hewan
class Kucing(Hewan) :
    def suara(self) :  
        print("Meoong..Meoong..Meoong..")

#Anak class Anakkucing mewarisi dari class hewan
class AnakKucing(Kucing) :
    def minum(self) :   
        print("Minum Susu")

#Objek
AK = AnakKucing()
AK.bersuara()
AK.suara()
AK.minum()