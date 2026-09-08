import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8737718436:AAGEkqwayT058tBVH_Pp-W2T0B-aaJXMylU"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """کله چې عکس راشي، خوندي یې کړي"""
    try:
        photo = update.message.photo[-1]  # غوره کیفیت
        file = await photo.get_file()
        
        os.makedirs("received_photos", exist_ok=True)
        file_path = f"received_photos/photo_{update.message.message_id}.jpg"
        await file.download_to_drive(file_path)
        
        print(f"✅ نوی عکس ترلاسه شو: {file_path}")
        
    except Exception as e:
        print(f"❌ تېروتنه: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """کله چې کارونکی /start واستوي"""
    await update.message.reply_text(
        "سلام! 👋\n\n"
        "د خپلو عکسونو لیږلو لپاره لاندې تڼۍ کلیک کړئ:\n"
        "[عکسونه واستوئ](https://your-domain.com)",
        parse_mode='Markdown'
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    print("🤖 بوټ روان دی...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
