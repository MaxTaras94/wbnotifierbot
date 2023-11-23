from telegram import Update
from telegram.ext import ContextTypes

from wbnotifierbot.handlers.response import send_response
from wbnotifierbot.templates import render_template


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(response=render_template("help.j2"), update=update, context=context )
