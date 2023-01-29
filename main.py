import config
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot()  # Put your bot token here
dp = Dispatcher(bot)

openai.api_key = config.api_key  # Put your OpenAI api key here


# /start command text
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hey! You can ask me any question")


# /help command text
@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply("You can use this bot as a browser\nYou can also use it as an interlocutor if you are bored\nHe can even code for you in any programming language!")


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
