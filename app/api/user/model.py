from app.database import BaseModel
from app import logger


class User(BaseModel):

    table = 'User'

    async def insert_user(self, username, pwd, email):
        sql = "insert into User(id,password,nickname,email) values(%s,%s,%s,%s);"
        try:
            async with self.conn.cursor() as cur:
                count = await cur.execute(sql, (username, pwd, username, email))
                await self.conn.commit()
            return count
        except Exception as e:
            logger.error(e)
            return -1