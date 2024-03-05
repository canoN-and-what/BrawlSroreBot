from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.keyboard import InCallBack
from keyboards.keyboard import tech_support_contacts_inline, main_inline
from utils.get_responses import get_responses

tech_router = Router()


@tech_router.callback_query(InCallBack.filter(F.action == 'tech'))
async def tech_support(call: CallbackQuery):
    await call.message.answer(
        get_responses('tech_support'),
        reply_markup=tech_support_contacts_inline()
    )


@tech_router.callback_query(InCallBack.filter(F.action == 'back_main_menu'))
async def back_main_menu(call: CallbackQuery):
    await call.message.answer(
        get_responses('start'),
        reply_markup=main_inline()
    )
