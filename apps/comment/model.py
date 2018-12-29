from apps.database import BaseModel
from apps import logger


class Comment(BaseModel):

    table = 'Comment'

    async def insert_comment(self, article_id, content):
        sql = "insert into Comment(article_id, content) values(%s, %s);"
        try:
            async with self.conn.cursor() as cur:
                tmp_sql = 'select id from Article where id=%s;'
                await cur.execute(tmp_sql, (article_id,))
                one = await cur.fetchone()
                if one is None:
                    return -1
                count = await cur.execute(sql, (article_id, content))
                await self.conn.commit()
                return count
        except Exception as e:
            logger.error(e)
            return -1

    async def select_article_comments(self, article_id, start, limit):
        if start == -1:
            start = 0
        if limit == -1:
            limit = 10
        if start < 100:
            sql = 'select id,content,created_at from {0} where article_id=%s order by created_at limit %s,%s;'\
                .format(self.table)
        else:
            sql = """
            select id,content,created_at from {0} where id >=
            (select id from {1} where article_id=%s order by created_by limit %s,1) 
            limit %s;
            """.format(self.table, self.table)
        try:
            async with self.conn.cursor() as cur:
                await cur.execute(sql, (article_id, start, limit))
                comments = await cur.fetchall()
            return comments
        except Exception as e:
            logger.error(e)
            return None