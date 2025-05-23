from datetime import datetime
from tabulate import tabulate
from utils.queue import Queue

from database.transaksi import load_transaksi

def lihat_riwayat(username):
    print("\n" + "="*30 + " 🕒 RIWAYAT TRANSAKSI " + "="*30)
    
    # 1. Muat data transaksi ke Queue
    transaksi_queue = Queue()
    for transaksi in load_transaksi():
        if transaksi["username"] == username:
            transaksi_queue.enqueue(transaksi)

    if transaksi_queue.is_empty():
        print("Belum ada transaksi.")
        return
    
    print("\n5 Transaksi Terakhir:")
    riwayat = transaksi_queue.get_all()[-5:]  # Ambil 5 terbaru
    for idx, transaksi in enumerate(reversed(riwayat), 1):
        print(
            f"{idx}. {transaksi['tanggal']} | "
            f"id transaksi {transaksi['id']}"
            f"{transaksi['jenis_bbm']} {transaksi['liter']}L | "
            f"Rp {transaksi['total']:,}"
        )