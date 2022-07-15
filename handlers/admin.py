from aiogram import types, Dispatcher
from config import ADMIN


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.answer("Ты не мой БОСС!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await message.bot.kick_chat_member(
                message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
            await message.answer(f"Пользователь {message.reply_to_message.from_user.full_name} "
                                 f"был забанен по воле {message.from_user.full_name}")
    else:
        await message.answer("Это работает только в чатах!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')