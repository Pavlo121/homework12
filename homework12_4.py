import re

def date_form(date_str):
    try:
        day, month, year = date_str.split('/')
        return f'{year}-{month.zfill(2)}-{day.zfill(2)}'
    except ValueError:
        raise ValueError('Неправильний формат дати')

dates = [
    '11/02/2004',
    '27/09/2004',
    '31/12/2024',
]

for date in dates:
    print(f'Старий формат: {date} Новий формат: {date_form(date)}')
