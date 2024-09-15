from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from supabase import create_client, Client

class SupabaseMiddleware(BaseMiddleware):
    def __init__(self, url: str, key: str):
        self.supabase_url = url
        self.supabase_key = key
        self.supabase: Client = create_client(self.supabase_url, self.supabase_key)

    async def __call__(self, handler, event: TelegramObject, data: dict):
        # Attach the Supabase client to the data dict
        data['supabase'] = self.supabase
        return await handler(event, data)
