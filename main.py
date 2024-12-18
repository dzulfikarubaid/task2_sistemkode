'''
Buatlah sebuah program yang meminta pengguna untuk memasukan jumlah jam kerja dan tarif per jam, lalu menghitung dan menampilkan gaji karyawan. Jika karyawan yang bekerja lebih dari 40 jam dalam seminggu, maka hitunglah gaji lembur dengan tarif 1.5 kali lipat.
'''
def hitung_gaji(jam_kerja, tarif_per_jam):
    gaji = jam_kerja * tarif_per_jam
    if jam_kerja > 40:
        gaji_lembur = (jam_kerja - 40) * tarif_per_jam * 1.5
        gaji += gaji_lembur
    return gaji

jam_kerja = int(input("Masukkan jumlah jam kerja: "))
tarif_per_jam = float(input("Masukkan tarif per jam: "))
gaji = hitung_gaji(jam_kerja, tarif_per_jam)
print(f"Gaji karyawan: {gaji}")
