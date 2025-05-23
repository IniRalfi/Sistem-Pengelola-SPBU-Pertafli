import questionary
from database.akun import load_akun, simpan_akun
from utils.hashing import hash_password

def register():
  print("\n" + "="*20 + " REGISTER " + "="*20)
  
  username = questionary.text('Masukkan username: ').ask()
  password = questionary.password('Masukkan password: ').ask()
  confirm_password = questionary.password('Konfirmasi password').ask()

  if password != confirm_password:
    print('Error: Password tidak cocok!')
    return None

  if len(password) < 6:
    print('Error: Password minimal 6 karakter!')
    return None

  data_akun = load_akun()
  if username in data_akun:
    print('Error: Username telah terdaftar!')
    return None
  
  hashed_password = hash_password(password)
  data_akun[username] = {
    "password" : hashed_password,
    "role" : 'user',
    "poin" : 0
  }

  simpan_akun(data_akun)
  print('Registrasi berhasil! Silahkan login dengan username yang telah dibuat!')
  return username



def login():
  print("\n" + "="*20 + " LOGIN " + "="*20)
  username = questionary.text('Masukkan username: ').ask()
  password = questionary.password('Masukkan password: ').ask()

  data_akun = load_akun()

  if username not in data_akun:
    print('Username tidak ditemukan!')
    return None
  
  hashed_input = hash_password(password)
  if hashed_input != data_akun[username]['password']:
    print('Error: Password salah!')
    return None
      
  
  print(f'Login berhasil! Selamat datang {username}')
  return {
        "username": username,
        "role": data_akun[username]["role"],
        "poin": data_akun[username]["poin"]
    }
