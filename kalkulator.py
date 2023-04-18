print("Kalkulator Sederhana")
num1 = int(input("Masukkan angka pertama: "))
num2 = int(input("Masukkan angka kedua: "))

print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

choice = input("Masukkan pilihan (1/2/3/4): ")

if choice == '1':
   print(num1,"+",num2,"=", num1+num2)
elif choice == '2':
   print(num1,"-",num2,"=", num1-num2)
elif choice == '3':
   print(num1,"*",num2,"=", num1*num2)
elif choice == '4':
   print(num1,"/",num2,"=", num1/num2)
else:
   print("Input salah")