#Multilevel Inheritance
        #Dicka Armadhany
        #5210411229

class Mahasiswa() :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
                        #5210411229
class Siswa1(Mahasiswa) :
    def __init__(self, nama, nim):
        super().__init__(nama, nim)
        
class Siswa2(Siswa1) :
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim  
                        #5210411229
mhsiswa1 = Mahasiswa("Mikasa", 135105)
mhsiswa2 = Siswa1("Nezuko", 135117)
mhsiswa3 = Siswa2("Hancock", 134079)

print(mhsiswa1.nama, mhsiswa1.nim)
print(mhsiswa2.nim)   
print(mhsiswa3.nama)