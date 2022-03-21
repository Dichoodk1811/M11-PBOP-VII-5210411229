#5210411229_Dicka Armadhany
class Mahasiswa :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim

    def tampil(self) :
        print(f"Nama\t\t: {self.nama} \nNim \t\t: {self.nim}\n")

class Hitung(Mahasiswa) :
    def __init__(self, nama, nim, jmlhsks, sks) :
        super().__init__(nama, nim)
        self.jmlhsks = jmlhsks
        self.sks = sks
        #5210411229_Dicka Armadhany
    def tampil(self):#Override Method
        totalsks = self.jmlhsks + self.sks

        if totalsks>=100 :      #5210411229_Dicka Armadhany
            print(f"Nama\t\t: {self.nama} \nNim \t\t: {self.nim}")
            print(f"Total Sks\t: {totalsks}")
            print("Diperbolehkan mengambil skripsi\n")
        else :
            print(f"Nama\t\t: {self.nama} \nNim \t\t: {self.nim}")
            print(f"Total Sks\t: {totalsks}")
            print("Tidak diperbolehkan mengambil skripsi\n")
        
mahasiswa1 = Mahasiswa("Eren", 5210411229)
mahasiswa2 = Hitung("Mikasa", 5210411292, 96, 24)
mahasiswa1.tampil()
mahasiswa2.tampil() #5210411229_Dicka Armadhany