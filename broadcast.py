import os
import asyncio
import aiohttp
import locale
import logging
from datetime import datetime, date
from aiogram import Bot, Dispatcher, types
from aiogram.utils import exceptions, executor
from dotenv import load_dotenv
from bot.src.app.factories import WeatherFactory, MessageFactory
from bot.src.domain.managers import BazaarManager, UserManager

load_dotenv()

API_TOKEN = os.getenv('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('broadcast')

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
bazaar_manager = BazaarManager.BazaarManager()
langCache = []
messageCache = []


async def send_message(user_id: int, text: str, disable_notification: bool = False) -> bool:
    try:
       await bot.send_message(user_id, text, disable_notification=disable_notification, disable_web_page_preview=True)
    except exceptions.BotBlocked:
        log.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        log.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message(user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        log.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        log.exception(f"Target [ID:{user_id}]: failed")
    else:
        log.info(f"Target [ID:{user_id}]: success")
        return True
    return False


async def broadcaster() -> int:
    weather = await get_weather()
    day_idx = datetime.now().weekday()
    daily = weather['daily'][day_idx]
    about_weather = WeatherFactory.get_text(round(daily['temp']['day']), daily['weather'])
    count = 0
    try:
        for user in get_users():
            lang = user[4]
            if lang == 'ru':
                locale.setlocale(category=locale.LC_ALL, locale="Russian")
            else:
                locale.setlocale(category=locale.LC_ALL, locale="English")

            if await send_message(
                    int(user[0]), get_full_message(date.today().strftime("%A").title(), about_weather, lang)
            ):
                count += 1
            await asyncio.sleep(.05)
    finally:
        log.info(f"{count} messages successful sent.")

    return count


def get_full_message(day: str, weather: str, lang: str):
    message = get_bazaar_message(day, lang)
    about_day = MessageFactory.get_message('Hello today is $day!', lang, day=day)
    hello = MessageFactory.get_message(' $day $data', lang, day=about_day, data=weather)
    return hello + "\n" + message + "\n"


def get_bazaar_message(day_abbr: str, language_code: str):
    if language_code not in langCache:
        langCache.append(language_code)
        messageCache.append(bazaar_manager.get_all(day_abbr, language_code))

    return messageCache[langCache.index(language_code)]


def get_users():
    return UserManager.UserManager().get_subscribers()


async def get_weather():
    async with aiohttp.ClientSession() as session:
        url = 'https://api.openweathermap.org/data/2.5/onecall?lat=36.651741&lon=32.023482&exclude=current,minutely,' \
              'hourly&units=metric&appid=' + os.getenv('WEATHER_TOKEN')
        async with session.get(url) as resp:
            return await resp.json()

if __name__ == '__main__':
    executor.start(dp, broadcaster())
