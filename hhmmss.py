import datetime
import pyperclip

now_time = datetime.datetime.now()
pyperclip.copy(now_time.strftime('%H%M%S'))
