import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode

BOT_TOKEN = "7991652167:AAFqUkHIqxhdBMtX9r76XqN-DL-zrPNRuZw"
TARGET_CHAT_ID = 1234567890  # сюда ID, куда пересылать фото

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.photo)
async def handle_photo(message: Message):
    # Берём самое большое фото
    largest_photo = message.photo[-1]

    # Пересылаем фото по нужному ID
    await bot.send_photo(
        chat_id=TARGET_CHAT_ID,
        photo=largest_photo.file_id,
        caption=f"Фото от пользователя {message.from_user.id}"
    )

    await message.answer("Фото получено и переслано.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
