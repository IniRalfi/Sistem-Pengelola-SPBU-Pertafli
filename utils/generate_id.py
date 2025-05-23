from datetime import datetime
import random
import string


def generate_id():
  now = datetime.now()
  timestamp = now.strftime("%Y%m%d-%H%M%S")
  random_str = ''.join(random.choices(string.digits+string.ascii_uppercase, k = 4))
  return f"PTF-{timestamp}-{random_str}"