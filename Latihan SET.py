Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str='aku cinta indonesia'
>>> print(str)
aku cinta indonesia
>>> str=str[:10]+'tanah air ku'+str[9:]
>>> print(str)
aku cinta tanah air ku indonesia
>>> str=''
>>> print(str)

>>> str1='aku cinta tanah air ku indonesia'
>>> str1=str1[:9]+''+str1[22:]
>>> print(str)

>>> print(str1)
aku cinta indonesia
>>> Kelas='Praktikum pemograman berorientasi objek'
>>> up=Kelas.upper()
>>> lo=Kelas.lower()
>>> print(Kelas)
Praktikum pemograman berorientasi objek
>>> print(up)
PRAKTIKUM PEMOGRAMAN BERORIENTASI OBJEK
>>> print(lo)
praktikum pemograman berorientasi objek
>>> s='     python     '
>>> s.strip()
'python'
>>> s
'     python     '
>>> s.lstrip()
'python     '
>>> s.rstrip()
'     python'
>>> len(Kelas)
39
>>> jumlah=len(Kelas)
>>> print('Panjang string tersebut adalah: ',jumlah)
Panjang string tersebut adalah:  39
>>> s1='python'
>>> s2='programming'
>>> s1+s2
'pythonprogramming'
>>> Kelas
'Praktikum pemograman berorientasi objek'
>>> print(Kelas.index('a'))
2
>>> kelas2=Kelas.replace('Praktikum','Praktik')
>>> print(kelas2)
Praktik pemograman berorientasi objek
>>> a='satu'
>>> b='dua'
>>> c='tiga'
>>> print('saya mempunyai %s mangga'%(b))
saya mempunyai dua mangga
>>> kelas2
'Praktik pemograman berorientasi objek'
>>> kelas2.split()
['Praktik', 'pemograman', 'berorientasi', 'objek']
>>> input('hari ini adalah: ')
hari ini adalah: rabu
'rabu'
>>> data1=input('angka 1: ')
angka 1: 8
>>> data2=input('angka 2: ')
angka 2: 5
>>> hasil=int(data1)*int(data2)
>>> print(data1,'*',data2,' = ',hasil)
8 * 5  =  40
>>> list=[0,1,2,3,4,5,6,7,8,9]
>>> print(list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(list[0])
0
>>> print(list[5])
5
>>> print(list[:3])
[0, 1, 2]
>>> len(list)
10
>>> print(list[10-3:])
[7, 8, 9]
>>> print(list[2:9])
[2, 3, 4, 5, 6, 7, 8]
>>> print(list[-10])
0
>>> print(list[0])
0
>>> list.append(10)
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list.insert(1,11)
>>> list
[0, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list2=['halo']
>>> list.extend(list2)
>>> list
[0, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'halo']
>>> list.extend('hai')
>>> list
[0, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'halo', 'h', 'a', 'i']
>>> del list[1]
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'halo', 'h', 'a', 'i']
>>> list.remove(10)
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'halo', 'h', 'a', 'i']
>>> list.pop()
'i'
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'halo', 'h', 'a']
>>> list.pop(2)
2
>>> list
[0, 1, 3, 4, 5, 6, 7, 8, 9, 'halo', 'h', 'a']
>>> a=[50,40,20,10,30]
>>> b=sorted(a)
>>> b
[10, 20, 30, 40, 50]
>>> a
[50, 40, 20, 10, 30]
>>> a.sort()
>>> a
[10, 20, 30, 40, 50]
>>> a.sort(reverse=True)
>>> a
[50, 40, 30, 20, 10]
>>> min(a)
10
>>> max(a)
50
>>> d={1:100, 2:200, 3:300, 4:400, 5:500}
>>> d
{1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
>>> d[2]
200
>>> d.get(4)
400
>>> d.keys()
dict_keys([1, 2, 3, 4, 5])
>>> d.values()
dict_values([100, 200, 300, 400, 500])
>>> del d[1]
>>> d
{2: 200, 3: 300, 4: 400, 5: 500}
>>> b=d.copy()
>>> b
{2: 200, 3: 300, 4: 400, 5: 500}
>>> d.clear()
>>> d
{}
>>> b
{2: 200, 3: 300, 4: 400, 5: 500}
>>> len(d)
0
>>> t=(100,200,300,400)
>>> t
(100, 200, 300, 400)
>>> t[0]
100
>>> t[3]
400
>>> t.index(200)
1
>>> t2=(10,20,10,30,10,40,20)
>>> t2.count(10)
3
>>> t2.count(20)
2
>>> t2.count(30)
1
>>> #LATIHAN TUGAS SET(HIMPUUNAN)
>>> k=set("Hai")
>>> print(k)
{'a', 'H', 'i'}
>>> k.add('Dunia')
>>> print(k)
{'a', 'H', 'Dunia', 'i'}
>>> k.update('Maya')
>>> k
{'H', 'y', 'M', 'i', 'a', 'Dunia'}
>>> k.discard('M')
>>> k
{'H', 'y', 'i', 'a', 'Dunia'}
>>> k.clear()
>>> k
set()
>>> No={3,5,1,2,8}
>>> No_tmbh = no.copy()
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    No_tmbh = no.copy()
NameError: name 'no' is not defined
>>> No_tmbh=No.copy()
>>> No_tmbh.add(7)
>>> print("Nomor yang ada: ",No)
Nomor yang ada:  {1, 2, 3, 5, 8}
>>> print("Nomor tambahan jadi: ",No_tmbh)
Nomor tambahan jadi:  {1, 2, 3, 5, 7, 8}
>>> a = {"Honda","Yamaha","Kawasaki"}
>>> b = {"BMW","Honda","Viar"}
>>> c = a.intersection(b)
>>> print(c)
{'Honda'}
>>> x = {"merah","kuning","hijau"}
>>> y = {"ungu","hitam","putih"}
>>> z = x.difference(y)
>>> print(z)
{'kuning', 'merah', 'hijau'}
>>> s = y.difference(x)
>>> print(s)
{'ungu', 'hitam', 'putih'}
>>> r = {"Inova","Xpander","Altis"}
>>> t = {"Supra","RollsRoyce","AMG"}
>>> y = r.union(t)
>>> print(y)
{'AMG', 'Xpander', 'Inova', 'Altis', 'Supra', 'RollsRoyce'}
>>> q = (6,8,2,66,8,9,78,1,3)
>>> num = frozenset(q)
>>> print(num)
frozenset({1, 2, 66, 3, 6, 8, 9, 78})
>>> 