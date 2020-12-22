# No.1
print("Prgogram Mengubah Huruf Besar Menjadi Huruf Kecil dan Sebaliknya")

kata_awa1 = input("Masukkan Kata = ")

kata_baru = ""

for kar in kata_awa1 :
    if kar.isupper() :
        karbaru = kar.lower()
    elif kar.islower():
        kerbaru = kar,upper ()
    else :
        karbaru = kar
    Kata_baru = Kata_baru + karbaru
print("Kalimat Sekarang Menjadi = ", kata_baru)


# NO.2
inc = 1
for x in range(5,0,-1):
    for y in range(x,0,-1):
      print(" ",end="")
    print("*"*inc)
    inc += 2;

# No 3
size = 5
for x in range(size ,-(size),-1):
    for y in range(1,abs(x)+1):
        print(" ",end="")
    for z in range(size,abs(x),-1):
        print("* ",end="")
    print()
   
# No.5
#Chapter9
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas'     : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid'     : 40, 'uas'     : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid'   : 100, 'uas'    : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid'    : 20, 'uas'     : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid'  : 70, 'uas'     : 100}]

print ('===========================================')
print ("NIM", "\t NAMA", "\t\tN.MID", "\t\tN.UAS")
print ('-------------------------------------------')
for data in nilai :
    print (data['nim'].ljust(9),data['nama'].ljust(15),str(data['mid']).ljust(13),str(data['uas']).ljust(9))
print ('-------------------------------------------')

# No.6
#Chapter9
import math
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
         {'nim' : 'A02', 'nama' : 'Budi',     'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha',   'mid' : 100,'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna',    'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah',  'mid' : 70, 'uas' : 100}]
print ('==============================================================')
print("NIM".ljust(10), "NAMA".ljust(10), "N.MID".ljust(10), "N.UAS".ljust(10), "N.AKHIR".ljust(10), "STATUS".ljust(10))
print ('--------------------------------------------------------------')

for data in nilai :
    HitungNilaiAkhir = (data['mid'] + (2 * data['uas'])) / 3
    
    nilaiakhir = math.ceil(HitungNilaiAkhir)
    
    if (nilaiakhir > 60) :
        status = 'LULUS'
    else :
        status = 'GAGAL'
    print (data['nim'].ljust(10),data['nama'].ljust(12),str(data['mid']).ljust(10),str(data['uas']).ljust(10),str(nilaiakhir).ljust(8),str(status).ljust(10))
print ('--------------------------------------------------------------')

# No.7
#Chapter9
mhs = ['K001:ROSIHAN ARI        :1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN        :2005-01-28:KARANGANYAR']
print("===========================================================")
print("NIM".ljust(10), "NAMA MAHASISWA".ljust(20), "TGL LAHIR".ljust(12), " TEMPAT LAHIR".ljust(8))
print("-----------------------------------------------------------")
for data in mhs :
    mahasiswa          = data.split(':')
    nim                = mahasiswa[0]
    nama               = mahasiswa[1]
    tglLahir           = mahasiswa[2]
    dataTglLahir       = tglLahir.split('-')
    formatBaruTglLahir = '{0}/{1}/{2}'.format(dataTglLahir[0],dataTglLahir[1],dataTglLahir[2])
    tempatLahir        = mahasiswa[3]
    print(nim.ljust(10), nama.ljust(20), formatBaruTglLahir.ljust(15), tempatLahir.ljust(8))
print("-----------------------------------------------------------")
