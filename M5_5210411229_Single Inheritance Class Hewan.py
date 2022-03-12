#Single Inheritance
                #Dicka Armadhany
                #5210411229
class Hewan :   
    def bersuara(self) :
        print("Kucing Bersuara")

#Child class mewarisi class hewan        
class Kucing(Hewan) :
    def suara(self) :
        print("Meoong..Meoong..Meoong..")

#Objek
k = Kucing()
k.suara()
k.bersuara()