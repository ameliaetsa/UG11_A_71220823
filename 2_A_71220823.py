k = input("Masukkan kata : ")

#fungsi cetak_huruf
def cetak_huruf(kata):

    if len(kata)%2==0 :
        kata_awal = kata[0:3] 
        kata_akhir = kata[len(k)-3: ]
        print("Huruf yang diambil pada kata", k, "adalah", kata_awal, "dan", kata_akhir)
    elif len(kata)%2!=0:
        x=round(len(kata)/2)
        kata_tengah = k[x-1:x+2]
        print("Huruf yang diambil pada kata", k, "adalah", kata_tengah)
cetak_huruf(kata=k)