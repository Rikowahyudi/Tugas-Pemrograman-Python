Berat_Badan = int(input("Silahkan Masukkan Berat Badan Anda : "))
Tinggi_Badan = int(input("Silahkan Masukkan Tinggi Badan Anda : "))
Tinggi_Badan = Tinggi_Badan/100
Nilai_IMT = Berat_Badan / (Tinggi_Badan**2)
print("Nilai IMT Anda Adalah : ",Nilai_IMT)

if Nilai_IMT <= 18.5:
    print("Gizi Anda = Underwight")
elif 18.5 <= Nilai_IMT <= 24.99:
    print("Gizi Anda = Normal Range")
elif 25 <= Nilai_IMT <= 29.99:
    print("Gizi Anda = Overweight")
elif 30 <= Nilai_IMT <= 34.99:
    print("Gizi Anda = Obese Class 1")
elif 35 <= Nilai_IMT <= 39.99:
    print("Gizi Anda = Obese Class 2")
else :
    print("Gizi Anda = Obese Class 3")