#Hierarchial Inheritance
            #Dicka Armadhany
            #5210411229

class Mahasiswa() :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim

class Siswa1(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
                            #5210411229
    def detSiswa1(self) :
        print(self.nama, "Alamat : Wall Rose")

class Siswa2(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim  
                            #5210411229
    def detSiswa2(self) :
        print(self.nama, "Jurusan : Informatika")

mhsiswa1 = Siswa1("Mikasa", 135105)
mhsiswa2 = Siswa2("Nezuko", 135117)

print(mhsiswa1.nim)   
mhsiswa1.detSiswa1()
print(mhsiswa2.nim)
mhsiswa2.detSiswa2()