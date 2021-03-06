import pymysql


class Database(object):
    def __init__(self,  database, host='localhost', user='root', password='000000', charset='utf8'):
        self.conn = pymysql.connect(host=host, user=user, password=password, database=database, charset=charset)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        try:
            self.conn.commit()
        except Exception:
            self.conn.rollback()
        finally:
            self.cursor.close()
            self.conn.close()


class Users(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        print(self.username)