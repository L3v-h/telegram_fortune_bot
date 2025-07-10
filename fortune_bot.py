import random
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# 🌙 Список предсказаний Лунного Медведя
PREDICTIONS = ["🌙 Lunar Bear says: Your crypto portfolio will shine under the moonlight tonight.",
    "🌙 Lunar Bear advice: Hold your coins tight, Telegram gifts might surprise you soon!",
    "🌙 The moon guides you to double-check your wallet security today.",
    "🌙 Beware of quick pumps, slow and steady wins the blockchain race.",
    "🌙 Lunar Bear sees a Telegram gift drop approaching — stay alert!",
    "🌙 Today is a perfect day to explore new crypto tokens cautiously.",
    "🌙 Lunar Bear whispers: Don’t share your private keys, no matter what.",
    "🌙 Your Telegram friends might send you a surprise soon — stay connected.",
    "🌙 The moonlight favors those who diversify their investments.",
    "🌙 Check your notifications, a gift might be waiting in your Telegram.",
    "🌙 Lunar Bear advises: Avoid FOMO — fear of missing out.",
    "🌙 The blockchain’s rhythm matches your heartbeat — trust your instincts.",
    "🌙 Small daily investments will grow stronger under the lunar sky.",
    "🌙 Telegram channels you follow could reveal hidden gems soon.",
    "🌙 Today, review your crypto wallet’s backup — better safe than sorry.",
    "🌙 The lunar bear encourages you to learn something new about NFTs.",
    "🌙 Gifts in Telegram are like moonbeams — unexpected and bright.",
    "🌙 Your crypto patience will pay off in the next moon cycle.",
    "🌙 Lunar Bear says: Trust only verified Telegram sources.",
    "🌙 It’s time to set realistic goals for your crypto journey.",
    "🌙 The moon favors calm traders over impulsive ones.",
    "🌙 Telegram stickers might carry a lucky charm for you today.",
    "🌙 Lunar Bear reminds: Scams lurk in shadows — stay vigilant.",
    "🌙 Your portfolio will find balance soon — the moon guarantees it.",
    "🌙 Pay attention to your Telegram wallet alerts — they are clues.",
    "🌙 Lunar Bear suggests: Take breaks, mental clarity improves trades.",
    "🌙 The moonlight reveals hidden Telegram giveaways tonight.",
    "🌙 Keep your passwords strong, like the lunar bear’s claws.",
    "🌙 Your crypto gains may surprise you if you stay patient.",
    "🌙 Telegram gift bots might have a secret for the attentive.",
    "🌙 Lunar Bear’s wisdom: Never invest what you can’t afford to lose.",
    "🌙 The stars align for your next big crypto idea.",
    "🌙 Your Telegram community supports you — lean on them if needed.",
    "🌙 Lunar Bear notes: Trends fade, fundamentals stay strong.",
    "🌙 Today’s moon phase favors secure transactions.",
    "🌙 A Telegram gift from a friend could brighten your day.",
    "🌙 Patience and moonlight will guide your crypto trades.",
    "🌙 Lunar Bear reminds you to check for new Telegram crypto groups.",
    "🌙 Unexpected Telegram gifts are on the horizon.",
    "🌙 The moon says: Stay calm during market volatility.",
    "🌙 Protect your Telegram account with two-factor authentication.",
    "🌙 Lunar Bear encourages sharing knowledge about crypto safely.",
    "🌙 Today’s prediction: You’ll discover a new favorite crypto coin.",
    "🌙 Telegram chats might hold clues to upcoming giveaways.",
    "🌙 Lunar Bear’s advice: Stay humble and keep learning.",
    "🌙 Crypto luck shines brighter when you stay informed.",
    "🌙 Telegram gifts often come when least expected.",
    "🌙 The moonlight guides you to make balanced investment choices.",
    "🌙 Lunar Bear says: Avoid chasing pumps; trust the process.",
    "🌙 A Telegram friend may send you helpful crypto tips soon.",
    "🌙 The stars encourage diversifying your Telegram subscriptions.",
    "🌙 Keep your private keys as sacred as the moon’s secrets.",
    "🌙 Lunar Bear sees positive growth in your crypto path.",
    "🌙 Telegram gifts sometimes hide behind simple messages.",
    "🌙 Moonlight helps you spot scams before they strike.",
    "🌙 Trust your research; the moon backs your decisions.",
    "🌙 Today, send good vibes to your Telegram crypto community.",
    "🌙 Lunar Bear reminds: Use hardware wallets for safety.",
    "🌙 Your Telegram notifications hold more than just messages.",
    "🌙 The moon smiles on those who plan long-term.",
    "🌙 Lunar Bear whispers: Never rush your trades.",
    "🌙 A Telegram gift might come wrapped in a sticker pack.",
    "🌙 Crypto markets sleep, but the moon never rests.",
    "🌙 Protect your Telegram with strong, unique passwords.",
    "🌙 Lunar Bear predicts growth after a calm period.",
    "🌙 Check Telegram channels carefully for trustworthy info.",
    "🌙 The moon’s glow favors steady and consistent investing.",
    "🌙 Lunar Bear encourages you to review your security settings.",
    "🌙 Gifts in Telegram may come from unexpected contacts.",
    "🌙 Your crypto journey is a marathon, not a sprint.",
    "🌙 Lunar Bear says: Stay aware of market news.",
    "🌙 Today’s moon phase supports making smart moves.",
    "🌙 Telegram crypto bots might have new features soon.",
    "🌙 Trust the lunar cycle to guide your trading rhythm.",
    "🌙 Lunar Bear reminds you: Avoid sharing sensitive info.",
    "🌙 Your Telegram chats might lead to exciting opportunities.",
    "🌙 Moonlight helps you see the bigger crypto picture.",
    "🌙 Patience is the best strategy under the lunar sky.",
    "🌙 Lunar Bear says: Backup your wallets regularly.",
    "🌙 Telegram gift alerts could brighten your week.",
    "🌙 The moon inspires innovation in your crypto strategies.",
    "🌙 Stay curious and explore new Telegram crypto channels.",
    "🌙 Lunar Bear advises: Avoid hype and trust data.",
    "🌙 Your Telegram friends might surprise you with tips.",
    "🌙 The stars favor careful analysis today.",
    "🌙 Lunar Bear sees a calm market before the next wave.",
    "🌙 Telegram stickers carry more than just fun — stay tuned.",
    "🌙 Moonlight illuminates your path to crypto wisdom.",
    "🌙 Always verify Telegram sources before trusting info.",
    "🌙 Lunar Bear encourages protecting your privacy online.",
    "🌙 Your crypto patience will be rewarded soon.",
    "🌙 Telegram gifts often arrive when least expected.",
    "🌙 The moon guides you to steady growth, not quick wins.",
    "🌙 Lunar Bear says: Keep learning every day.",
    "🌙 Your Telegram community is a treasure — cherish it.",
    "🌙 Today is good for reviewing your crypto goals.",
    "🌙 Lunar Bear whispers: Trust the process, not the hype.",
    "🌙 Crypto moves slow under the calm lunar phases.",
    "🌙 Telegram gifts may come in mysterious ways.",
    "🌙 Stay safe and secure your Telegram and wallets well.",
    "🌙 Lunar Bear sees promising trends in your future.",
    "🌙 The moonlight shines on your dedication.",
    "🌙 Remember to rest — even crypto needs balance."]

# 🧵 Укажи сюда ID нужной темы в канале (узнаешь через /id)
ALLOWED_THREAD_ID = -1002195265419  # заменишь после

# ✅ Команда /Prediction
async def handle_prediction_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.message_thread_id != ALLOWED_THREAD_ID:
        return

    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("🔮 Reveal Prediction", callback_data="get_prediction")
    ]])

    await update.message.reply_text(
        "🌕 The Lunar Bear awaits...\nFor you, a single fortune can be unlocked.\n\nPress the button below to reveal your fate.",
        reply_markup=keyboard
    )

# 🔮 Кнопка — выдать предсказание
async def reveal_prediction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    prediction = random.choice(PREDICTIONS)
    await query.edit_message_text(
        f"🧸 Lunar Bear’s fortune for you:\n\n{prediction}"
    )

# 🆔 Вспомогательная команда /id — узнать thread_id
async def echo_thread_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    thread_id = update.message.message_thread_id
    chat_id = update.message.chat_id
    await update.message.reply_text(
        f"📌 Thread ID: {thread_id}\n💬 Chat ID: {chat_id}"
    )

# 🚀 Основной запуск
def main():
    TOKEN = "7901742836:AAExhlLBU6qEmiR0dmjAVfGlxPkmTT2mvHU"  # ← Вставь сюда свой токен

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("Prediction", handle_prediction_command))
    app.add_handler(CallbackQueryHandler(reveal_prediction, pattern="^get_prediction$"))
    app.add_handler(CommandHandler("id", echo_thread_id))  # только для вывода thread_id

    app.run_polling()

if __name__ == "__main__":
    main()
