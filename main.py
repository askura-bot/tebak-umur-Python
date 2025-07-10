import datetime as dt

welcome_massage = "Selamat datang di Alat hitung umur"
length = len(welcome_massage)
print("="*3 + "="*length + "="*3)
print("="*3 + welcome_massage + "="*3)
print("="*3 + "="*length + "="*3)

hari_ini = dt.date.today()
print(f"\nHari ini adalah: {hari_ini}")

tahun = int(input("\nMasukkan tahun\t: "))
bulan = int(input("Masukkan bulan\t: "))
hari = int(input("Masukkan hari\t: "))

tanggal_lahir = dt.date(tahun, bulan, hari)

print(f"\nTanggal lahir anda adalah: {tanggal_lahir.strftime('%A, %d %B %Y')}")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")

sisa_bulan = 12 - umur_bulan_sisa

print(f"\n{sisa_bulan} bulan lagi anda berulang tahun") 