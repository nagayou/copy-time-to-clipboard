import datetime
import pyperclip

today = datetime.date.today()
pyperclip.copy(today.strftime('%Y-%m-%d'))
