import pymysql
from configparser import ConfigParser


def truncate_table():
    cf = ConfigParser()
    cf.read("../config.ini")
    db = pymysql.connect(
        # cf.get('mysql', 'host'),
        'localhost',
        cf.get('mysql', 'user'),
        cf.get('mysql', 'pwd'),
        cf.get('mysql', 'db'),
        charset='utf8mb4',
    )
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE User;")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute("TRUNCATE TABLE ArticleLabel;")
    cursor.execute("TRUNCATE TABLE Article;")
    cursor.execute("TRUNCATE TABLE Label;")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    cursor.execute("TRUNCATE TABLE Comment;")
    db.commit()
    db.close()


if __name__ == '__main__':
    truncate_table()