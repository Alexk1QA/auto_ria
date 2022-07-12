
from aiogram.utils import executor
from bot_init import dp
from handler import handlers

handlers.register_handler_command(dp)


executor.start_polling(dp, skip_updates=True)