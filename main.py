
from aiogram.utils import executor

import handler.handlers
from bot_init import dp
from handler import *

handlers_bu.register_handler_command(dp)
handler.handlers.register_handler_command(dp)


executor.start_polling(dp, skip_updates=True)
