#5210411229_Dicka Armadhany
class PerpusItem:
    def __init__(self,judul,subjek,lokasi,info):
        self.judul = judul
        self.subjek = subjek
        self.lokasi = lokasi
        self.info = info
#5210411229_Dicka
class Buku(PerpusItem):
    def __init__(self, judul, subjek, lokasi, info,isbn,pengarang,jmlhl,uk):
        super().__init__(judul,subjek,lokasi,info)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhl = jmlhl
        self.uk = uk
#5210411229_Dicka
class Majalah(PerpusItem):
    def __init__(self, judul, subjek, lokasi, info,volume,issue):
        super().__init__(judul, subjek, lokasi, info)
        self.volume = volume
        self.issue = issue
#5210411229_Dicka
class DVD(PerpusItem):
    def __init__(self, judul, subjek, lokasi, info,sutradara,genre):
        super().__init__(judul, subjek, lokasi, info)
        self.sutradara = sutradara
        self.genre = genre
#5210411229_Dicka
Buku1 = Buku('Teknologi Web','Buku Cetak','Rak AB 1','sisa 2','989-558-622','Eko Prayogo',60,'A4')
Majalah1 = Majalah('Fashion Kekinian','Majalah Cetak','Rak BA 2','sisa 1','XI','Fashion')
DVD1 = DVD('Uncharted','Softcopy','Rak BC2','sisa 3','Ruben Fleischer','Adventure')
obj = [Buku1,Majalah1,DVD1]

for object in obj :
    print('{} {} {} {}'.format(object.judul,object.subjek,object.lokasi,object.info))