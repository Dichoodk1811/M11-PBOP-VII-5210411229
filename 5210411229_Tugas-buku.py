class Buku :                                            
    def __init__(self, judul, pengarang, tahun_terbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
                                        #5210411229_Dicka Armadhany
buku1 = Buku('Huja', 'Tere Liye', 2016)
buku2 = Buku('Dilan 1991','Pidi Baiq', 2014)
buku3 = Buku('Dilan 1991','Pidi Baiq', 2015)

daftarbuku = [buku1,buku2,buku3]
print("==== Daftar Buku ====")
for buku in daftarbuku :     
    teks = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit)
    print(teks) 
print() 