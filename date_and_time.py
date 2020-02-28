from datetime import datetime, timedelta
import locale
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF8')
dt_now = datetime.now()
delta = timedelta(days=1)
print(f'Вчера: {(dt_now - delta).strftime("%A %d %B %Y")}')
print(f'Сегодня: {(dt_now).strftime("%A %d %B %Y")}')
print(f'Завтра: {(dt_now + delta).strftime("%A %d %B %Y")}')
delta = timedelta(days=30)
print(f'Месяц назад: {(dt_now - delta).strftime("%A %d %B %Y")}')
date_string = '01/01/17 12:10:03.234567'
#date_string = '12/23/2010'
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
#date_dt = datetime.strptime(date_string, '%m/%d/%Y')
print(date_dt)
