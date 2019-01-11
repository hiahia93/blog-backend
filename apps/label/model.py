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
                if count > 0:
                    sql = "select id from Label where label=%s;"
                    await cur.execute(sql, label)
                    one = await cur.fetchone()
                    return one
                else:
                    return None
        except Exception as e:
            logger.error(e)
            return None

    async def binding_labels(self, article_id: int, labels: list):
        try:
            async with self.conn.cursor() as cur:
                for l in labels:
                    tmp_sql = 'select label from {0} where id=%s;'.format(self.table)
                    await cur.execute(tmp_sql, (l,))
                    one = await cur.fetchone()
                    if one is None:
                        labels.pop(labels.index(l))
                if len(labels) > 0:
                    sql = "insert into ArticleLabel(article_id, label_id) VALUES (%s,%s);"
                    data = []
                    for l in labels:
                        data.append((article_id, l))
                    count = await cur.executemany(sql, data)
                    await self.conn.commit()
                    return count
                return 0
        except Exception as e:
            logger.error(e)
            return -1

    async def select_article_labels(self, article_id):
        sql = "select id, label from {0} where id in " \
              "(select label_id from ArticleLabel where article_id=%s);" \
              .format(self.table)
        try:
            async with self.conn.cursor() as cur:
                await cur.execute(sql, (article_id,))
                labels = await cur.fetchall()
            return labels
        except Exception as e:
            logger.error(e)
            return None

    async def select_labels(self):
        sql = 'select id,label from {0} order by label;'.format(self.table)
        try:
            async with self.conn.cursor() as cur:
                await cur.execute(sql)
                labels = await cur.fetchall()
            return labels
        except Exception as e:
            logger.error(e)
            return None