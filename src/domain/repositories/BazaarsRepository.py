from src.app.server.connection import Connection


class BazaarsRepository(Connection):

    def get_all(self, day: str, language_code: str):
        c = self.conn.cursor()
        c.execute('SELECT * FROM nomad_bazaars WHERE day=%s AND language_code=%s', (day, language_code))

        return c.fetchall()
