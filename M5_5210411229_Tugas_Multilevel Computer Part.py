#Multilevel Computer Part Tugas 
            #Dicka Armadhany
            #5210411229
class ComputerPart:
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        
    def Tampil(self) :  
        print(f"{self.nama} produk dari {self.pabrikan} dijual dengan harga {self.harga}")

class RandomAccessMemory(Processor) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga

    def Tampil(self) :  
        print(f"{self.nama} produk dari {self.pabrikan} dijual dengan harga {self.harga}")
    
class HardDiskSATA(RandomAccessMemory) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga

    def Tampil(self) : 
        print(f"{self.nama} produk dari {self.pabrikan} dijual dengan harga {self.harga}")

p = Processor('Intel', 'Core i7 7740X', 4350000)    
r = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000)
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000)

parts = [p, r, hdd]   
print("\n\t\t\tMULTILEVEL COMPUTER PART")
print("---------------------------------------------------------------------")
for part in parts :
    part.Tampil()   
print("---------------------------------------------------------------------\n")