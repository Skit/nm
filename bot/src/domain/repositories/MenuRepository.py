menuKeys = [
    {
        'ru': {
            'mon': 'Понедельник',
            'tue': 'Вторник',
            'wed': 'Среда',
            'thu': 'Четверг',
            'fri': 'Пятница',
            'sat': 'Суббота',
            'sun': 'Воскресенье',
        }
    },
    {
        'en': {
            'mon': 'Monday',
            'tue': 'Tuesday',
            'wed': 'Wednesday',
            'thu': 'Thursday',
            'fri': 'Friday',
            'sat': 'Saturday',
            'sun': 'Sunday',
        }
    }
]


class MenuRepository:

    def retrieve(self, language_code: str):
        result = filter(lambda keys: language_code in keys, menuKeys)
        return list(result)[0][language_code]
