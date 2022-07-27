import os
from builtins import print

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
from bot.src.app.factories.MessageFactory import get_message
from bot.src.app.factories import KeyboardFactory
from bot.src.domain.managers import UserManager, BazaarManager

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

all_days = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
    'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'
]


@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    if msg.from_user.is_bot:
        return

    user = UserManager.UserManager().retrieve(msg.from_user.id)

    if user is None:
        await UserManager.UserManager().add(msg.from_user)

    menu = KeyboardFactory.get_keyboard(msg.from_user.language_code)
    message = get_message(
        "Hello $name!\n\n«Remember to get affordable and healthy foods with my daily notifications about marketplaces "
        "in Alanya»\nYour best guide — nomad_bazaar.\n\nContact me via nomadbazaar.bot@gmail.com if you spot a mistake"
        " or have an offer.",
        msg.from_user.language_code,
        name=msg.from_user.first_name
    )
    await msg.answer(message, reply_markup=menu)


@dp.message_handler(lambda m: m.text in all_days)
async def send_welcome(msg: types.Message):
    if msg.from_user.is_bot:
        return

    try:
        user = UserManager.UserManager().retrieve(msg.from_user.id)

        if user is None:
            await msg.answer(get_message("Please run /start command", msg.from_user.language_code))
            return

        if msg.from_user.language_code != 'ru':
            msg.from_user.language_code = 'en'

        bazaar_message = BazaarManager.BazaarManager().get_all(msg.text, msg.from_user.language_code)

        if bazaar_message:
            message = bazaar_message
        else:
            message = get_message('I`m lost', msg.from_user.language_code)

        menu = KeyboardFactory.get_keyboard(msg.from_user.language_code)
        await msg.answer(message, parse_mode='HTML', reply_markup=menu, disable_web_page_preview=True)
    except KeyError as e:
        print(e)
        await msg.answer(get_message('Bot got sunstroke', msg.from_user.language_code))


if __name__ == '__main__':
    executor.start_polling(dp)
