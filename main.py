import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def send_message_to_api(payload: dict):
    url = "http://94.228.162.189:5678/webhook-test/Task"
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     return None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_id = update.message.chat.id

    payload = {
        "message": user_message,
        "chat_id": chat_id
    }
    await send_message_to_api(payload)
    print(f"Отправляем payload: {payload}")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Ошибка: {context.error}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.add_error_handler(error)

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()