#Hierarchial Inheritance
        #Dicka Armadhany
        #5210411229

#Class Parents(Orangtua)
class Induk:
    def fungsiinduk(self):
        print("Fungsi pada parent class.")

#Class turunan 1
class Anak1(Induk):
    def fungsianak1(self):
        print("Fungsi pada anak 1.")

#Class turunan 2
class Anak2(Induk):
    def fungsianak2(self):
        print("Fungsi pada anak 2.")

#Objek
kid1 = Anak1()
kid2 = Anak2()
                    #5210411229_Dicka Armadhany
kid1.fungsiinduk()
kid1.fungsianak1()
                    #5210411229_Dicka Armadhany
kid2.fungsiinduk()
kid2.fungsianak2()