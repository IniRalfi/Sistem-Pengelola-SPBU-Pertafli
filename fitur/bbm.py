import questionary
from database.transaksi import load_transaksi, simpan_transaksi
from datetime import datetime
from utils.generate_id import generate_id
from fitur.kendaraan import pilih_kendaraan
from database.akun import load_akun, simpan_akun
from database.antrian import tambah_antrian,load_antrian


def transaksi_bbm(username) : 
  print("\n" + "="*30 + " ⛽ TRANSAKSI BBM " + "="*30)

  # 1. Pilih kendaraan
  kendaraan = pilih_kendaraan(username)
  if not kendaraan: 
    return
  
  #2. Pilih jenis BBM
  jenis_bbm = questionary.select(
    'Pilih jenis BBM : ',
    choices = [
      {'name' : 'Pertafli Premium', 'value' : 'premium'},
      {'name': 'Pertafli Max', 'value' : 'max'},
      {'name' : 'Pertafli Turbo', 'value' : 'turbo'}]
  ).ask()

  #3. Input Liter
  jumlah = questionary.text(
        "Masukkan jumlah liter:",
        validate=lambda x: x.replace('.','',1).isdigit() or "Harap masukkan angka"
  ).ask()

  total= float(jumlah) * harga_bbm[jenis_bbm]
  confirm = questionary.select(
    f"Konfirmasi isi {jumlah}L {jenis_bbm} (Rp {total:,.0f})?",
        choices=["Ya", "Batalkan"]
    ).ask()
  
  #4. Konfirmasi
  if confirm == 'Ya':
    transaksi = {
      "id" : generate_id(),
      'username': username,
      'tanggal' : datetime.now().strftime("%Y-%m-%d %H:%M"),
      "kendaraan": kendaraan['plat'],
      "jenis_bbm": jenis_bbm,
      "liter": jumlah,
      "total": total,
      "poin": int(total / 10000),
      'status': 'MENUNGGU'
    }
  
  tambah_antrian(transaksi) 
  print(f"⏳ Anda masuk antrian. No Antrian: {len(load_antrian())}")

  data = load_transaksi()
  data.append(transaksi)
  simpan_transaksi(data)

  akun_data = load_akun()
  if username in akun_data:
    akun_data[username]['poin'] = akun_data[username].get('poin', 0) + transaksi['poin']
  simpan_akun(akun_data)

  print("⛽ Transaksi berhasil! Poin bertambah:", transaksi["poin"])



harga_bbm = {
  'premium' : 10000,
  'max' : 13000,
  'turbo': 15000
}