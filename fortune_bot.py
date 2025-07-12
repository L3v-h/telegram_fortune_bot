import random
import json
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

PREDICTIONS = [
    "🌕 The moon says Bitcoin’s about to blast off… but don’t forget your spacesuit, astronaut trader.",
    "🌙 That NFT you scoffed at? It’s about to be the next digital Mona Lisa — grab your popcorn.",
    "🌑 Ethereum’s gas fees might dip lower than your morning coffee price today. Time to flex those DeFi muscles!",
    "🌝 Dogecoin’s wagging its tail toward the moon again — better leash your portfolio tight.",
    "🌘 The lunar bear senses a dip incoming. Buy the dip? More like hug the dip.",
    "🌔 Your favorite altcoin is moonwalking on Wall Street’s lunar stage — don’t blink or you’ll miss it.",
    "🌙 NFT market looks as busy as a New York subway at rush hour. Pick your ride wisely.",
    "🌕 Crypto winter? More like a lunar breeze. Time to layer up or HODL like a boss.",
    "🌑 Watch out for pump-and-dump shadows lurking like street vendors in Times Square.",
    "🌝 Your wallet’s about to feel as full as a New York pizza box after a late-night order.",
    "Lunar bear’s tip: Coinbase might toss some surprises your way faster than a subway train.",
    "If Bitcoin was a Broadway show, it’d be sold out through the next lunar cycle.",
    "NFT collectibles are hotter than a Brooklyn rooftop BBQ in July — snag ‘em before they’re gone.",
    "The moon whispers: DeFi protocols could throw you a ‘Big Apple’ style curveball.",
    "Your favorite token’s about to grow like a Wall Street skyscraper — tall and unstoppable.",
    "Lunar bear says: don’t let FOMO hit you harder than NYC traffic at 5 PM.",
    "Ethereum NFTs are flying off digital shelves like hotcakes at a Brooklyn diner.",
    "Watch those crypto swings like you watch the Yankees—always expect surprises.",
    "Your NFT might soon be worth more than a Times Square billboard ad.",
    "Moon bear predicts: gas fees could drop lower than Manhattan rent (well, almost).",
    "Satoshi’s ghost just winked — maybe time to stack more BTC before the next lunar cycle.",
    "The lunar tides suggest a sudden surge in meme coins — invest at your own risk (and laughs).",
    "NFT drops today will be more crowded than a Saturday at Central Park.",
    "Crypto whales might be sneaking around like subway rats—keep an eye on your tokens.",
    "The moon’s glow says your DeFi stake might blossom like NYC spring flowers.",
    "Buy low, sell high? Lunar bear prefers ‘hold tight and enjoy the cosmic ride’.",
    "Your portfolio’s about to bounce like a Harlem Globetrotters’ ball.",
    "Watch for moon phases—sometimes they align with crypto gains, sometimes with traffic jams.",
    "Lunar bear advice: diversify like you’d pick pizza toppings — a little of everything.",
    "The NFT you ignored last week? Could become the next Brooklyn street art sensation.",
    "Bitcoin might do a Times Square ball drop, but sideways for a while — patience, young trader.",
    "The moon hints that your favorite altcoin could skyrocket faster than NYC skyscraper elevators.",
    "Crypto market volatility? Just think of it as the subway delays of investing.",
    "NFTs with ‘moon’ in the title are about to become collector’s gold.",
    "Moon bear suggests: stash some tokens before the next big Wall Street crypto party.",
    "The lunar glow predicts Ethereum might surprise you with a gas fee discount.",
    "Your wallet’s gonna feel fatter than a Manhattan cheesecake this week.",
    "Lunar bear’s warning: avoid scams slicker than a Times Square hustler.",
    "The NFT scene is buzzing louder than a New York City street musician.",
    "Bitcoin’s path could curve like a NYC taxi at rush hour — unpredictable but exciting.",
    "Moon phases affect more than tides — maybe your portfolio too. HODL through the full moon!",
    "DeFi farming could get as juicy as summer in the Hamptons.",
    "The lunar bear suspects your crypto stash might soon hit a new high score.",
    "NFT auctions today will be hotter than Brooklyn summer rooftops.",
    "Keep your wallet close, and your passwords closer — scams lurk like rats in the subway tunnels.",
    "The moon says: ‘Don’t sell out before the big show — crypto’s encore is coming.’",
    "Your portfolio is about to take a New York minute to grow — fast and furious.",
    "Lunar bear thinks: expect some ‘moonshots’ that could turn pennies into Lambos.",
    "NFT collections with urban vibes might be the next big craze.",
    "Bitcoin could bounce like a basketball in Madison Square Garden tonight.",
    "Lunar bear’s advice: don’t get lost in the ‘FUD subway’—trust the moonlight instead.",
    "Ethereum’s upgrade might feel like a NYC power surge — sudden and impactful.",
    "Your crypto could spike like the Empire State Building lights during a celebration.",
    "NFTs with a backstory might sell faster than street food in Queens.",
    "Moon phases suggest your favorite token might dance like a Broadway star.",
    "The lunar bear says: stay calm during dips — even NYC has rainy days.",
    "Crypto whales might move stealthier than Times Square crowds after midnight.",
    "Your portfolio might light up like the Brooklyn Bridge at night.",
    "Lunar bear predicts: some tokens will shine brighter than the Statue of Liberty torch.",
    "NFT hype could be as viral as a subway flash mob.",
    "Moonlight reveals: now’s a good time to stack stablecoins for upcoming action.",
    "Bitcoin might behave like a taxi driver — unpredictable but always moving forward.",
    "NFT drops today are more crowded than Grand Central at rush hour.",
    "The lunar bear advises: watch out for ‘moonlighting’ scammers in disguise.",
    "Ethereum could see a ‘gas fee holiday’ — time to mint that rare NFT.",
    "Your crypto journey might feel like a Broadway musical — full of drama and applause.",
    "Lunar bear whispers: ‘Pump and dumps are like subway delays — frustrating but temporary.’",
    "NFTs tied to urban art might become the next cultural phenomenon.",
    "Bitcoin might climb higher than the Chrysler Building this week.",
    "Your portfolio could glow like NYC’s skyline on a clear night.",
    "Lunar bear says: DeFi yields may shine brighter than Times Square billboards.",
    "Watch your tokens like a New Yorker watches their coffee — carefully and with love.",
    "NFT marketplaces might get busier than a Brooklyn flea market.",
    "Bitcoin’s next move might surprise you like a sudden subway performance.",
    "Lunar bear suggests: keep your private keys safer than your NYC apartment keys.",
    "Crypto volatility could hit harder than a New York snowstorm.",
    "NFT hype might explode like Fourth of July fireworks over the Hudson.",
    "The moon predicts some altcoins will have their own ‘Wall Street moment.’",
    "Your portfolio might get a boost like morning coffee at a NYC diner.",
    "Lunar bear reminds: don’t chase every shiny token — some are just lunar illusions.",
    "Bitcoin’s price might swing like a NYC cabbie on a Friday night — hold tight!",
    "NFT art inspired by urban legends could be next on the lunar bear’s hit list.",
    "DeFi protocols might offer yields sweeter than New York cheesecake.",
    "Your crypto wallet could fill up faster than a NYC subway car at rush hour.",
    "Lunar bear warns: beware of quick flips — they burn faster than Times Square neon.",
    "Ethereum’s upcoming update might shine like the Empire State Building’s lights.",
    "NFT drops from local artists could moon like Brooklyn’s art scene.",
    "Bitcoin could ride a wave as high as Coney Island’s roller coaster.",
    "Your portfolio’s growth might feel as steady as a classic NYC skyline.",
    "Lunar bear says: sometimes you gotta HODL through the subway stops to reach your destination.",
    "NFT collectors today are buzzing like bees on a rooftop garden in Manhattan.",
    "Bitcoin might dance through the market like a street performer in Union Square.",
    "DeFi yields could surprise you like a free pizza slice in the city.",
    "The moon suggests: invest wisely — don’t get caught in the hype subway car.",
    "Your tokens might shine brighter than Broadway’s marquee lights.",
    "Lunar bear’s advice: keep calm and HODL on — the moon is watching.",
    "NFTs themed around NYC landmarks could be the next big thing.",
    "Bitcoin might take you on a ride wilder than the Staten Island Ferry.",
    "Your portfolio could bloom like Central Park in spring.",
    "Lunar bear whispers: patience, young trader — the moon’s light always returns.",
    "Crypto gains might hit you like a New York minute — fast and unforgettable."
]
# Максимум одно предсказание в день
COOLDOWN_HOURS = 24
USERDATA_FILE = "users.json"

# Загружаем user_data из файла
def load_user_data():
    if os.path.exists(USERDATA_FILE):
        with open(USERDATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Сохраняем user_data в файл
def save_user_data(data):
    with open(USERDATA_FILE, "w") as f:
        json.dump(data, f)

user_data = load_user_data()

def can_user_predict(user_id: str):
    now = datetime.utcnow()
    data = user_data.get(user_id)

    if not data:
        return True, ""

    last_time = datetime.fromisoformat(data["last_time"])
    if now - last_time > timedelta(hours=COOLDOWN_HOURS):
        return True, ""
    remaining = timedelta(hours=COOLDOWN_HOURS) - (now - last_time)
    hrs, rem = divmod(remaining.seconds, 3600)
    mins = rem // 60
    return False, f"🌙 You’ve already received your prediction. Try again in {hrs}h {mins}m."

# Команда /start или переход из канала
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🌙 Get Lunar Bear's Prediction", callback_data="get_fortune")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🌙 I am the Lunar Bear.\nPress the button below to receive your crypto & Telegram gift prediction.",
        reply_markup=reply_markup
    )

# Обработка кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = str(query.from_user.id)
    await query.answer()

    allowed, msg = can_user_predict(user_id)
    if not allowed:
        await query.edit_message_text(msg)
        return

    # Обновляем время предсказания
    user_data[user_id] = {"last_time": datetime.utcnow().isoformat()}
    save_user_data(user_data)

    prediction = random.choice(PREDICTIONS)
    await query.edit_message_text(
        f"🌙 Your prediction:\n\n{prediction}\n\nCome back tomorrow for another one!"
    )

# Команда /Prediction — в канале
async def prediction_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    allowed, msg = can_user_predict(user_id)
    if not allowed:
        await update.message.reply_text(msg)
        return

    # Обновляем дату предсказания
    user_data[user_id] = {"last_time": datetime.utcnow().isoformat()}
    save_user_data(user_data)

    prediction = random.choice(PREDICTIONS)
    await update.message.reply_text(
        f"🌙 Your Lunar Bear prediction:\n\n{prediction}\n\n🕒 Come back tomorrow for another one!"
    )

def main():
    TOKEN = "7901742836:AAExhlLBU6qEmiR0dmjAVfGlxPkmTT2mvHU"  # ← Вставь свой токен
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("Prediction", prediction_command))
    app.add_handler(CallbackQueryHandler(button))

    print("🌙 Lunar Bear is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
