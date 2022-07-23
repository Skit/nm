from src.app.server.connection import Connection


class Migrations(Connection):

    def init(self):
        cursor = self.conn.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS nomad_bazaars ('
            'day CHAR(3) NOT NULL,'
            'title VARCHAR(150) NOT NULL,'
            'description VARCHAR(255) NOT NULL,'
            'mapUrl VARCHAR(255) NOT NULL,'
            'language_code CHAR(2) NOT NULL,'
            'UNIQUE INDEX (day, mapUrl))'
            'CHARACTER SET utf8mb4 COLLATE utf8mb4_bin'
            )

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS nomad_users ('
            'id INT(11) NOT NULL,'
            'first_name VARCHAR(255) NOT NULL,'
            'last_name VARCHAR(255) NOT NULL,'
            'username VARCHAR(255) NOT NULL,'
            'language_code VARCHAR(5) NOT NULL,'
            'is_bot TINYINT(1) NOT NULL,'
            'created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,'
            'UNIQUE INDEX (id))'
            'CHARACTER SET utf8mb4 COLLATE utf8mb4_bin'
            )

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS nomad_schedule ('
            'user_id INT(11) NOT NULL,'
            'week JSON,'
            'is_active tinyint(1) NOT NULL,'
            'UNIQUE INDEX (user_id),'
            'FOREIGN KEY(`user_id`) REFERENCES nomad_users(`id`) ON DELETE CASCADE ON UPDATE RESTRICT)'
            'CHARACTER SET utf8mb4 COLLATE utf8mb4_bin'
            )

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS nomad_stat ('
            'user_id INT(11) NOT NULL,'
            'count_notifies INT(11) NOT NULL DEFAULT 0,'
            'updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,'
            'INDEX (user_id))'
            'CHARACTER SET utf8mb4 COLLATE utf8mb4_bin'
            )


Migrations().init()
