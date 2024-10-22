from aiogram import Bot, Dispatcher, types, F
from contextlib import suppress
import asyncio
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder 
from aiogram.types.web_app_info import WebAppInfo

TOKEN = '7527223108:AAEninRPQVXmp1Xr53Os74P0DB9mktNA1Ro'


bot = Bot(TOKEN)
dp = Dispatcher()

site = FSInputFile('Stalin.html')

def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Начать игру", web_app=WebAppInfo(url = 'Stalin.html'))],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

@dp.message(Command('start'))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer_photo(photo='https://postimg.cc/ygBrsQxt', caption='Привет! Добро пожаловать в Stalin Kombat\nОтныне ты — директор\nКакой? Выбирай сам. Тапай по экрану, собирай монеты, качай пассивный доход, разрабатывай\nсобственную стратегию дохода.\n\nПро друзей не забывай — зови их в игру и получайте вместе ещё больше монет!', reply_markup=ease_link_kb())
        
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
    