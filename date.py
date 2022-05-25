date = input('Введите дату в формате dd.mm.yyyy : ')

d, m, y = date.split('.')
print(d, m, y)

days = {
    '01':'Первое',
    '02': 'Второе',
    '03': 'Третье',
    '04': 'Четвёртое',
    '05': 'Пятое',
    '06': 'Шестое',
    '07': 'Седьмое',
    '08': 'Восьмое',
    '09': 'Девятое',
    '10': 'Десятое',
    '11': 'Одиннадцатое',
    '12': 'Двенадцатое',
    '13': 'Тринадцатое',
    '14': 'Четырнадцатое',
    '15': 'Пятнадцатое',
    '16': 'Шестнадцатое',
    '17': 'Семнадцатое',
    '18': 'Восемнадцатое',
    '19': 'Девятнадцатое',
    '20': 'Двадцатое',
    '21': 'Двадцать первое',
    '22': 'Двадцать второе',
    '23': 'Двадцать третье',
    '24': 'Двадацать четвёртое',
    '25': 'Двадцать пятое',
    '26': 'Двадцать шестое',
    '27': 'Двадцать седьмое',
    '28': 'Двадцать восьмое',
    '29': 'Двадцать девятое',
    '30': 'Тридцатое',
    '31': 'Тридцать первое'
}

months = {
    '01':'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}

result = f'{days[d]} {months[m]} {y} года.'
print(result)
