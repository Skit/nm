from bot.src.app.server.connection import Connection


class Migrations(Connection):

    def init(self):
        cursor = self.conn

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS nomad_bazaars (
             day CHAR(3) NOT NULL,
             title VARCHAR(150) NOT NULL,
             description VARCHAR(255) NOT NULL,
             mapUrl VARCHAR(255) NOT NULL,
             language_code CHAR(2) NOT NULL)
        ''')

        cursor.execute('''
        CREATE UNIQUE INDEX IF NOT EXISTS uidx_nomad_bazaars_day_title ON nomad_bazaars(day,title)
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS nomad_users (
            id INTEGER NOT NULL,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL,
            language_code VARCHAR(5) NOT NULL,
            created_at timestamp DEFAULT current_timestamp)
        ''')

        cursor.execute('''
        CREATE UNIQUE INDEX IF NOT EXISTS uidx_nomad_users_id ON nomad_users(id)
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS nomad_schedule (
            user_id INTEGER NOT NULL,
            week JSON,
            is_active INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES nomad_users(id) ON DELETE CASCADE ON UPDATE RESTRICT)
        ''')

        cursor.execute('''
        CREATE UNIQUE INDEX IF NOT EXISTS uidx_nomad_schedule_user_id ON nomad_schedule(user_id)
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS nomad_stat (
            user_id INTEGER NOT NULL,
            count_notifies INTEGER NOT NULL DEFAULT 0,
            updated_at timestamp DEFAULT current_timestamp)
        ''')

        cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_nomad_stat_user_id ON nomad_stat(user_id)
        ''')

        cursor.commit()

Migrations().init()
