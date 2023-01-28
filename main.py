import config
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(config.token)  # Put your bot token here
dp = Dispatcher(bot)

openai.api_key = config.api_key  # Put your OpenAI api key here


# /start command text
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Можешь задать мне любой вопрос")


# /help command text
@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply("К сожалению специалистов порекомендовать не могу ;(")


@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You:"]
    )

    await message.answer(response['choices'][0]['text'])


executor.start_polling(dp, skip_updates=True)
