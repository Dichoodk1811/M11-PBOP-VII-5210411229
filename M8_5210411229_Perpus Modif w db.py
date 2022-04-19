import mysql.connector
import datetime
                #5210411229_Dicka Armadhany
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perpus"
)
cur=mydb.cursor()

def tambah_buku():
    idbuku = input("-->Masukan id buku\n")
    judul = input("-->Masukan Judul\n")
    subjek = input("-->Masukan Subjek\n")
    penulis = input("-->Masukan Penulis\n")
    info = input("-->Masukan Info\n")
    stok = int(input("-->Masukan Stok\n"))
    cur.execute("INSERT INTO data_buku(id_buku, subjek, judul, penulis, info, stok) VALUES (%s,%s,%s,%s,%s,%s)",(idbuku,subjek,judul,penulis,info,stok))
    mydb.commit()

def update_stok():
    idbuku = input("-->Masukan Id buku\n ")
    jml_stok = input("-->Masukan Stok saat ini \n")
    cur.execute("UPDATE data_buku SET stok=%s WHERE id_buku=%s",(jml_stok,idbuku))
    mydb.commit()
    print("Update Sukses..")

def tampilkan():
    cur.execute("select * from data_buku")
    db = cur.fetchall()
    for row in db:
        print(row)

def hapus_buku():
    idbuku = input("-->Masukan Id buku yang akan dihapus\n")
    cur.execute("DELETE FROM data_buku WHERE id_buku=%s",(idbuku,))
    mydb.commit()
    print("Hapus Sukses..")

def cari_buku():
    idbuku = input("-->Masukan id buku yang dicari\n")
    cur.execute("SELECT * FROM data_buku WHERE id_buku=%s",(idbuku,))
    p = cur.fetchall()
    print(p)
    print("Buku ditemukan")

def pinjambk():
    id_buku = input("Masukan id buku\n")
    nama = input("Masukan Nama peminjam\n")
    jumlah = input("Masukan jumlah\n")
    now = datetime.datetime.now()
    cur.execute("INSERT INTO peminjam(id_buku, nama, tgl_keluar, jumlah) VALUES (%s,%s,%s,%s)",(id_buku,nama,now.strftime('%Y-%m-%d %H:%M:%S'),jumlah))
    mydb.commit()

def kembalibk():
    id_buku = input("Masukan id buku yang akan dikembalikan\n")
    nama = input("Masukan Nama peminjam\n")
    jumlah = input("Masukan jumlah\n")
    now = datetime.datetime.now()
    cur.execute("INSERT INTO kembali(id_buku, nama, tgl_kembali, jumlah) VALUES (%s,%s,%s,%s)",(id_buku,nama,now.strftime('%Y-%m-%d %H:%M:%S'),jumlah))
    mydb.commit()


#MENU PERPUSTAKAAN
while True:
    print("\n Menu Perpustakaan")
    print("1. Input Data Buku")
    print("2. Tampilkan Daftar Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan Buku")
    print("5. Update Stock Buku")
    print("6. Hapus Data Buku")
    print("7. Cari Buku")
    print("8. Keluar")
    pilihan = input("\n-->Masukan Pilihan : ")
    if pilihan == '1':
            tambah_buku()
    elif pilihan == '2':
            tampilkan()
    elif pilihan == '3':
            pinjambk()
    elif pilihan == '4':
            kembalibk()
    elif pilihan == '5':
            update_stok()
    elif pilihan == '6':
            hapus_buku()
    elif pilihan == '7':
            cari_buku()
    elif pilihan == '8':
            print("Terimakasih !")
            break
    else:
        print("Masukan dengan benar!")