import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
BANK_CHANNEL_ID = os.getenv("BANK_CHANNEL_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Bank Konten Lu & Ra aktif! Kirim foto/video ke sini.\nKetik /id buat cek ID.")

async def cek_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Chat ID: {update.effective_chat.id}\nUser ID: {update.effective_user.id}")

async def save_konten(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.copy_message(chat_id=int(BANK_CHANNEL_ID), from_chat_id=update.effective_chat.id, message_id=update.message.message_id)
        await update.message.reply_text("✅ Disimpen ke Bank!")
    except Exception as e:
        await update.message.reply_text(f"Gagal: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("id", cek_id))
    app.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO | filters.Document.ALL, save_konten))
    app.run_polling()

if __name__ == "__main__":
    main()
