import json, os
PATH = 'data/transaksi.json'

def load_transaksi():
  if not os.path.exists(PATH) : return{}
  with open(PATH) as f:
    return json.load(f)
  
def simpan_transaksi(data):
  with open (PATH, 'w') as f:
    return json.dump(data, f, indent=4)

