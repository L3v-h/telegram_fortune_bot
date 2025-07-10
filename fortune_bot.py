import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

PREDICTIONS = [
    "Today feels like a honey-sweet day ahead!",
    "The forest whispers: trust your instincts.",
    "Something unexpected and lovely will find you soon.",
    "A good nap solves more than you think — try it!",
    "Even bears get lost — but they always find their way.",
    "Your path is yours alone. Walk it proudly.",
    "A cozy moment is coming. Savor it.",
    "Let go of the worry — it's not your size.",
    "Someone out there is grateful for you.",
    "Be kind, even to grumpy squirrels. Especially them."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🧸 Get a fortune", callback_data="get_fortune")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Hello there, friend! I’m the forest bear of fortune.\nPress the button below to receive a cozy prediction.",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    prediction = random.choice(PREDICTIONS)
    await query.edit_message_text(text=f"🧸 Your bear fortune:\n\n{prediction}")

def main():
    TOKEN = "7901742836:AAExhlLBU6qEmiR0dmjAVfGlxPkmTT2mvHU"
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
