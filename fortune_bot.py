import random
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔮 Здесь будут предсказания (вставим позже)
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

user_data = {}
MAX_DAILY_PREDICTIONS = 5
COOLDOWN_HOURS = 24

def can_user_predict(user_id: int) -> (bool, str):
    now = datetime.utcnow()
    if user_id not in user_data:
        return True, ""
    data = user_data[user_id]
    first_time = data["first_time"]
    count = data["count"]
    if now - first_time > timedelta(hours=COOLDOWN_HOURS):
        user_data[user_id] = {"count": 0, "first_time": now}
        return True, ""
    if count < MAX_DAILY_PREDICTIONS:
        return True, ""
    remaining = timedelta(hours=COOLDOWN_HOURS) - (now - first_time)
    hrs, rem = divmod(remaining.seconds, 3600)
    mins = rem // 60
    return False, f"You’ve reached your limit of {MAX_DAILY_PREDICTIONS} predictions today. Try again in {hrs}h {mins}m."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🌙 Get a lunar bear's prediction", callback_data="get_fortune")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🌙 Hello! I am the Lunar Bear, your modern guide to crypto and Telegram gifts.\nPress the button below to receive your fortune.",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    allowed, msg = can_user_predict(user_id)
    if not allowed:
        await query.edit_message_text(msg)
        return

    now = datetime.utcnow()
    if user_id not in user_data:
        user_data[user_id] = {"count": 1, "first_time": now}
    else:
        user_data[user_id]["count"] += 1

    if not PREDICTIONS:
        await query.edit_message_text("No predictions available yet. Please try again later.")
        return

    prediction = random.choice(PREDICTIONS)
    await query.edit_message_text(
        f"🌙 Your lunar bear prediction:\n\n{prediction}\n\n🎉 Prediction {user_data[user_id]['count']} of {MAX_DAILY_PREDICTIONS} today."
    )

def main():
    TOKEN = "7901742836:AAExhlLBU6qEmiR0dmjAVfGlxPkmTT2mvHU"
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Lunar Bear bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
