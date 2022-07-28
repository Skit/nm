from bot.src.app.server.connection import Connection, StoreException


class UsersRepository(Connection):

    async def add_user(self, user_id: int, first_name, last_name, username, language_code: str):
        try:
            c = self.conn.cursor()
            c.execute('''
            INSERT INTO nomad_users (id,first_name,last_name,username,language_code) VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
            ''', (user_id, first_name, last_name, username, language_code))
            self.conn.commit()
        except Exception as e:
            raise StoreException(e)

    def retrieve(self, user_id: int):
        c = self.conn.cursor()
        c.execute('SELECT * FROM nomad_users WHERE id=%s', [user_id], binary=True)
        return c.fetchone()

    def get_subscribers(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM nomad_users')
        return c.fetchall()
