from apps.database import BaseModel
from apps import logger


class Article(BaseModel):
    table = 'Article'

    async def insert_article(self, title, content):
        sql = "insert into Article(title,content) values(%s,%s);"
        try:
            async with self.conn.cursor() as cur:
                await cur.execute(sql, (title, content))
                await self.conn.commit()
                sql = "select id from Article where title=%s";
                await cur.execute(sql, (title,))
                return await cur.fetchone()
        except Exception as e:
            logger.error(e)
            return None

    async def select_articles(self, start, limit, label):
        if start == -1:
            start = 0
        if limit == -1:
            limit = 10
        if label == '':
            sql = "select * from {0} order by created_at limit %s,%s;" \
                .format(self.table)
            query = (start, limit)
        else:
            sql = """
                select * from {0} where id in
                (select article_id from ArticleLabel where label=%s)
                order by created_at limit %s,%s;
            """.format(self.table)
            query = (label, start, limit)
        try:
            async with self.conn.cursor() as cur:
                await cur.execute(sql, query)
                comments = await cur.fetchall()
            return comments
        except Exception as e:
            logger.error(e)
            return None

    async def handle_article_label(self, article_id, label, insert: bool = True):
        if insert:
            sql = "insert into ArticleLabel(article_id, label) values (%s,%s);"
        else:
            sql = "delete from ArticleLabel where article_id=%s and label=%s"
        try:
            async with self.conn.cursor() as cur:
                count = await cur.execute(sql, (article_id, label))
                await self.conn.commit()
            return count
        except Exception as e:
            logger.error(e)
            return -1
