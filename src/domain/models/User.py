class Bazaar(object):

    def __init__(self, user_id: int, first_name: str, last_name: str, username: str, language_code: str, is_bot: bool):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_bot = is_bot
