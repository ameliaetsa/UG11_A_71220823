print("="*7, "Program Manipulasi String", "="*7)
print("Pilihan Menu :")
print("1. Hitung Kata")
print("2. Ubah Kata")
pil = int(input("Pilihan anda: "))

#hitungkata
def banyak_kata(kat):
    k = kal.count(kat)
    return k

#ubahkata
def ubah_kata(kat):
    u = kal.replace(kat,peng)
    return u

if pil == 1:
    kal = input("Masukkan sebuah kalimat/kata : ")
    kat = input("Masukkan kata yang ingin dihitung : ")
    print("Terdapat sebanyak", banyak_kata(kat), "kata",kat,"di dalam kalimat")
elif pil == 2:
    kal = input ("Masukkan sebuah kalimat/kata : ")
    kat = input("Masukkan kata yang ingin diubah : ")
    peng = input("Masukkan kata pengganti : ")
    print("String berhasil diubah menjadi:", ubah_kata(kat))
else :
    kal = input("Masukkan sebuah kalimat/kata: ")
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")


