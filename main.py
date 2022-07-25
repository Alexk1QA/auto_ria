
from aiogram.utils import executor

import handler.handlers
from bot_init import dp
from handler import *


handler.handlers.register_handler_command(dp)

handlers_bu.register_handler_command_bu(dp)
handlers_bu_inline.register_handler_command_bu_inline(dp)


executor.start_polling(dp, skip_updates=True)
