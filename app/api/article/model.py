from app.database import BaseModel
from app import logger


class Article(BaseModel):
    table = 'Article'

    async def insert_article(self, title: str, content: str, public: int):
        sql = "insert into Article(title,content,public) values(%s,%s,%s);"
        try:
            async with self.conn.cursor() as cur:
                await cur.execute(sql, (title, content, public))
                await self.conn.commit()
                sql = "select id from Article where title=%s;"
                await cur.execute(sql, (title,))
                return await cur.fetchone()
        except Exception as e:
            logger.error(e)
            return None

    async def select_articles(self, start: int, limit: int, label_id: int):
        if start == -1:
            start = 0
        if limit == -1:
            limit = 10
        if label_id is None:
            sql = "select * from {0} order by created_at limit %s,%s;" \
                .format(self.table)
            query = (start, limit)
        else:
            sql = "select * from {0} where id in " \
                  "(select article_id from ArticleLabel where label_id=%s) " \
                  "order by created_at limit %s,%s;".format(self.table)
            query = (label_id, start, limit)
        try:
            async with self.conn.cursor() as cur:
                await cur.execute(sql, query)
                comments = await cur.fetchall()
            return comments
        except Exception as e:
            logger.error(e)
            return None

    async def handle_article_label(self, article_id: int, label_id: int, insert: bool = True):
        if insert:
            sql = "insert into ArticleLabel(article_id, label_id) values (%s,%s);"
        else:
            sql = "delete from ArticleLabel where article_id=%s and label_id=%s"
        try:
            async with self.conn.cursor() as cur:
                count = await cur.execute(sql, (article_id, label_id))
                await self.conn.commit()
            return count
        except Exception as e:
            logger.error(e)
            return -1
