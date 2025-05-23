import json, os
PATH = 'data/promo.json'

def load_promo():
  if not os.path.exists(PATH) : return{}
  with open(PATH) as f:
    return json.load(f)
  
def simpan_promo(data):
  with open (PATH, 'w') as f:
    return json.dump(data, f, indent=4)

