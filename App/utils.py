import pymysql


class myUtils(object):
    def select_book_list(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='sayid', passwd='111', db='test', charset='utf8')
        cursor = self.conn.cursor()
        cursor.execute("select * from book_list")
        re = cursor.fetchall()
        conn.commit()
        return re
