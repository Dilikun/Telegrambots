from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API

LISTS_OF_COMMAND = '''
<b> /help - calls lists of commands </b>
<em> /give - sends sticker with cute cat </em> 
'''

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot successfully has been launched')


@dp.message_handler(commands=['help'])
async def help_command(message: types.message):
    await message.answer(LISTS_OF_COMMAND, parse_mode='HTML')


@dp.message_handler(content_types=['sticker'])
async def send_sticker(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await message.answer('Look at this cute cat ❤️')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgQAAxkBAAEJvbpkt-Z35T9YDMw-3kZMkieSUH5n3AAC4AkAAu9GYFGTgHavjO_HLi8E')

#
# @dp.message_handler()
# async def black_heart(message: types.Message):
#     if "❤️" in message.text:
#         await message.reply('🖤')


@dp.message_handler()
async def checkmark_count(message: types.Message):
    await message.answer(text=str(message.text.count('✅')))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)