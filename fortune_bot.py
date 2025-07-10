import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔮 Список предсказаний
PREDICTIONS = [
    "Сегодня твой день — используй его мудро!",
    "Впереди перемены, не бойся их.",
    "Ты получишь приятную новость совсем скоро.",
    "Оглянись — кто-то рядом нуждается в тебе.",
    "Улыбнись, и удача обязательно заглянет!",
    "То, что ты ищешь, уже ищет тебя.",
    "День будет лучше, чем ты думаешь.",
    "Иногда, чтобы всё изменить, нужно просто начать.",
    "Скоро ты окажешься там, где должен быть.",
    "Твоя энергия вдохновляет других — продолжай!"
]

# /start команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🔮 Дать предсказание", callback_data="get_fortune")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Нажми кнопку ниже, чтобы получить предсказание:", reply_markup=reply_markup)

# Обработка кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    prediction = random.choice(PREDICTIONS)
    await query.edit_message_text(f"🔮 Твоё предсказание:\n\n{prediction}")

# Запуск бота
def main():
    TOKEN = "7901742836:AAExhlLBU6qEmiR0dmjAVfGlxPkmTT2mvHU"
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
