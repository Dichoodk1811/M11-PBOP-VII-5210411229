#Multiple Inheritance
            #Dicka Armadhany
            #5210411229

class Mahasiswa1() :
    def __init__(self, nama, nim ) :
        self.nama = nama
        self.nim = nim
                        #5210411229
class Mahasiswa2() :
    def __init__(self, alamat, jurusan) :
        self.alamat = alamat
        self.jurusan = jurusan
                        #5210411229    
class Siswa(Mahasiswa1, Mahasiswa2) :
    def __init__(self, nama, nim, alamat, jurusan) :
        Mahasiswa1.__init__(self, nama, nim)
        Mahasiswa2.__init__(self, alamat, jurusan)

s = Siswa("Mikasa", 135105, "Wall Rose", "Informatika") 
print(f"Nim : {s.nim}, Nama : {s.nama} Alamat : {s.alamat} Jurusan : {s.jurusan}")