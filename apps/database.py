
import aiomysql

from apps import logger, cf


class BaseModel:

    table = ''

    def __init__(self):
        self.conn = None

    async def connect(self):
        self.conn = await aiomysql.connect(
            host=cf.get('mysql', 'host'),
            port=int(cf.get('mysql', 'port')),
            user=cf.get('mysql', 'user'),
            password=cf.get('mysql', 'pwd'),
            db=cf.get('mysql', 'db')
        )

    async def select(self, id, *fields):
        if len(fields) == 0:
            sql = "select id from {0} where id=%s;".format(self.table)
        else:
            sql = "select {0} from {1} where id=%s".format(BaseModel.build_fields(*fields), self.table)
        try:
            async with self.conn.cursor() as cur:
                await cur.execute(sql, (id,))
                result = await cur.fetchone()
                return result
        except Exception as e:
            logger.error(e)
            return None

    async def update(self, id, fields: dict):
        sql = 'update {0} set {1} where id=%s;'.format(self.table, BaseModel.set_fields(fields))
        try:
            async with self.conn.cursor() as cur:
                count = await cur.execute(sql, tuple(fields.values()) + (id,))
                await self.conn.commit()
                return count
        except Exception as e:
            logger.error(e)
            return -1

    async def delete(self, id):
        sql = "delete from {0} where id=%s".format(self.table)
        try:
            async with self.conn.cursor() as cur:
                count = await cur.execute(sql, (id,))
                await self.conn.commit()
                return count
        except Exception as e:
            logger.error(e)
            return -1

    @staticmethod
    def build_fields(*fields):
        tmp = ''
        for f in fields:
            tmp += f + ','
        return tmp[:len(tmp) - 1]

    @staticmethod
    def set_fields(fields: dict):
        result = ''
        for key in fields.keys():
            result += '{0}=%s,'.format(key)
        return result[:len(result) - 1]

    def __del__(self):
        self.conn.close()
