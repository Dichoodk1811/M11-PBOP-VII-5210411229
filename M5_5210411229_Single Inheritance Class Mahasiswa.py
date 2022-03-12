#Single Inheritance
        #Dicka Armadhany
        #5210411229


class Mahasiswa :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
        
    def detailMhs(self) :
        return self.nim, self.nama

    def cekMhs(self) :  
        if self.nim < 150000 :
            return "Mahasiswa Aktif"
        else :
            return "Mahasiswa Tidak Terdaftar"

class Siswa(Mahasiswa) :
    def End(self) : 
        print("Mahasiswa belum melakukan daftar ulang")

mhsiswa1 = Mahasiswa("Mahasiswa 1", 135103)
print(mhsiswa1.detailMhs(), mhsiswa1.cekMhs())
mhsiswa2 = Siswa("Mahasiswa 2", 150503)
print(mhsiswa2.detailMhs(), mhsiswa2.cekMhs())
mhsiswa2.End()