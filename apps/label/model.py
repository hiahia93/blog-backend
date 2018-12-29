from apps.database import BaseModel
from apps import logger


class Label(BaseModel):

    table = 'Label'

    async def insert_label(self, label: str):
        sql = "insert into Label(label) values(%s);"
        try:
            async with self.conn.cursor() as cur:
                count = await cur.execute(sql, label)
                await self.conn.commit()
            return count
        except Exception as e:
            logger.error(e)
            return -1

    async def binding_labels(self, article_id: int, labels: list):
        sql = "insert into {0}(label) values(%s);".format(self.table)
        data = []
        try:
            async with self.conn.cursor() as cur:
                for l in labels:
                    tmp_sql = 'select label from {0} where label=%s;'.format(self.table)
                    await cur.execute(tmp_sql, (l,))
                    one = await cur.fetchone()
                    if one is None:
                        data.append((l,))
                if len(data) > 0:
                    await cur.executemany(sql, data)
                    await self.conn.commit()
                sql = "insert into ArticleLabel(article_id, label) VALUES (%s,%s);"
                data = []
                for l in labels:
                    data.append((article_id, l))
                count = await cur.executemany(sql, data)
                await self.conn.commit()
            return count
        except Exception as e:
            logger.error(e)
            return -1

    async def select_article_labels(self, article_id, *fields):
        sql = 'select label from ArticleLabel where article_id=%s;'
        try:
            async with self.conn.cursor() as cur:
                await cur.execute(sql, (article_id,))
                labels = await cur.fetchall()
            return labels
        except Exception as e:
            logger.error(e)
            return None

    async def select_labels(self):
        sql = 'select * from {0} order by label;'.format(self.table)
        try:
            async with self.conn.cursor() as cur:
                await cur.execute(sql)
                labels = cur.fetchall()
            return labels
        except Exception as e:
            logger.error(e)
            return None