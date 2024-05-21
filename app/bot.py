from aiogram import Bot, Dispatcher
from aiogram.types import Message
from services import DataPipeline
from settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def send_answer(message: Message):
    answer = await DataPipeline(message.text).execute()
    await message.reply(text=answer)


if __name__ == '__main__':
    dp.run_polling(bot)
