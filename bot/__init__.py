class DummyDB:
    async def add_user(self, *args, **kwargs):
        pass

    async def is_user_exist(self, *args, **kwargs):
        return False

    async def get_all_users(self, *args, **kwargs):
        return []

    async def total_users_count(self, *args, **kwargs):
        return 0

    async def delete_user(self, *args, **kwargs):
        pass

    async def set_config(self, *args, **kwargs):
        pass

    async def get_config(self, *args, **kwargs):
        return None

    async def save_file(self, *args, **kwargs):
        pass

    async def get_file(self, *args, **kwargs):
        return None


class Database:
    def __init__(self):
        self.users = DummyDB()
        self.config = DummyDB()
        self.files = DummyDB()


db = Database()
