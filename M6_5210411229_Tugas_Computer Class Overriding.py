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
    def __init__(self, pabrikan, nama, harga, kapasitas) :
        super().__init__(pabrikan, nama, harga)
        self.kapasitas = kapasitas
                            #Dicka Armadhany 5210411229  
    # Override  Method
    def Tampil(self) :  
        print("Tampil dari sub class RandomAccessMemory")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {self.kapasitas}")
        print(f"Harga\t\t: {(self.harga)}")

class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
        super().__init__(pabrikan, nama, harga)
        self.kapasitas = kapasitas
        self.rpm = rpm 
                        #Dicka Armadhany 5210411229  
    # Override  Method
    def Tampil(self) :
        print("Tampil dari sub class HardDiskSATA")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {self.kapasitas}")
        print(f"RPM\t\t: {self.rpm}\nHarga\t\t: {(self.harga)}")

p = Processor('AMD', 'Ryzen 5 3600', 3500000)
ram = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 750000, "16GB")
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 870000, '1TB', 7200)
                        #Dicka Armadhany 5210411229  
parts = [p, ram, hdd]   
print("\n\t\t\tOVERRIDING COMPUTER PART")
print("=================================================================================")
for part in parts :
    part.Tampil()
    print("")           #Dicka Armadhany 5210411229  
