import json, os
PATH = 'data/akun.json' 

def load_akun():
  if not os.path.exists(PATH) : return{}
  with open(PATH) as f:
    return json.load(f)
  
def simpan_akun(data):
  with open (PATH, 'w') as f:
    return json.dump(data, f, indent=4)