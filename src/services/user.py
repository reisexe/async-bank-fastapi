import bcrypt

from src.database import database
from src.models.user import users

class UserService:
    async def create(self, username: str, password: str) -> int:
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        command = users.insert().values(username=username, password=hashed)
        return await database.execute(command)

    async def get_by_username(self, username: str):
        query = users.select().where(users.c.username == username)
        return await database.fetch_one(query)

    def verify_password(self, plain: str, hashed: str) -> bool:
        return bcrypt.checkpw(plain.encode(), hashed.encode())