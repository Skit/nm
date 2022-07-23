from bot.src.app.messages.all import all_langs
from string import Template


def get_message(original: str, language_code: str, **kwds):
    message = original

    if language_code in all_langs:
        messages = all_langs[language_code]
        if original in messages:
            message = messages[original]

    s = Template(message)
    return s.substitute(kwds)
