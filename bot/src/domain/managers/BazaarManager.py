from bot.src.domain.repositories import BazaarsRepository, MenuRepository
from bot.src.app.factories.MessageFactory import get_message


class BazaarManager(BazaarsRepository.BazaarsRepository, MenuRepository.MenuRepository):

    def get_all(self, day: str, language_code: str):
        day_key = None
        message = ''

        for day_key, day_name in self.retrieve(language_code).items():
            if day_name == day:
                break

        if day_key:
            for bazaar in super().get_all(day_key, language_code):
                message += "\n" + '📍<a href="' + bazaar[3] + '">' + bazaar[1] + '</a>' + "\n" + \
                           bazaar[2] + "\n"
        else:
            message = ''

        if message:
            message += "\n" + '⏱' + get_message('Markets open from ~9am-7pm', language_code)

        return message

