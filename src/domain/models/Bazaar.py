class Bazaar(object):

    def __init__(self, title: str, description: str, map_url: str, opening: str, active: bool):
        self.title = title
        self.description = description
        self.mapUrl = map_url
        self.opening = opening
        self.active = active
