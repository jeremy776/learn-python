# level
level = input("Masukan tingkat kesulitan: ")
# array level
arr_level = [10, 100, 1000, 10000, 100000]
def random_number(level):
    import random
    if int(level) == 1:
        return random.randint(1, 10)
    elif int(level) == 2:
        return random.randint(1, 100)
    elif int(level) == 3:
        return random.randint(1, 1000)
    elif int(level) == 4:
        return random.randint(1, 10000)
    elif int(level) == 5:
        return random.randint(1, 100000)

while not level.isdigit():
    print("Pastika memberi level sebuah angka")
    level = input("Masukan tingkat kesulitan: ")

while int(level) < 1 or int(level) > 5:
    print("Pastika memberi level sebuah angka antara 1 dan 10")
    level = input("Masukan tingkat kesulitan: ")

curr_number = random_number(level)
print('Kamu haru menebak angka dari 1 sampai ' + str(arr_level[int(level) - 1]))
tebakan = input("Masukan tebakan: ")
percobaan = float(arr_level[int(level) - 1] / 2)
while percobaan > 1:
  percobaan -= 1
  if(int(tebakan) < curr_number):
    print("Tebakan kamu terlalu kecil, masa percobaan kamu tinggal " + str(percobaan) + " kali")
    tebakan = input("Masukan tebakan: ")
  elif(int(tebakan) > curr_number):
    print("Tebakan kamu terlalu besar, masa percobaan kamu tinggal " + str(percobaan) + " kali")
    tebakan = input("Masukan tebakan: ")
  elif(int(tebakan) == int(curr_number)):
    print("Selamat kamu berhasil menebak angka " + str(curr_number) + " dengan level " + str(level))
    break
  if percobaan == 1:
    print("Kamu gagal menebak angka " + str(curr_number) + " dengan level " + str(level))