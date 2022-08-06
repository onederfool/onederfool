import os
import datetime
import pyperclip

folder = 'e:\\Dropbox\\work\\'
year = datetime.datetime.now().strftime("%Y")  #указывает текущий год
month = datetime.datetime.now().strftime("%m") #указывает текущий месяц
day = datetime.datetime.now().strftime("%d")   #указывает текущий день
bufer = pyperclip.paste()                      #забирает содержимое буфера обмена
ta = "ts"    
newpath = os.path.join(year,month,day,bufer,ts) #соединяет переменные в иерархию папок
if not os.path.exists(newpath):
    os.makedirs(newpath)
