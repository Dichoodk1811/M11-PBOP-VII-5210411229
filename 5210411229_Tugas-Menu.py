class MenuMinuman :
    def __init__(self, nama, deskripsi, harga) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
                                        #5210411229_Dicka Armadhany
mnm1 = MenuMinuman("Jus Jambu", "Jus jambu merah tanpa gula", 8500)
mnm2 = MenuMinuman("Jus Alpukat", "Jus alpukat dengan gula merah", 15000)
mnm3 = MenuMinuman("Jus Alpukat Ektra Milk", "Jus alpukat dengan campuran susu cokelat dan tapuran kepingan choco", 15000)
mnm4 = MenuMinuman("Red & Smooth", "Smoothie pisang susu dengan strawberry", 17500)

mnm11 = MenuMinuman("Esteh", "Es teh tawar tanpa gula", 3000)
mnm21 = MenuMinuman("Es Jeruk", "Jeruk nipis tanpa gula", 5000)
mnm31 = MenuMinuman("Es Teh Tarik", "Es Teh Tarik dengan ekstra creamer", 80000)
mnm41 = MenuMinuman("Good Day", "GoodDay Cappucino extra bubuk coklat", 10000)

pilihan_minuman1 = [mnm1, mnm2, mnm3, mnm4]
pilihan_minuman2 = [mnm11, mnm21, mnm31, mnm41]
print("Daftar Menu Healty Fruits")
for mn in pilihan_minuman1 :
    t = '{} harga Rp {}, {}'. format(mn.nama, mn.harga, mn.deskripsi)
    print(t)
print("Daftar Menu Minuman Segar")
for mn in pilihan_minuman2 :
    t = '{} harga Rp {}, {}'. format(mn.nama, mn.harga, mn.deskripsi)
    print(t)