def month_name(number_month, language):
    month_en = ['', 'january', 'february', 'march', 'april', 'may', 'june',
                'july', 'august', 'september', 'october', 'november', 'december']
    month_rus = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    if language == 'en':
        return month_en[number_month]
    return month_rus[number_month]


print(month_name(3, 'rus'))
