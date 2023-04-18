import random
import string

def generate_password(length):
  char = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(char) for i in range(length))
  return password

def main():
  length = int(input("Masukan panjang password: "))
  print(generate_password(length))

if __name__ == "__main__":
  main()
  