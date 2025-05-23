from database.antrian import lihat_antrian, proses_antrian, batalkan_antrian
import time
import questionary
from database.antrian import batalkan_antrian

def batalkan_antrian():
    antrian = lihat_antrian()
    if not antrian:
        print("Tidak ada antrian untuk dibatalkan.")
        return

    pilihan = questionary.select(
        "Pilih transaksi yang akan dibatalkan:",
        choices=[
            {
                "name": f"{t['id']} | {t['username']} | {t['jenis_bbm']} {t['liter']}L", 
                "value": t['id']
            } for t in antrian
        ] + [{"name": "Kembali", "value": None}]
    ).ask()

    if not pilihan:
        return

    if questionary.confirm("Yakin batalkan transaksi ini?", default=False).ask():
        if batalkan_antrian(pilihan):
            print(f"❌ Transaksi {pilihan} berhasil dibatalkan!")
        else:
            print("Transaksi tidak ditemukan!")


def kelola_antrian():
    while True:
        antrian = lihat_antrian()
        print("\n" + "="*20 + " 🛢️ ANTRIAN PENGISIAN BBM " + "="*20)
        
        if not antrian:
            print("Tidak ada antrian saat ini.")
            return
            
        for idx, transaksi in enumerate(antrian, 1):
            print(f"{idx}. {transaksi['username']} | {transaksi['jenis_bbm']} {transaksi['liter']}L | {transaksi['status']}")
        
        # Menu Admin
        action = questionary.select(
            "Pilih aksi:",
            choices=[
                {"name": "Proses antrian terdepan", "value": "proses"},
                {"name": "Batalkan transaksi", "value": "batal"},
                {"name": "Kembali", "value": "kembali"}
            ]
        ).ask()
        
        if action == "proses":
            transaksi = proses_antrian()
            print(f"✅ Transaksi {transaksi['id']} atas nama {transaksi['username']} telah diproses!")
            time.sleep(2)
        elif action == "batal":
            batalkan_antrian()
        else:
            break


def menu_admin():
  while True:
    pilihan = questionary.select('Silahkan pilih menu berikut :',
              choices= [{'name' : 'Kelola Antrian','value' : 'kelola'},
                        {'name' : 'Keluar',  'value' : 'out'}]).ask()
    if pilihan == 'kelola':
      kelola_antrian()
    elif pilihan == 'out':
        break