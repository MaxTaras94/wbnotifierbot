
from telegram import Chat, Update
from telegram.ext import ContextTypes
from typing import cast
from wbnotifierbot.handlers.response import send_response
from wbnotifierbot.service.check_user_is_admin import is_user_admin
from wbnotifierbot.templates import render_template


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if is_user_admin(cast(Chat, update.effective_chat).id):
        await send_response(update, context, 
                            response=render_template(
                                            "start_4_admin.j2", 
                                             data={"name":update.message.from_user.username}
                            )
        )
    else:
        await send_response(update, context, response=render_template("start.j2"))