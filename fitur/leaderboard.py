from database.akun import load_akun
from utils.sorting import merge_sort

def tampilkan_leaderboard(username):
  print("\n" + "="*30 + " 🏆 LEADERBOARD " + "="*30)
  all_akun = load_akun()

  users = [
    {'username' : akun,
    'poin' : data['poin']}
    for akun,data in all_akun.items() 
    if data.get('role') == 'user' and data.get('poin',0) > 0
    ]
  
  if not users:
    print('Belum ada data poin pengguna.')
    return
  
  users_sorted = merge_sort(users)

  print("\n🏅 Top 10 Pengguna:")
  print("-" * 40)
  for rank, user in enumerate(users_sorted[:10], 1):
      print(f"{rank}. {user['username']:20} {user['poin']:5} poin")

  if username:
    user_position = next(
        (i+1 for i, u in enumerate(users_sorted) 
        if u["username"] == username), None
    )

    if user_position:
      print(f"\n🎯 Posisi Anda: #{user_position} dengan {all_akun[username]['poin']} poin")
