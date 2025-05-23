import json, os
PATH = 'data/kendaraan.json'

def load_kendaraan():
  if not os.path.exists(PATH) : return{}
  with open(PATH) as f:
    return json.load(f)
  
def simpan_kendaraan(data):
  with open (PATH, 'w') as f:
    return json.dump(data, f, indent=4)

