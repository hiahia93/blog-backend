from apps.database import BaseModel
from apps import logger


class User(BaseModel):

    table = 'User'

    async def insert_user(self, id, pwd, email):
        sql = "insert into User(id,password,nickname,email) values(%s,%s,%s,%s);"
        try:
            async with self.conn.cursor() as cur:
                count = await cur.execute(sql, (id, pwd, id, email))
                await self.conn.commit()
            return count
        except Exception as e:
            logger.error(e)
            return -1