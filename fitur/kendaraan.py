
import questionary
from database.kendaraan import load_kendaraan, simpan_kendaraan
from datetime import datetime


def pilih_kendaraan(username):
  kendaraans = []
  kendaraan_all = load_kendaraan()
  for k in kendaraan_all:
    if k['username'] == username:
      kendaraans.append(k)


  if not kendaraans:
    print('Belum ada kendaraan terdaftar!')
    tambah = questionary.select(
      "Tambah kendaraan sekarang?",
      choices=['Ya', 'Tidak']
    ).ask()

    if tambah == 'Ya':
      return tambah_kendaraan(username)
    else:
      return None
    
  pilihan = questionary.select(
    "Pilih kendaraan",
    choices=[f'{k['plat']} ({k['jenis']})' for k in kendaraans]
  ).ask()

  for k in kendaraans:
        if f"{k['plat']} ({k['jenis']})" == pilihan:
            return k

def tambah_kendaraan(username):
    print("\n" + "="*30 + " TAMBAH KENDARAAN " + "="*30)
    jenis = questionary.select(
      'Jenis kendaraan : ',
      choices=['Mobil', 'Motor']
    ).ask()

    plat = questionary.text('Nomor plat anda. contoh (KB 4907 AU) : ').ask().upper()
    nama = questionary.text('Nama kendaraan anda. contoh (Honda Beat) : ').ask()

    data = {
      'username' : username,
      'jenis' : jenis,
      'plat' : plat,
      'nama_kendaraan' : nama,
      'didaftarkan_pada' : datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    kendaraans = load_kendaraan()
    kendaraans.append(data)
    simpan_kendaraan(kendaraans)


def lihat_kendaraan(username):
  kendaraans = []
  kendaraan_all = load_kendaraan()
  for k in kendaraan_all:
    if k['username'] == username:
      kendaraans.append(k)

  print("\n" + "="*30 + " DAFTAR KENDARAAN " + "="*30)
  
  if not kendaraans:
      print("Belum ada kendaraan terdaftar.")
      return
  
  for idx, k in enumerate(kendaraans, 1):
    print(f"{idx}. {k['jenis']} {k['nama_kendaraan']} - {k['plat']}")

def edit_kendaraan(username):
  kendaraans = []
  kendaraan_all = load_kendaraan()
  for k in kendaraan_all:
    if k['username'] == username:
      kendaraans.append(k)

  if not kendaraans:
        print("Belum ada kendaraan untuk diedit.")
        return
  
  pilihan = questionary.select(
    'Pilih kendaraan yang ingin di edit : ',
    choices=[f'{k['nama_kendaraan']} ({k['plat']})' for k in kendaraans]
  ).ask()

  kendaraan_dipilih = None
  for k in kendaraans:
    if f'{k['nama_kendaraan']} ({k['plat']})' == pilihan:
        kendaraan_dipilih = k
        break
    if not kendaraan_dipilih:
        print('kendaraan tidak ditemukan')
        return
    
  nama_baru = questionary.text('Masukkan nama kendaraan baru : ').ask()
  plat_baru = questionary.text('Masukkan plat kendaraan baru : ').ask()

  for k in kendaraans:
    if k['username'] == username and k['nama_kendaraan'] == kendaraan_dipilih['nama_kendaraan'] and k['plat'] == kendaraan_dipilih['plat']:
      k['nama_kendaraan'] = nama_baru
      k['plat'] = plat_baru

  simpan_kendaraan(kendaraans)
  print("Kendaraan berhasil diedit.")
  return


def hapus_kendaraan(username):
  kendaraans = []
  kendaraan_all = load_kendaraan()
  for k in kendaraan_all:
    if k['username'] == username:
      kendaraans.append(k)
  
  if not kendaraans:
      print("Belum ada kendaraan untuk dihapus.")
      return
  
  pilihan = questionary.select(
      "Pilih kendaraan yang akan dihapus:",
      choices=[f"{k['nama_kendaraan']} ({k['plat']})" for k in kendaraans]
    ).ask()

    # Konfirmasi
  if questionary.select(
        f"Yakin hapus {pilihan}?",
        choices=["Ya", "Tidak"]
      ).ask() == "Ya":

        kendaraans_baru = []
        for k in kendaraans:
      
            kendaraan_user = (k["username"] == username)
            format_kendaraan = f"{k['nama_kendaraan']} ({k['plat']})"
            cocok_dengan_pilihan = (format_kendaraan == pilihan)
            
            if not (kendaraan_user and cocok_dengan_pilihan):
                kendaraans_baru.append(k) 
        simpan_kendaraan(kendaraans_baru)
        print("✅ Kendaraan berhasil dihapus!")


def kelola_kendaraan(username):
  while True:
    action = questionary.select(
      f'🚗 Kelola Kendaraan ({username})',
      choices=[
        {"name": "➕ Tambah Kendaraan", "value": "tambah"},
        {"name": "📋 Lihat Daftar Kendaraan", "value": "lihat"},
        {"name": "✏️ Edit Kendaraan", "value": "edit"},
        {"name": "🗑️ Hapus Kendaraan", "value": "hapus"},
        {"name": "🔙 Kembali ke Menu Utama", "value": "kembali"}
      ]
    ).ask()

    if action == 'tambah':
      tambah_kendaraan(username)
    elif action == 'lihat':
      lihat_kendaraan(username)
    elif action == 'edit':
      edit_kendaraan(username)
    elif action == 'hapus':
      hapus_kendaraan(username)
    elif action == 'kembali':
      break
