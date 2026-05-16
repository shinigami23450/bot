import telebot

TOKEN = "7991652167:AAFqUkHIqxhdBMtX9r76XqN-DL-zrPNRuZw"
TARGET_ID = 1414933285  # сюда вставь свой Telegram ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["ids"])
def get_id(message):
    bot.reply_to(message, f"Твой ID: {message.from_user.id}")


@bot.message_handler(func=lambda message: True, content_types=[
    "text", "photo", "video", "document", "audio",
    "voice", "sticker", "location", "contact"
])
def forward_all(message):
    try:
        bot.forward_message(
            chat_id=TARGET_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )
    except Exception as e:
        print(e)


def f():
    pass

bot.infinity_polling()