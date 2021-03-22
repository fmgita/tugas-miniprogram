# IDEAL
# IDEAL merupakan program yang membantu user untuk mengetahui berat badan idealnya
# Syarat : Perhitungan hanya berlaku untuk user berusia 11 tahun ke atas

print("SELAMAT DATANG DI IDEAL. YUK KETAHUI BERAT BADAN IDEAL DIRI")
nama          = input("Nama               : ")
usia          = int(input("Usia               : "))
jenis_kelamin = input("Jenis Kelamin (L/P): ")
berat_badan   = int(input("Berat badan (kg)   : "))
tinggi_badan  = int(input("Tinggi badan (cm)  : "))
if jenis_kelamin == "L" or jenis_kelamin == "l":
    ideal3_1  = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.1)
    print("\nBerat badan ideal", nama, "adalah", ideal3_1)
    print("Perhitungan ini hanya sebagai patokan umum akan berat badan ideal.\n")
elif jenis_kelamin == "P" or jenis_kelamin == "p":
    ideal3_2  = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.15)
    print("\nBerat badan ideal", nama, "adalah", ideal3_2)
    print("(!!!) Perhitungan ini hanya sebagai patokan umum akan berat dan ukuran tubuh ideal.")
    print("(!!!) NOTE : Tidak apa bila berat badan tidak ideal. Tetap semangat dan jaga kesehatan!")
else:
    print(">> Karakter jenis kelamin tidak sesuai <<\n")