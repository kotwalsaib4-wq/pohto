import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# --- ستاسو معلومات ---
BOT_TOKEN = "8737718436:AAGEkqwayT058tBVH_Pp-W2T0B-aaJXMylU"
CHAT_ID = "8295417969"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """کله چې عکس راشي، خوندي یې کړي"""
    try:
        photo = update.message.photo[-1]  # غوره کیفیت
        file = await photo.get_file()
        
        # د عکس خوندي کولو لپاره فولډر جوړول
        os.makedirs("received_photos", exist_ok=True)
        
        # عکس خوندي کول
        file_path = f"received_photos/photo_{update.message.message_id}.jpg"
        await file.download_to_drive(file_path)
        
        print(f"✅ نوی عکس ترلاسه شو: {file_path}")
        await update.message.reply_text("✅ ستا عکس ترلاسه شو!")
        
    except Exception as e:
        print(f"❌ تېروتنه: {e}")
        await update.message.reply_text("❌ تېروتنه رامنځ ته شوه!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    print("🤖 بوټ روان دی... د عکسونو انتظار کې")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
