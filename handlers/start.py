import jsons
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

import redisapi
from entity.User import User, serialize, deserialize
from dbapi import get_group_id_by_name



router = Router()  # [1]


@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    user = User(False, None)
    redisapi.set_value(message.chat.id, serialize(user))
    await message.answer(
        "Введите группу ...", reply_markup=ReplyKeyboardRemove()
    )

@router.message(Command("get"))  # [2]
async def cmd_start(message: Message):
    user = deserialize(redisapi.get_value(message.chat.id))
    await message.answer(
       "Status:"+str(user.auth) + " Group_id: "+ str(user.group)
    )

@router.message(F.text)
async def start_listening(message: Message):
    response = get_group_id_by_name(message.text)

    if response.status_code == 200:
        json_response = jsons.load(response.json())
        #проверка на существоание группы
        user = deserialize(redisapi.get_value(message.chat.id))
        user.auth = True
        user.group = json_response["id"]
        redisapi.set_value(message.chat.id, serialize(user))
        await message.answer(
            "Мы запомнили", reply_markup=get_start_kb()
        )
    else:
        await message.answer(
            "Такой группы нет"
        )







# Клвиатура
def get_start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Сегодня")
    kb.button(text="Завтра")
    kb.button(text="После завтра")
    return kb.as_markup(resize_keyboard=True)
