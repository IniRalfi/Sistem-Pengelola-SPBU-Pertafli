import json
import os 

ANTRIAN_PATH = 'data/antrian.json'

def load_antrian():
  if not os.path.exists(ANTRIAN_PATH):
        return []
  with open(ANTRIAN_PATH) as f:
        return json.load(f)
  
def simpan_antrian(data):
    with open(ANTRIAN_PATH, 'w') as f:
        json.dump(data,f,indent=4)

def tambah_antrian(transaksi):
    antrian = load_antrian()
    antrian.append(transaksi)
    simpan_antrian(antrian)

def proses_antrian():
    antrian = load_antrian()
    if not antrian:
        return None
    transaksi = antrian.pop(0)
    simpan_antrian(antrian)
    return transaksi

def batalkan_antrian(transaksi_id):
    antrian = load_antrian()
    antrian_baru = [t for t in antrian if t['id'] != transaksi_id]
    
    if len(antrian_baru) == len(antrian):
        return False
    
    simpan_antrian(antrian_baru)
    return True

def lihat_antrian():
    return load_antrian()