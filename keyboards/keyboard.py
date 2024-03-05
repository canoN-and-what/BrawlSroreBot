from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton, CallbackData


def main_inline():
    builder = InlineKeyboardBuilder()
    buy_button = InlineKeyboardButton(text="Покупка", callback_data=InCallBack(action='buy').pack())
    tech_button = InlineKeyboardButton(text="Тех. Поддержка", callback_data=InCallBack(action='tech').pack())
    faq_button = InlineKeyboardButton(text="FAQ", url="https://telegra.ph/FAQ-info-02-16-2")

    builder.add(buy_button)
    builder.row(
        tech_button, faq_button,
    )

    markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
    return markup


def buy_inline():
    builder = InlineKeyboardBuilder()
    button_30 = InlineKeyboardButton(text="30 гемов", callback_data=InCallBack(action='sum30').pack())
    button_80 = InlineKeyboardButton(text="80 гемов", callback_data=InCallBack(action='sum80').pack())
    button_170 = InlineKeyboardButton(text="170 гемов", callback_data=InCallBack(action='sum170').pack())
    button_360 = InlineKeyboardButton(text="360 гемов", callback_data=InCallBack(action='sum360').pack())
    button_950 = InlineKeyboardButton(text="950 гемов", callback_data=InCallBack(action='sum950').pack())
    button_2000 = InlineKeyboardButton(text="2000 гемов", callback_data=InCallBack(action='sum2000').pack())
    pass_button = InlineKeyboardButton(text="Бравл пасс", callback_data=InCallBack(action='pass').pack())
    pass_up_button = InlineKeyboardButton(text="Улучшение БП", callback_data=InCallBack(action='pass_up').pack())
    pass_plus_button = InlineKeyboardButton(text="Бравл пасс+", callback_data=InCallBack(action='pass_plus').pack())

    builder.row(
        button_30, button_80, button_170,
        button_360, button_950, button_2000,
        pass_button, pass_up_button, pass_plus_button,
        width=3
    )

    markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
    return markup


def order_info_inline():
    builder = InlineKeyboardBuilder()
    ok_order_button = InlineKeyboardButton(
        text="Верно",
        callback_data=InCallBack(action='ok_order').pack()
    )
    negative_order_button = InlineKeyboardButton(
        text="Не так",
        callback_data=InCallBack(action='negative_order').pack()
    )
    builder.row(
        ok_order_button, negative_order_button,
        width=2
    )
    markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
    return markup


def tech_support_contacts_inline():
    builder = InlineKeyboardBuilder()
    admin_button = InlineKeyboardButton(
        text='Админстратор',
        url='tg://resolve?domain=BrawlGemSeller'
    )
    tech_admin_button = InlineKeyboardButton(
        text='Тех. Администратор',
        url='tg://resolve?domain=slas_GOD'
    )
    main_menu_button = InlineKeyboardButton(
        text='Назад',
        callback_data=InCallBack(action='back_main_menu').pack()
    )
    builder.add(admin_button, tech_admin_button, main_menu_button)
    builder.adjust(2)
    markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
    return markup


def pay_method_inline():
    builder = InlineKeyboardBuilder()
    sbp_button = InlineKeyboardButton(
        text='СБП',
        callback_data=InCallBack(action='sbp').pack()
    )
    qiwi_button = InlineKeyboardButton(
        text='Qiwi',
        callback_data=InCallBack(action='qiwi').pack()
    )
    card_button = InlineKeyboardButton(
        text='Карта',
        callback_data=InCallBack(action='card').pack()
    )
    builder.row(
        sbp_button, qiwi_button, card_button,
        width=3
    )
    markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
    return markup


class InCallBack(CallbackData, prefix='in'):
    action: str
