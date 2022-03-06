class MenuMinuman :
    def __init__(self, nama, deskripsi, harga, stok) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__stok = stok 
                                        #5210411229_Dicka Armadhany_Menu tambahan atribut private
    def Tampil(self) :
        print(self.nama, "harga Rp :",self.harga, self.deskripsi ,"sisa stok : ",self.__stok)
                                        #5210411229_Dicka Armadhany
mnm1 = MenuMinuman("Jus Jambu", "Jus jambu merah tanpa gula,", 8500, 12)
mnm2 = MenuMinuman("Jus Alpukat", "Jus alpukat dengan gula merah,", 15000, 10)
mnm3 = MenuMinuman("Jus Alpukat Ektra Milk", "Jus alpukat dengan campuran susu cokelat dan tapuran kepingan choco,", 15000,9)
mnm4 = MenuMinuman("Red & Smooth", "Smoothie pisang susu dengan strawberry,", 17500, 7)
mnm5 = MenuMinuman("Esteh", "Es teh tawar tanpa gula,", 3000,20)
mnm6 = MenuMinuman("Es Jeruk", "Jeruk nipis tanpa gula,", 5000, 18)


pilihan_minuman1 = [mnm1, mnm2, mnm3, mnm4,mnm5,mnm6]

print("Daftar Menu Healty Fruits")
for mn in pilihan_minuman1 :
    mn.Tampil()
    print("\n")