#Dicka Armadhany_5210411229
# Polymorphism
# Contoh menggunakan fungsi len

from msilib.schema import Class


print(len("Polymorphism"))
print(len([0, 1, 2, 3]))

'''
Menggunakan Fungsi len
Output :
12 (Tipe Data String)
4 (Tipe Data List)
'''

# Menggunakan Class
class jerman:
    def ibukota(self):
        print("Berlin adalah ibukota negara Jerman")

class jepang:
    def ibukota(self):
        print("Tokyo adalah ibukota negara Jepang")

negara1 = jerman()
negara2 = jepang()

for country in (negara1,negara2):
    country.ibukota()