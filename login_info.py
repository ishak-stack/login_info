login_info = {
   'rayan': {
      'id': 1,
      'pass': '1111',
      'school': 'rayan school',
      'email': 'rayan@mail.com',
   },
   'aymen': {
      'id': 2,
      'pass': '1222',
      'school': 'aymen school',
      'email': 'aymen@mail.com'
   },
   'ishak': {
      'id': 3,
      'pass': '1333',
      'school': 'ishak school',
      'email': 'ishak@mail.com'
   }
}

def unique_id(db, a=1):
   from random import shuffle, choice
   id_lst = [choice(range(1, 10)) for _ in range(a)]
   shuffle(id_lst)
   id_num = int(''.join([str(s) for s in id_lst]))
   id_dict = [user['id'] for user in db.values()]
   if len(id_dict) < int('9'*a):
      return unique_id(db) if id_num in id_dict else id_num
   else:
      a += 1
      return unique_id(db, a)
print(unique_id(login_info))

def inputs(txt='', user=None, password=None, school=None, email=None):
   if user: user = input('Enter your username: ').strip().lower()
   if password: password = input('Enter your password: ').strip()
   if school: school = input(f'Enter {txt}school name: ').strip().title()
   if email: email = input(f'Enter {txt}email address: ').strip().lower()
   return (user, password, school, email)

def sign_up(db):
   user_login, _, _, _ = inputs(user=True)
   if user_login not in db:
      _, pass_login, school, email = inputs(password=True, school=True, email=True)
      db[user_login] = {'id': unique_id(db),'pass': pass_login, 'school': school, 'email': email}
      print('Successfully registered !')
      return user_login
   else:
      print('Username already exists !')
      main()

def show_details(user_data):
   print('Details '.ljust(21, '='))
   print(f'ID: {user_data["id"]}\nSchool: {user_data["school"].title()}\nEmail: {user_data["email"]}')

def modify_details(user_data):
   _, _, school, email = inputs('new ', school=True, email=True)
   pass_login = input('Enter password to continue: ')
   if pass_login == user_data['pass']:
      user_data['school'], user_data['email'] = school, email
      print('Your info has been modified successfully!')
   else: print('Invalid Password !')

def menu(user_login):
   print('1. Show details\n2. Modify infos\n3. Logout')
   choice = input('Pick a number: ')
   user_data = login_info[user_login]
   if choice == '3': main()
   else: print('Invalid Choice !')
   menu(user_login)

print(f'Welcome to login system\n{"="*23}')
def main():
   print('1. Sign Up\n2. Login\n3. Exit')
   choice = input('Pick a number: ')
   if choice == '1':
      user_login = sign_up(login_info)
      menu(user_login)
   elif choice == '2':
      user_login = login(login_info)
      menu(user_login)
   elif choice == '3': exit()
   else: print('Invalid Choice !')
main()
