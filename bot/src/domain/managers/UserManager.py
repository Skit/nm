from bot.src.domain.repositories.UsersRepository import UsersRepository


class UserManager(UsersRepository):

    async def add(self, from_user):
        await self.add_user(
            from_user.id,
            from_user.first_name,
            from_user.last_name,
            from_user.username,
            from_user.language_code
        )
