from pymysql import connect
from pymysql.cursors import DictCursor
import setting
class User(object):
    def __init__(self):
        self.conn = connect(
            host=setting.MYSQL_HOST,
            port=setting.MYSQL_PORT,
            user=setting.MYSQL_USER,
            database=setting.MYSQL_DB,
            password=setting.MYSQL_PASSWORD,
            charset=setting.MYSQL_CHARSET
        )
        self.cursor = self.conn.cursor(DictCursor)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_user_info(self):
        sql = "select * from user"
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)

        return data