import questionary
from fitur.kendaraan import kelola_kendaraan
from fitur.bbm import transaksi_bbm
from fitur.riwayat import lihat_riwayat
from fitur.leaderboard import tampilkan_leaderboard

def menu_user(username) : 
  
  while True:
    choice = questionary.select(
            f"🏠 Menu User (Login sebagai: {username})",
            choices=[
                {"name": "⛽ Transaksi BBM", "value": "transaksi"},
                {"name": "📜 Lihat Riwayat Pengisian", "value": "riwayat"},
                {"name": "🚗 Kelola Kendaraan", "value": "kendaraan"},
                {"name": "🏆 Cek Poin & Leaderboard", "value": "poin"},
                {"name": "🚪 Keluar", "value": "logout"}]
    ).ask()

    if choice == 'transaksi':
      transaksi_bbm(username)
    elif choice == 'riwayat':
      lihat_riwayat(username)
    elif choice == 'kendaraan':
      kelola_kendaraan(username)
    elif choice == "poin":
      tampilkan_leaderboard(username)
    elif choice == 'logout':
      print('Logout berhasil!')
      break