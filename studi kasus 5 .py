def hitung_biaya_parkir(jenis_kendaraan, lama_parkir, jam_masuk, jam_keluar):
    if jenis_kendaraan == "mobil":
        tarif_per_jam = 5000
    elif jenis_kendaraan == "motor":
        tarif_per_jam = 3000

    total_biaya = tarif_per_jam * lama_parkir
    return total_biaya

jenis_kendaraan = (input("Masukan Jenis Kendaraan: "))
lama_parkir = int(input("Masukan Lama Parkir: "))
jam_masuk = int(input("Masukan Jam Masuk: "))
jam_keluar = int(input("Masukan Jam Keluar: "))
hasil = hitung_biaya_parkir(jenis_kendaraan, lama_parkir, jam_masuk, jam_keluar)

print (" Tampilan Semua Data ")
print(" Jenis Kendaraan : jenis_kendaraan")
print(" lama parkir : lama_parkir" )
print(" jam masuk : jam_masuk ")
print(" jam keluar : jam_keluar ")
print("Total Biaya Parkir :", hasil)