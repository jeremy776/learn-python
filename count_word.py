print("Menghitung jumlah Kata dalam Teks")

text = input("Masukkan teks: ")
word = input("Masukkan kata yang ingin dihitung: ")

count = text.count(word)
print("Kata", word, "ditemukan sebanyak", count, "kali dalam teks")
