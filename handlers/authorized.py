from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums import ParseMode
import dbapi
import jsons
from entity.User import User

import redisapi
from filter.auth_filter import deserialize


router = Router()


@router.message(F.text.lower() == 'сегодня')
async def listening_item(message: Message):
    user: User = deserialize(redisapi.get_value(message.chat.id))
    response = dbapi.get_today_day(user)
    json_response = jsons.load(response.json())
    if response.text == "" or response.text == "[]":
        await message.answer(
            "Занятий нет"
        )
    else:
        if len(json_response) == 1:
            await message.answer(
                "<b style='text-align:center'>Дата: " + str(json_response[0]['date']) + "</b>\n" +
                "Дисциплина: " + str(json_response[0]['discipline']) + "\n" +
                "Преподаватель: " + str(json_response[0]['teacher']) + "\n" +
                "Аудитория: " + str(json_response[0]['classroom']),
                parse_mode=ParseMode.HTML
            )
        else:
            await message.answer(
                "<b>Дата: " + str(json_response[0]['date']) + "</b>\n\n" +
                "<b>Подгруппа I</b>\n" +
                "Дисциплина: " + str(json_response[0]['discipline']) + "\n" +
                "Преподаватель: " + str(json_response[0]['teacher']) + "\n" +
                "Аудитория: " + str(json_response[0]['classroom']) + "\n\n" +
                "<b>Подгруппа II</b>\n" +
                "Дисциплина: " + str(json_response[1]['discipline']) + "\n" +
                "Преподаватель: " + str(json_response[1]['teacher']) + "\n" +
                "Аудитория: " + str(json_response[1]['classroom']),
                parse_mode=ParseMode.HTML
            )

@router.message(F.text.lower() == 'завтра')
async def listening_item(message: Message):
    user: User = deserialize(redisapi.get_value(message.chat.id))
    response = dbapi.get_tomorrow_day(user)
    json_response = jsons.load(response.json())
    if response.text == "" or response.text == "[]":
        await message.answer(
            "Занятий нет"
        )
    else:
        if len(json_response) == 1:
            await message.answer(
                "<b style='text-align:center'>Дата: " + str(json_response[0]['date']) + "</b>\n" +
                "Дисциплина: " + str(json_response[0]['discipline']) + "\n" +
                "Преподаватель: " + str(json_response[0]['teacher']) + "\n" +
                "Аудитория: " + str(json_response[0]['classroom']),
                parse_mode=ParseMode.HTML
            )
        else:
            await message.answer(
                "<b>Дата: " + str(json_response[0]['date']) + "</b>\n\n" +
                "<b>Подгруппа I</b>\n" +
                "Дисциплина: " + str(json_response[0]['discipline']) + "\n" +
                "Преподаватель: " + str(json_response[0]['teacher']) + "\n" +
                "Аудитория: " + str(json_response[0]['classroom']) + "\n\n" +
                "<b>Подгруппа II</b>\n" +
                "Дисциплина: " + str(json_response[1]['discipline']) + "\n" +
                "Преподаватель: " + str(json_response[1]['teacher']) + "\n" +
                "Аудитория: " + str(json_response[1]['classroom']),
                parse_mode=ParseMode.HTML
            )

@router.message(F.text.lower() == 'после завтра')
async def listening_item(message: Message):
    user: User = deserialize(redisapi.get_value(message.chat.id))
    response = dbapi.get_after_tomorrow_day(user)
    json_response = jsons.load(response.json())
    if response.text == "" or response.text == "[]":
        await message.answer(
            "Занятий нет"
        )
    else:
        if len(json_response) == 1:
            await message.answer(
                "<b style='text-align:center'>Дата: " + str(json_response[0]['date']) + "</b>\n" +
                "Дисциплина: " + str(json_response[0]['discipline']) + "\n" +
                "Преподаватель: " + str(json_response[0]['teacher']) + "\n" +
                "Аудитория: " + str(json_response[0]['classroom']),
                parse_mode=ParseMode.HTML
            )
        else:
            await message.answer(
                "<b>Дата: " + str(json_response[0]['date']) + "</b>\n\n" +
                "<b>Подгруппа I</b>\n" +
                "Дисциплина: " + str(json_response[0]['discipline']) + "\n" +
                "Преподаватель: " + str(json_response[0]['teacher']) + "\n" +
                "Аудитория: " + str(json_response[0]['classroom']) + "\n\n" +
                "<b>Подгруппа II</b>\n" +
                "Дисциплина: " + str(json_response[1]['discipline']) + "\n" +
                "Преподаватель: " + str(json_response[1]['teacher']) + "\n" +
                "Аудитория: " + str(json_response[1]['classroom']),
                parse_mode=ParseMode.HTML
            )

