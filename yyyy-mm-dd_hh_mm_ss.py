import datetime
import pyperclip

now_time = datetime.datetime.now()
pyperclip.copy(now_time.strftime('%Y-%m-%d %H:%M:%S'))
