class Mahasiswa :
    def __init__ (self, nama, nim, prodi, thn_masuk, gelombang) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
        self.__gelombang = gelombang
                                        #5210411229_Dicka Armadhany
    def Tampil(self) :
        print(self.nama, "NIM :",self.nim, ", Program Pendidikan : ", self.prodi ,", Angkatan : ",self.thn_masuk,", Jalur : ",self.__gelombang)
msiswa1 = Mahasiswa("Udin", "10120371", "Sistem Informasi", 2020, 1)
msiswa2 = Mahasiswa("Ronaldo", "10120513", "Sistem Jaringan", 2021, 2)
msiswa3 = Mahasiswa("Pipeng", "10120514", "Sistem Informatika", 2021, 3)

daftarmahasiswa = [msiswa1, msiswa2, msiswa3]
print("=============== Daftar Mahasiswa ================")
for mhs in daftarmahasiswa :     
    mhs.Tampil()
    print("\n")