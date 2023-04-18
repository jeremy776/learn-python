import datetime

print('Menghitung Episentrum | menggunakan rumus Laksa')

def is_valid_time(time_str):
  try:
    datetime.datetime.strptime(time_str, '%H:%M:%S')
    return True
  except ValueError:
    return False

p = input('Masukkan waktu gempa pertama: ')

while not is_valid_time(p):
  print('Waktu tidak valid')
  p = input('Masukkan waktu gempa pertama: ')

s = input('Masukkan waktu gempa kedua: ')

while not is_valid_time(s):
  print('Waktu tidak valid')
  s = input('Masukkan waktu gempa kedua: ')

p = datetime.datetime.strptime(p, '%H:%M:%S')
s = datetime.datetime.strptime(s, '%H:%M:%S')

selisih = s - p
selisih = selisih - datetime.timedelta(minutes=1)
selisih = (selisih.total_seconds() / 60)
jarak_episentrum = selisih * 1000

print('Jarak episentrum adalah', jarak_episentrum, 'km')