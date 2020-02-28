#/usr/bin/env python3
import sqlite3, os, sys, win32crypt, getpass
from prettytable import PrettyTable

def get_chrome_passwd():
   db = 'C:/Users/' + getpass.getuser() + "/AppData/Local/Google/Chrome/User Data/Default/Login Data"
   connection = sqlite3.connect(db)
   cursor = connection.cursor()
   cursor.execute('SELECT action_url, username_value, password_value FROM logins')
   data = cursor.fetchall()

   c = 0

   table = PrettyTable(['id', 'Link', 'Username', 'Password'])
   table.title = 'Chrome Passwords'
   table.align = "l"

   for i in data:
       password = win32crypt.CryptUnprotectData(i[2], None, None, None, 0)[1]

       result = int(c), str(i[0]), str(i[1]), str(password.decode())
       if not str(result[1]) == '':
           print(result[1])
           table.add_row([result[0], result[1], result[2], result[3]])
           c+=1

   print(table)
   print('Found %i saved password(s) in Chrome db' % int(c))

get_chrome_passwd()
