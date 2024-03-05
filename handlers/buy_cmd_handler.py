from typing import Dict, Any

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.keyboard import InCallBack, buy_inline, pay_method_inline, main_inline, order_info_inline
from utils.get_responses import get_responses
from utils.statesorder import OrderForm

buy_router = Router()


@buy_router.callback_query(InCallBack.filter(F.action == 'buy'))
async def buy_action(call: CallbackQuery, state: FSMContext):
    await state.set_state(OrderForm.order)
    await call.message.answer_photo(
        get_responses('photo_teg'),
        caption=get_responses('buy_step1'),
        reply_markup=buy_inline()
    )


@buy_router.callback_query(InCallBack.filter(F.action.casefold().in_(
    ['sum30', 'sum80', 'sum170', 'sum360', 'sum950', 'sum2000', 'pass', 'pass_up', 'pass_plus']
        )
    )
)
async def buy_step1(call: CallbackQuery, state: FSMContext):
    action = call.data[3:]
    if action == 'sum30':
        await state.update_data(order='30 гемов')
        await call.message.answer_photo(
            get_responses('photo_teg_30'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'sum80':
        await state.update_data(order='80 гемов')
        await call.message.answer_photo(
            get_responses('photo_teg_80'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'sum170':
        await state.update_data(order='170 гемов')
        await call.message.answer_photo(
            get_responses('photo_teg_170'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'sum360':
        await state.update_data(order='360 гемов')
        await call.message.answer_photo(
            get_responses('photo_teg_360'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'sum950':
        await state.update_data(order='950 гемов')
        await call.message.answer_photo(
            get_responses('photo_teg_950'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'sum2000':
        await state.update_data(order='2000 гемов')
        await call.message.answer_photo(
            get_responses('photo_teg_2000'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'pass':
        await state.update_data(order='Бравл пасс')
        await call.message.answer_photo(
            get_responses('photo_teg_pass'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'pass_up':
        await state.update_data(order='Улучшение БП')
        await call.message.answer(
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'pass_plus':
        await state.update_data(order='Бравл пасс+')
        await call.message.answer_photo(
            get_responses('photo_teg_pass_plus'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    await state.set_state(OrderForm.pay_method)


@buy_router.callback_query(OrderForm.order)
async def incorrect_order(call: CallbackQuery, order_state: FSMContext):
    await call.message.answer(get_responses('inc_order'), reply_markup=buy_inline())


@buy_router.callback_query(OrderForm.pay_method, InCallBack.filter(F.action.casefold().in_(
    ['sbp', 'qiwi', 'card']
        )
    )
)
async def buy_step2(call: CallbackQuery, state: FSMContext):
    action = call.data[3:]
    if action == 'sbp':
        await state.update_data(pay_method='СБП')
    elif action == 'qiwi':
        await state.update_data(pay_method='Qiwi')
    elif action == 'card':
        await state.update_data(pay_method='Карта')
    data = await state.get_data()
    await state.clear()
    await show_summary(call=call, data=data)


@buy_router.callback_query(OrderForm.pay_method)
async def incorrect_pay(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        get_responses('inc_order'),
        reply_markup=pay_method_inline()
    )


@buy_router.callback_query(InCallBack.filter(F.action.casefold() == 'ok_order'))
async def ok_order(call: CallbackQuery):
    await call.message.answer(
        get_responses('ok_order'),
        reply_markup=main_inline()
    )
    await call.message.forward(chat_id='-1002110191577')


@buy_router.callback_query(InCallBack.filter(F.action == 'negative_order'))
async def incor_order(call: CallbackQuery):
    await call.message.answer(
        get_responses('incorrect_order'),
        reply_markup=main_inline()
    )


@buy_router.message()
async def unknown_cmd(message: Message):
    await message.reply(get_responses('unknown_cmd'))


async def show_summary(call: CallbackQuery, data: Dict[str, Any]):
    order = data.get('order')
    pay_method = data.get('pay_method')
    summ = str(order)
    pay = str(pay_method)
    msg = f"Пользователь: @{call.from_user.username}\nСумма заказа: {summ}\nМетод оплаты: {pay}\nВсё верно?"
    await call.message.answer(
        msg,
        reply_markup=order_info_inline()
    )
