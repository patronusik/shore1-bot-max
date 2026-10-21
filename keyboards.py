from maxbot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_URL, SITE_URL, FORM_URL

# --- ПРОВЕРКА ПОДПИСКИ ---
subscribe_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📢 Открыть канал", url=CHANNEL_URL)],
    [InlineKeyboardButton(text="✅ Я подписан", callback_data="check_sub")]
])

# --- ГЛАВНОЕ МЕНЮ ---
main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🤸‍♀️ Об учреждении", callback_data="about")],
    [InlineKeyboardButton(text="📍 Адреса учреждения", callback_data="addresses")],
    [InlineKeyboardButton(text="💳 Платные услуги", url="https://olimpreserv1-30.ru/paid-service/")],
    [InlineKeyboardButton(text="❓ Часто задаваемые вопросы", callback_data="support_menu")],
    [InlineKeyboardButton(text="📞 Контактная информация", callback_data="contacts")],
    [InlineKeyboardButton(text="💬 Остались вопросы? Напишите нам", url="https://pos.gosuslugi.ru/landing/")],
])

# --- ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ ---
support_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="❓ Возраст приема", callback_data="question_1")],
    [InlineKeyboardButton(text="❓ Программы", callback_data="question_2")],
    [InlineKeyboardButton(text="❓ Вид спорта", callback_data="question_3")],
    [InlineKeyboardButton(text="❓ Направления", callback_data="question_4")],
])

# --- КНОПКА "НАЗАД" ДЛЯ ПОДМЕНЮ ---
back_to_support_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к часто задаваемым вопросам", callback_data="support_menu")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

back_to_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])
