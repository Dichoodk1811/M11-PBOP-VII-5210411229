class Buku :                                            
    def __init__(self, judul, pengarang, tahun_terbit, stok) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__stok = stok
                                        #5210411229_Dicka Armadhany
    def Tampil(self) :
        print(self.judul, "Nama Pengarang :",self.pengarang, ", Tahun Terbit : ", self.tahun_terbit ,", sisa stok : ",self.__stok)  

buku1 = Buku('Huja', 'Tere Liye', 2016, 22)
buku2 = Buku('Dilan 1991','Pidi Baiq', 2014, 35)
buku3 = Buku('Dilan 1991','Pidi Baiq', 2015, 59)

daftarbuku = [buku1,buku2,buku3]
print("==== Daftar Buku ====")
for buku in daftarbuku :     
    buku.Tampil()
    print("\n") 
 