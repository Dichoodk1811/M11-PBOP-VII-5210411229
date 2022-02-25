class Mahasiswa :
    def __init__ (self, nama, nim, prodi, thn_masuk) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
                                        #5210411229_Dicka Armadhany
msiswa1 = Mahasiswa("Udin", "10120371", "Sistem Informasi", 2020)
msiswa2 = Mahasiswa("Ronaldo", "10120513", "Sistem Jaringan", 2021)
msiswa3 = Mahasiswa("Pipeng", "10120514", "Sistem Informatika", 2021)
msiswa4 = Mahasiswa("Neymar", "10120515", "Sistem Informasi", 2021)
msiswa5 = Mahasiswa("Mbappe", "10120526", "Ilmu Komunikasi", 2020)

daftarmahasiswa = [msiswa1, msiswa2, msiswa3, msiswa4]
print("=============== Daftar Mahasiswa ================")
for mhs in daftarmahasiswa :     
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print()