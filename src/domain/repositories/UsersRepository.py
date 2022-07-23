from src.app.server.connection import Connection, StoreException


class UsersRepository(Connection):

    async def add_user(self, user_id: int, first_name: str, last_name: str, username: str, language_code: str,
                       is_bot: bool):
        try:
            c = self.conn.cursor()
            c.execute(
                'INSERT IGNORE INTO nomad_users (id,first_name,last_name,username,language_code,is_bot) VALUES (%s, %s, %s, %s, %s, %s)',
                (user_id, first_name, last_name, username, language_code, is_bot))
            self.conn.commit()
        except Exception as e:
            raise StoreException(e)

    def retrieve(self, user_id: int):
        c = self.conn.cursor()
        c.execute('SELECT * FROM nomad_users WHERE id=%s', user_id)
        return c.fetchone()

    def get_subscribers(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM nomad_users')
        return c.fetchall()
