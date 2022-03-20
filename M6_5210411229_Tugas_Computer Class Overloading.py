#Dicka Armadhany 5210411229  
class ComputerPart:
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama    
        self.harga = harga
                            #Dicka Armadhany 5210411229 
class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
                            #Dicka Armadhany 5210411229             
    def Tampil(self) :  
        print("\nTampil dari sub class Processor")
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga\t\t: {(self.harga)}")
                            #Dicka Armadhany 5210411229 
class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama    
        self.harga = harga
                            #Dicka Armadhany 5210411229 
    
    def Tampil(self, kapasitas) :  
        print("\nTampil dari sub class RandomAccessMemory")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {kapasitas}")
        print(f"Harga\t\t: {(self.harga)}")

class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama    
        self.harga = harga

    #Overload Method
    def Tampil(self, kapasitas, rpm) :  
        print("\nTampil dari sub class HardDiskSATA")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {kapasitas}")
        print(f"RPM\t\t: {rpm}\nHarga\t\t: {(self.harga)}")

                    #Dicka Armadhany 5210411229 
p = Processor('AMD', 'Ryzen 5 3600', 3500000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 750000)
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 870000)

print("OVERLOADING COMPUTER PART")
print("\n\t\t\tOVERRIDING COMPUTER PART")
print("=================================================================================")
p.Tampil()
ram.Tampil("16GB")
hdd.Tampil("1TB", 7200) #Dicka Armadhany 5210411229 