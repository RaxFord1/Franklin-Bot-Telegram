# -*- coding: utf-8 -*- p
#import
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

CHAT_ID = "-227725329"

#creating bot
TOKEN = "1061044668:AAG9GvEyVTgXcrKsl927zzrr1Zmzg6WMca8"

bot = TeleBot(TOKEN)



#bot functions
#message functions
def StartMessage(message):
    text_to_message = """Привет👋
Этот бот значительно упростит тебе жизнь - он был разработан для помощи в поиске и выборе подходящих инструментов для пассивного инвестирования
Пройдя небольшой опрос ты получишься от бота сформулированый список инструментов и компаний, которые подходят именно тебе
Предварительно, мы отобрали только надёжные компании, именно их мы можем смело рекомендовать"""
    keyboard = ReplyKeyboardMarkup(True)
    button1 = KeyboardButton('Пройти опрос')
    keyboard.add(button1)
    bot.send_message(message.chat.id, text_to_message, reply_markup=keyboard, parse_mode="html")
questions = [['До 25 👶','25-30 👦','30-45 👨','Больше 45 🧔'],
['Меньше 1000$ 💵','1000-3000$ 💸','3000-5000$ 💰','Больше 5000$ 🧾'],
['меньше 10% 🌑','10-25% 🌒','25-50% 🌓','больше 50% 🌔'],
['Да 🐣', 'Нет 🍾'],
['Баланс доходности и риска ⚖️','Большая покупка 🚗','Сохранение капитала🗄','Безбедная старость 🛀🏻 '],
['Да 🎢', 'Нет 🎠'],
['менее 1 года 🕯','1-3 года ⏱','3-5 лет ⏰','более 5 лет ⏳']]

#message functions
def StartQuiz(message):
    text_to_message = "Сколько Вам лет?"
    markup = ReplyKeyboardMarkup(True)
    button1 = KeyboardButton(questions[0][0])
    button2 = KeyboardButton(questions[0][1])
    button3 = KeyboardButton(questions[0][2])
    button4 = KeyboardButton(questions[0][3])
    back = KeyboardButton('Назад🔙')
    markup.row(button1,button2)
    markup.row(button3, button4)

    bot.send_message(message.chat.id, text_to_message,  reply_markup=markup, parse_mode="html")

def secondQuestion(message):
    text_to_message = "Какую сумму Вы готовы проинвестировать?"
    markup = ReplyKeyboardMarkup(True)
    button1 = KeyboardButton(questions[1][0])
    button2 = KeyboardButton(questions[1][1])
    button3 = KeyboardButton(questions[1][2])
    button4 = KeyboardButton(questions[1][3])
    back = KeyboardButton('Назад🔙')
    markup.row(button1,button2)
    markup.row(button3, button4)
    markup.row(back)

    bot.send_message(message.chat.id, text_to_message,  reply_markup=markup, parse_mode="html")


#3 вопрос
def thirdQuestion(message):
    text_to_message = "Какую часть от своего дохода Вы откладываете?"
    markup = ReplyKeyboardMarkup(True)
    button1 = KeyboardButton(questions[2][0])
    button2 = KeyboardButton(questions[2][1])
    button3 = KeyboardButton(questions[2][2])
    button4 = KeyboardButton(questions[2][3])
    back = KeyboardButton('Назад🔙')
    markup.row(button1,button2)
    markup.row(button3, button4)
    markup.row(back)

    bot.send_message(message.chat.id, text_to_message,  reply_markup=markup, parse_mode="html")


#4 вопрос
def fourthQuestion(message):
    text_to_message = "Есть ли у вас Дети?"
    markup = ReplyKeyboardMarkup(True)
    button1 = KeyboardButton(questions[3][0])
    button2 = KeyboardButton(questions[3][1])
    back = KeyboardButton('Назад🔙')
    markup.row(button1,button2)
    markup.row(back)

    bot.send_message(message.chat.id, text_to_message,  reply_markup=markup, parse_mode="html")


#5 вопрос
def fifthQuestion(message):
    text_to_message = "Какая основная цель Ваших инвестиций?"
    markup = ReplyKeyboardMarkup(True)
    button1 = KeyboardButton(questions[4][0])
    button2 = KeyboardButton(questions[4][1])
    button3 = KeyboardButton(questions[4][2])
    button4 = KeyboardButton(questions[4][3])
    back = KeyboardButton('Назад🔙')
    markup.row(button1,button2)
    markup.row(button3, button4)
    markup.row(back)

    bot.send_message(message.chat.id, text_to_message,  reply_markup=markup, parse_mode="html")


#6 вопрос
def sixthQuestion(message):
    text_to_message = "Готовы ли Вы инвестировать в рисковые инструменты?"
    markup = ReplyKeyboardMarkup(True)
    button1 = KeyboardButton(questions[5][0])
    button2 = KeyboardButton(questions[5][1])
    back = KeyboardButton('Назад🔙')
    markup.row(button1,button2)
    markup.row(back)

    bot.send_message(message.chat.id, text_to_message,  reply_markup=markup, parse_mode="html")

#message functions
#7 вопрос
def seventhQuestion(message):
    text_to_message = "На какое количество времени Вы готовы инвестировать?"
    markup = ReplyKeyboardMarkup(True)
    button1 = KeyboardButton(questions[6][0])
    button2 = KeyboardButton(questions[6][1])
    button3 = KeyboardButton(questions[6][2])
    button4 = KeyboardButton(questions[6][3])
    back = KeyboardButton('Назад🔙')
    markup.row(button1,button2)
    markup.row(button3, button4)
    markup.row(back)
    bot.send_message(message.chat.id, text_to_message,  reply_markup=markup, parse_mode="html")


def ICU_UAH(answers):
    if (answers[1] == questions[1][0] or answers[1] == questions[1][1] ):
        return False

    return True


def ICU_USD(answers):
    if ( answers[1] == questions[1][0] or answers[1] == questions[1][1] ):
        return False

    return True

def FID_USD(answers):
    if (answers[1] == questions[1][0] ):
        return False

    return True

def FID_UAH(answers):

    if ( answers[1] == questions[1][1] or answers[1] == questions[1][2] or answers[1] == questions[1][3]):
        return False
    return True


def UNIVER_USD(answers):
    if (answers[1] == questions[1][0] or answers[1] == questions[1][1] or answers[1] == questions[1][2]):
        return False

    return True

def UNIVER_UAH(answers):
    if (answers[1] == questions[1][0] or answers[1] == questions[1][1] or answers[1] == questions[1][3]):
        return False

    if ( False):
        return False
    return True

def DRAGON_CAPITAL_USD(answers):
    if (answers[1] == questions[1][0] or answers[1] == questions[1][1] or answers[1] == questions[1][2]):
        return False
    if (False or False):
        return False
    if ( False):
        return False
    return True

def DRAGON_UAH(answers):
    if (answers[1] == questions[1][0] or answers[1] == questions[1][1]):
        return False
    if ( False):
        return False
    if (False or False):
        return False
    return True

def HUGS(answers):
    if (answers[1] == questions[1][0] or answers[1] == questions[1][1]):
        return False
    if (answers[6] == questions[6][0]):
        return False
    if (False or False):
        return False
    if ( False):
        return False
    return True

def UNIVER(answers):
    if (answers[1] == questions[1][0]):
        return False
    if (answers[6] == questions[6][0]):
        return False
    if ( False):
        return False
    if (False or False):
        return False
    return True

def ICU_PIF(answers):
    if (answers[1] == questions[1][0] or answers[1] == questions[1][1]):
        return False
    if (answers[6] == questions[6][0] or answers[6] == questions[6][2] or answers[6] == questions[6][3]):
        return False
    if ( False):
        return False
    if (False or False ):
        return False
    return True

def OTP_CAPITAL_PIF(answers):
    if ( False):
        return False
    if (False or False):
        return False
    return True

def ICU_NPF(answers):
    if (answers[0] == questions[0][3]):
        return False
    if (answers[6] == questions[6][0] or answers[6] == questions[6][1] or answers[6] == questions[6][2]):
        return False
    if ( False):
        return False
    if (False or False):
        return False
    return True

def LIGA_PENSIJA_NPF(answers):
    if (answers[0] == questions[0][3]):
        return False
    if (answers[6] == questions[6][0] or answers[6] == questions[6][1] or answers[6] == questions[6][2]):
        return False
    if ( False):
        return False
    if (False or False):
        return False
    return True

def OTP_NPF(answers):
    if (answers[0] == questions[0][3]):
        return False
    if (answers[6] == questions[6][0] or answers[6] == questions[6][1] or answers[6] == questions[6][2]):
        return False
    if ( False):
        return False
    if (False or False):
        return False
    return True

def KINTO_NPF(answers):
    if (answers[0] == questions[0][3]):
        return False
    if (answers[6] == questions[6][0] or answers[6] == questions[6][1] or answers[6] == questions[6][2]):
        return False
    if ( False):
        return False
    if (False or False):
        return False
    return True

def MONOBANK(answers):

    return True

def ALPHABANK(answers):
    if ( False):
        return False
    if (False or False):
        return False
    return True

def AVAL(answers):
    if (False):
        return False
    if (False or  False):
        return False
    return True

def OTP_BANK(answers):
    if (False or  False):
        return False
    if ( False):
        return False
    return True

def FINHUB(answers):
    if (False or False or False):
        return False
    if ( answers[5] == questions[5][1]):
        return False
    return True

def FREEDOMFINANCE(answers):
    if (answers[1] == questions[1][0]):
        return False

    if ( answers[5] == questions[5][1]):
        return False
    if (False or False or False):
        return False
    return True

def UNITEDTRADERS(answers):
    if (answers[1] == questions[1][0]):
        return False
    if (answers[6] == questions[6][3] or answers[6] == questions[6][1] or answers[6] == questions[6][2]):
        return False
    if ( answers[5] == questions[5][1]):
        return False
    if (False or False or False):
        return False
    return True


def Monobank_text():
    currency = """
🔸<b>Валюта</b>: (UAH)
"""
    historical = """🔸<b>Доходность</b>: от 14 до 17,5 % (зависит от срока депозита и досрочного снятия)
"""
    min_threshold = """🔸<b>Порог входа</b>: 1 000 UAH
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: 1 месяц
"""
    liquidity = """🔸<b>Ликвидность</b>: погашение в любое время, но при досрочном погашении, теряется львиная доля заработаных процентов
"""
    name = "Monobank"
    what_the_guy = """
💡<b>Monobank</b> - <i>украинский мобильный банк без отделений.
Запустились в 2017 году и имеют 1,5 миллиона клиентов.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: Подоходный налог 18
Военный сбор 1,5%
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Получить дебетную карту
2. Выбрать подходящую сумму и срок для депозита

"""
    website = "https://www.monobank.ua"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def Alphabank_text():
    currency = """
🔸<b>Валюта</b>: (UAH)
"""
    historical = """🔸<b>Доходность</b>: от 11 до 16,75 % (зависит от срока депозита и досрочного снятия)
"""
    min_threshold = """🔸<b>Порог входа</b>: 5 000 UAH
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: 1 месяц
"""
    liquidity = """🔸<b>Ликвидность</b>: погашение в любое время, но при досрочном погашении, теряется львиная доля заработаных процентов
"""
    name = "Альфа Банк"

    what_the_guy = """
💡<b>Альфа-Банк</b> — <i>крупнейший частный банк. Входит в 20-ку надежных банков в Украине по данным Dragon Capital & Новое время.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: Подоходный налог 18
Военный сбор 1,5%
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Выбрать подходящую сумму и срок для депозита
2. Оформить депозит через дебетную карту, либо же в отеделнии банка

"""
    website = "https://alfabank.ua/ru"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def Aval_text():
    currency = """
🔸<b>Валюта</b>: (UAH)
"""
    historical = """🔸<b>Доходность</b>: от 8,5 до 14 % (зависит от срока депозита и досрочного снятия)
"""
    min_threshold = """🔸<b>Порог входа</b>: 1 00 UAH
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: 1 месяц
"""
    liquidity = """🔸<b>Ликвидность</b>: погашение в любое время, но при досрочном погашении, теряется львиная доля заработаных процентов
"""

    name = "Райфайзен Банк Аваль"
    what_the_guy = """
💡<b>Райфайзен Банк Аваль</b> — <i>один из самых крупных украинских банков. №1 в рейтинге самых надежных банков по данным Dragon Capital & Новое время</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: Подоходный налог 18
Военный сбор 1,5%"
"""
    mechanics = """
⚙️<b>механика начала инвестиций</b>:
1. Выбрать подходящую сумму и срок для депозита
2. Оформить договор в отделении банка
"""
    website = "https://www.aval.ua/ru"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def OTP_text():
    currency = """
🔸<b>Валюта</b>: (UAH)
"""
    historical = """🔸<b>Доходность</b>: от 9,5 до 13 % (зависит от срока депозита и досрочного снятия)
"""
    min_threshold = """🔸Порог входа: 2 000 UAH
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: 1 месяц
"""
    liquidity = """🔸<b>Ликвидность</b>: погашение в любое время, но при досрочном погашении, теряется львиная доля заработаных процентов
"""

    name = "ОТП Банк"
    what_the_guy = """
💡<b>ОТП Банк</b>— <i>крупнейший венгерский банк. Входит в 10-ку надежных банков в Украине по данным Dragon Capital & Новое время.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: Подоходный налог 18
Военный сбор 1,5%"
"""
    mechanics = """
⚙️<b>механика начала инвестиций</b>:
1. Выбрать подходящую сумму и срок для депозита
2. Оформить депозит через дебетную карту, либо же в отеделнии банка

"""
    website = "https://ru.otpbank.com.ua"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def ICU_USD_text():
    currency = """
🔸<b>Валюта</b>: (UAH / USD)
"""
    historical = """🔸<b>Историческая доходность</b>: 15,65% / от 2 до 5 %
"""
    min_threshold = """🔸<b>Порог входа</b>: 100 000 UAH / 5 000 USD
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: отсутсвует
"""
    liquidity = """🔸<b>Ликвидность</b>: возможна продажа в течении 5 дней
"""

    name = "ICU"
    what_the_guy = """
💡  <b>ICU</b> - <i>Финансовая компания с услугами торговли ценными бумагами и управлением активами. На рынке Украины уже 13 лет.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: комиссия за покупку/продажу  – 200 UAH за сделку, независимо от объёма // комиссия за возврат купонного дохода и/или всей суммы погашения ОВГЗ в валюте – 25 $;
"""
    mechanics = """
⚙️<b>механика начала инвестиций</b>:
1. Открыть свой личный брокерский счет (нужен паспорт & ИНН) ;
2. Открыть вместе с Freedom счет в ценных бумагах;
3. Оформить покупку по договору ""купля-продажа"".

"""
    website = "https://www.icu.ua/uk"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def ICU_UAH_text():
    currency = """
🔸<b>Валюта</b>: UAH
"""
    historical = """🔸<b>Историческая доходность</b>: до 15%
"""
    min_threshold = """🔸<b>Порог входа</b>: 100 000 грн
"""
    min_term = """🔸<b>Минимальный срок инвестировании</b>: рекомендуемый срок 3 года
"""
    liquidity = """🔸<b>Ликвидность</b>: возможна продажа в течении 5 дней
"""

    name = "ICU"
    what_the_guy = """
💡<b>ICU</b> - <i>Финансовая компания с услугами торговли ценными бумагами и управлением активами. На рынке Украины уже 13 лет.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>:
Подоходный налог 18%
Военный сбор 1,5%
- на всю сумму при единоразовой выплате;
- на 60% выплату при регулярных выплатах;
- Лица старше 70 лет, инвалиды 1 группы и наследники первой степени родства освобождаются от уплаты налогов.
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Прислать в электронном виде скан-копии паспорта (все заполненные страницы) и идентификационного кода.
2. На основе документов, вам приготовят пенсионный контракт и отправят на подпись.

<b>Альтернативный вариант</b>: открыть счет через личный кабинет в Приват24
"""
    website = "https://www.icu.ua/uk"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def FID_USD_text():
    currency = """
🔸<b>Валюта</b>: (UAH / USD)
"""
    historical = """🔸<b>Историческая доходность</b>: 13% /  5% (доходность только после 3 месяцев)
"""
    min_threshold = """🔸<b>Порог входа</b>: 1 100 UAH / 1 100 USD
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: 3 месяца
"""
    liquidity = """🔸<b>Ликвидность</b>: есть возможность мгновенной продажи.
"""

    name = "Freedom Finance "
    what_the_guy = """
💡 <b>Freedom Finance</b> - <i>предоставляет услуги по управлению ценными бумагами. Основное направление деятельности — американский фондовый рынок. В Украине с 1999 года.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: отсутствует
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Открыть свой личный брокерский счет (нужен паспорт & ИНН) ;
2. Открыть вместе с Freedom счет в ценных бумагах;
3. Оформить покупку по договору ""купля-продажа"".

"""
    website = "https://www.ffin.ua/"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def FID_UAH_text():
    currency = """
🔸<b>Валюта</b>: (UAH)
"""
    historical = """🔸<b>Историческая доходность</b>: 13% (доходность только после 3 месяцев)
"""
    min_threshold = """🔸<b>Порог входа</b>: 1 100 UAH
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: 3 месяца
"""
    liquidity = """🔸<b>Ликвидность</b>: есть возможность мгновенной продажи.
"""

    name = "Freedom Finance "
    what_the_guy = """
💡 <b>Freedom Finance</b> - <i>предоставляет услуги по управлению ценными бумагами. Основное направление деятельности — американский фондовый рынок. В Украине с 1999 года.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: отсутствует
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Открыть свой личный брокерский счет (нужен паспорт & ИНН) ;
2. Открыть вместе с Freedom счет в ценных бумагах;
3. Оформить покупку по договору ""купля-продажа"".

"""
    website = "https://www.ffin.ua/"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def UNIVER_USD_text():
    currency = """
🔸<b>Валюта</b>: (UAH / USD)
"""
    historical = """🔸<b>Историческая доходность</b>:15% / 3,5%
"""
    min_threshold = """🔸<b>Порог входа</b>: 50 000 UAH / 10 000 USD
"""
    min_term = """🔸<b>Минимальный срок инвестировании</b>: рекомендуемый срок 3 года
"""
    liquidity = """🔸<b>Ликвидность</b>: возможна продажа в течении 5 дней
"""

    name = "Univer "
    what_the_guy = """
💡<b>Univer</b> - <i>инвестиционная группа. Работает с гос. облигациями, инвестиционными фондами, инвестициями в Украине и за границу, а также IPO. Работают с 2013 года.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: За операцию - 0,05% от суммы, но не менее 200 грн.,
Комиссия НБУ за выплату купона и погашение бумаг - 200 грн.
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Прислать в электронном виде скан-копии паспорта & ИНН, справку о счете в банке и их опросник;
2. Подписать договор на брокерское обслуживание;
3. Подписать договор на открытие счета в ценных бумагах.

"""
    website = "https://www.univer.ua/fund"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def UNIVER_UAH_text():
    currency = """
🔸<b>Валюта</b>: (UAH)
"""
    historical = """🔸<b>Историческая доходность</b>: 15%
"""
    min_threshold = """🔸<b>Порог входа</b>: 50 000 UAH
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: отсутсвует
"""
    liquidity = """🔸<b>Ликвидность</b>: возможна продажа в течении 5 дней
"""

    name = "Univer "
    what_the_guy = """
💡<b>Univer</b> - <i>инвестиционная группа. Работает с гос. облигациями, инвестиционными фондами, инвестициями в Украине и за границу, а также IPO. Работают с 2013 года.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: За операцию - 0,05% от суммы, но не менее 200 грн.,
Комиссия НБУ за выплату купона и погашение бумаг - 200 грн.
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Прислать в электронном виде скан-копии паспорта & ИНН, справку о счете в банке и их опросник;
2. Подписать договор на брокерское обслуживание;
3. Подписать договор на открытие счета в ценных бумагах.

"""
    website = "https://www.univer.ua/fund"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def DRAGON_CAPITAL_USD_text():
    currency = """
🔸<b>Валюта</b>: (UAH / USD)
"""
    historical = """🔸<b>Историческая доходность</b>: от 14,5 до 15 % /  от 3 до 4 %
"""
    min_threshold = """🔸<b>Порог входа</b>:100 000 UAH /  8 000 USD
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: отсутсвует
"""
    liquidity = """🔸<b>Ликвидность</b>: возможна продажа в течении 5 дней
"""

    name = "Dragon Capital "
    what_the_guy = """
💡<b>Dragon Capital</b> – <i>инвестиционная компания, осуществляет брокерские операции с акциями и долговыми инструментами, прямые инвестиции и управление активами. Основана в 2000 году в Киеве.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>:
— Осуществление депозитарного учета ценных бумаг (от номинальной стоимости ЦБ) — 0,003%, но не меньше 50,00 грн.
— Выплата Накопленного Купонного Дохода и всей суммы при погашении — 0,5% от суммы, но не менее 200,00 и не больше 2500,00 грн.
— Блокировка/разблокировка грн. на биржу – 10,00 грн.
— Блокировка/разблокировка ЦБ на биржу – 3,00 грн.
— Вывод грн. на банковский счет – 10,00 грн.
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Прислать в электронном виде скан-копии паспорта & ИНН, справку о счете в банке и документ подтверждающие средства;
2. Подписать договор на брокерское обслуживание;
3. Подписать договор на открытие счета в ценных бумагах.
"""
    website = "https://dragon-capital.com/ru/"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def DRAGON_UAH_text():
    currency = """
🔸<b>Валюта</b>: (UAH)
"""
    historical = """🔸<b>Историческая доходность</b>: от 14,5 до 15 %
"""
    min_threshold = """🔸<b>Порог входа</b>: 100 000 UAH
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: отсутсвует
"""
    liquidity = """🔸<b>Ликвидность</b>: возможна продажа в течении 5 дней
"""

    name = "Dragon Capital  "
    what_the_guy = """
💡<b>Dragon Capital</b> – <i>инвестиционная компания, осуществляет брокерские операции с акциями и долговыми инструментами, прямые инвестиции и управление активами. Основана в 2000 году в Киеве.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>:
— Осуществление депозитарного учета ценных бумаг (от номинальной стоимости ЦБ) — 0,003%, но не меньше 50,00 грн.
— Выплата Накопленного Купонного Дохода и всей суммы при погашении — 0,5% от суммы, но не менее 200,00 и не больше 2500,00 грн.
— Блокировка/разблокировка грн. на биржу – 10,00 грн.
— Блокировка/разблокировка ЦБ на биржу – 3,00 грн.
— Вывод грн. на банковский счет – 10,00 грн.
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Прислать в электронном виде скан-копии паспорта & ИНН, справку о счете в банке и документ подтверждающие средства;
2. Подписать договор на брокерское обслуживание;
3. Подписать договор на открытие счета в ценных бумагах.

"""
    website = "https://dragon-capital.com/ru/"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def HUGS_text():
    currency = """
🔸<b>Валюта</b>: USD
"""
    historical = """🔸<b>Историческая доходность</b>: до 12% в USD
"""
    min_threshold = """🔸<b>Порог входа</b>: 100 000 UAH
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: рекомендуют 3 года
"""
    liquidity = """🔸<b>Ликвидность</b>: возврат средств на Ваш счёт в течении 3 дней
"""

    name = "HUG'S"
    what_the_guy = """
💡<b>HUG'S</b> - <i>первый в Украине робоэдвайзер (на основе алгоритмов формирует набор компаний для инвестиций). Все средства находятся на личном счету у одного из брокеров в США. Работают с 2018 года.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: 12% от прибыли
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Связаться с менеджером
2. Подписать договор
3. Пополнить счёт

"""
    website = "https://hugs.fund"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def UNIVER_text():
    currency = """
🔸<b>Валюта</b>: UAH
"""
    historical = """🔸<b>Историческая доходность</b>: 13%
"""
    min_threshold = """🔸<b>Порог входа</b>: 10 000 грн
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: рекомендуют 3 года
"""
    liquidity = """🔸<b>Ликвидность</b>: возможна продажа в течении 5 дней
"""

    name = "Univer"
    what_the_guy = """
💡<b>Univer</b> - <i>инвестиционная группа. Работает с гос. облигациями, инвестиционными фондами, инвестициями в Украине и за границу, а также IPO. Работают с 2013 года.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: от 10 000 грн комиссия 0%
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Связаться с менеджером
2. Подписать договор
3. Пополнить счёт

"""
    website = "https://www.univer.ua/fund"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def ICU_PIF_text():
    currency = """
🔸<b>Валюта</b>: UAH
"""
    historical = """🔸<b>Историческая доходность</b>: до 15%
"""
    min_threshold = """🔸<b>Порог входа</b>: 100 000 грн
"""
    min_term = """🔸<b>Минимальный срок инвестировании</b>: рекомендуемый срок 3 года
"""
    liquidity = """🔸<b>Ликвидность</b>: возможна продажа в течении 5 дней
"""

    name = "ICU"
    what_the_guy = """
💡 <b>ICU</b> - <i>Финансовая компания с услугами торговли ценными бумагами и управлением активами. На рынке Украины уже 13 лет.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: 1% от СЧА (год)
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Открыть вместе с ICU счет в ценных бумагах;
2. Оформить покупку по договору ""купля-продажа""."

"""
    website = "https://www.icu.ua/uk"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def OTP_CAPITAL_PIF_text():
    currency = """
🔸<b>Валюта</b>: UAH
"""
    historical = """🔸<b>Историческая доходность</b>: до 15%
"""
    min_threshold = """🔸<b>Порог входа</b>: 20 000 грн
"""
    min_term = """🔸<b>Минимальный срок инвестировании</b>: рекомендуемый срок 3 года
"""
    liquidity = """🔸<b>Ликвидность</b>: продажа в течении 5 дней
"""

    name = "OTP-Capital"
    what_the_guy = """
💡<b>OTP Capital</b> <i>предоставляет широкий спектр инвестиционных услуг корпоративным клиентам и частным лицам. OTP Capital на рынке с 2007 года.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: 200 грн при покупке и от 200 до 2000 грн при продаже
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Связаться с менеджером
2. Подписать договор
3. Пополнить счёт

"""
    website = "http://ru.otpcapital.com.ua"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def ICU_NPF_text():
    currency = """
🔸<b>Валюта</b>: UAH
"""
    historical = """🔸<b>Историческая доходность</b>: до 13%
"""
    min_threshold = """🔸<b>Порог входа</b>: 425 грн
"""
    min_term = """🔸<b>Минимальный срок инвестировании</b>: 10 лет до пенсионного возвраста
"""
    liquidity = """🔸<b>Ликвидность</b>: продажа активов осуществляется на основании договора
"""

    name = "ICU"
    what_the_guy = """
💡<b>ICU</b> - <i>Финансовая компания с услугами торговли ценными бумагами и управлением активами. На рынке Украины уже 13 лет.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>:
Подоходный налог 18%
Военный сбор 1,5%
- на всю сумму при единоразовой выплате;
- на 60% выплату при регулярных выплатах;
- Лица старше 70 лет, инвалиды 1 группы и наследники первой степени родства освобождаются от уплаты налогов.
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Прислать в электронном виде скан-копии паспорта (все заполненные страницы) и идентификационного кода.
2. На основе документов, вам приготовят пенсионный контракт и отправят на подпись.
<b>Альтернативный вариант</b>: открыть счет через личный кабинет в Приват24

"""
    website = "https://www.icu.ua/uk"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def LIGA_PENSIJA_NPF_text():
    currency = """
🔸<b>Валюта</b>: UAH
"""
    historical = """🔸<b>Историческая доходность</b>: до 15%
"""
    min_threshold = """🔸<b>Порог входа</b>: 425 грн
"""
    min_term = """🔸<b>Минимальный срок инвестировании</b>: 10 лет до пенсионного возвраста
"""
    liquidity = """🔸<b>Ликвидность</b>: продажа активов осуществляется на основании договора
"""

    name = "Лига пенсия"
    what_the_guy = """
💡<b>Лига пенсия</b> - <i>один из крупнейших фондов на рынке Украины.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: Подоходный налог 18%
Военный сбор 1,5%
- на всю сумму при единоразовой выплате;
- на 60% выплату при регулярных выплатах;
- Лица старше 70 лет, инвалиды 1 группы и наследники первой степени родства освобождаются от уплаты налогов.
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Связаться с менеджером
2. Подписать договор
3. Пополнить счёт

"""
    website = "https://ligapension.com"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def OTP_NPF_text():
    currency = """
🔸<b>Валюта</b>: UAH
"""
    historical = """🔸<b>Историческая доходность</b>: до 14,25%
"""
    min_threshold = """🔸<b>Порог входа</b>: 425 грн
"""
    min_term = """🔸<b>Минимальный срок инвестировании</b>: 10 лет до пенсионного возвраста
"""
    liquidity = """🔸<b>Ликвидность</b>: продажа активов осуществляется на основании договора
"""

    name = "OTP-пенсия"
    what_the_guy = """
💡<b>ОТП Пенсия</b> - <i>лидер в Украине по темпам прироста пенсионных взносов, активов и количества клиентов. Фонд входит в ТОП-3 крупнейших по объему средств открытых пенсионных фондов в Украине.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: Подоходный налог 18%
Военный сбор 1,5%
- на всю сумму при единоразовой выплате;
- на 60% выплату при регулярных выплатах;
- Лица старше 70 лет, инвалиды 1 группы и наследники первой степени родства освобождаются от уплаты налогов.
"""
    mechanics = """
⚙️ <b>механика начала инвестиций:</b>
1. Связаться с менеджером
2. Подписать договор
3. Пополнить счёт

"""
    website = "https://otppension.com.ua"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def KINTO_NPF_text():
    currency = """
🔸<b>Валюта</b>: UAH
"""
    historical = """🔸<b>Историческая доходность</b>: до 13%
"""
    min_threshold = """🔸<b>Порог входа</b>: 425 грн
"""
    min_term = """🔸<b>Минимальный срок инвестировании</b>: 10 лет до пенсионного возвраста
"""
    liquidity = """🔸<b>Ликвидность</b>: продажа активов осуществляется на основании договора
"""

    name = "Кинто"
    what_the_guy = """
💡 <b>Kinto</b> - <i>один из старейших НПФ на территории Украины с опытом работы более 15 лет.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: Подоходный налог 18%
Военный сбор 1,5%
- на всю сумму при единоразовой выплате;
- на 60% выплату при регулярных выплатах;
- Лица старше 70 лет, инвалиды 1 группы и наследники первой степени родства освобождаются от уплаты налогов.
"""
    mechanics = """
⚙️ <b>механика начала инвестиций:</b>
1. Связаться с менеджером
2. Подписать договор
3. Пополнить счёт

"""
    website = "https://kinto.com"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def FREEDOMFINANCE_text():
    currency = """
🔸<b>Валюта</b>: USD
"""
    historical = """🔸<b>Возможная доходность</b>: ˜40%
"""
    min_threshold = """🔸<b>Порог входа</b>: 2000$
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: 3 месяца
"""
    liquidity = """🔸<b>Ликвидность</b>: Продажа через 3 месяца
"""

    name = "Freedom Finance "
    what_the_guy = """
💡 <b>Freedom Finance</b> - <i>предоставляет услуги по управлению ценными бумагами. Основное направление деятельности — американский фондовый рынок. В Украине с 1999 года.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: 5% при входе, 0,5% при выходе
"""
    mechanics = """
⚙️ <b>механика начала инвестиций</b>:
1. Связаться с менеджером
2. Подписать договор
3. Пополнить счёт

"""
    website = "https://www.ffin.ua/"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]

def UNITEDTRADERS_text():
    return []

def FINHUB_text():
    currency = """
 🔸<b>Валюта</b>: (UAH)
"""
    historical = """🔸<b>Возможная доходность</b>: ˜36% (зависит от суммы и сроков)
"""
    min_threshold = """🔸<b>Порог входа</b>: 500 UAH
"""
    min_term = """🔸<b>Минимальный срок инвестирования</b>: отсутствует
"""
    liquidity = """🔸<b>Ликвидность</b>: вывод средств в любое время
"""

    name = "FIN HUB"
    what_the_guy = """
💡<b>FIN HUB</b> — <i>это онлайн платформа p2p-кредитования, которая объединяет инвесторов и заемщиков.</i>
"""
    tarif = """
💸<b>Тарифы за обслуживание</b>: Вывод средств - 1 %
"""
    mechanics = """
⚙️ <b>механика начала инвестиций:</b>
1. Зарегистрироваться на сайте
2. Указать паспортные данные + ИНН
3. Пополнить счет
4. Выбрать заемщика, которому будет выдаваться кредит

"""
    website = "https://finhub.ua/"
    return [[ currency, historical, min_threshold, min_term, liquidity],[what_the_guy, tarif, mechanics, website], name]


def givesDeposit(message):
    messages = []
    markup = ReplyKeyboardMarkup(True)
    messages.append(Monobank_text())
    messages.append(Alphabank_text())
    messages.append(Aval_text())
    messages.append(OTP_text())
    markup.row(KeyboardButton('Подробнее о Monobank'))
    markup.row(KeyboardButton('Подробнее о АльфаБанк'))
    markup.row(KeyboardButton('Подробнее о АвальБанк'))
    markup.row(KeyboardButton('Подробнее о ОТП Банк'))
    markup.row(KeyboardButton('Вернутся к выбору инструментов'))

    for i in messages:
        result_string = i[1][0]
        for j in i[0]:
            result_string += j
        bot.send_message(message.chat.id, result_string,reply_markup = markup, parse_mode="html")


def givesOVGZ(message, user):
    answers = user[1]
    good = user[3]
    buttons = []
    messages = []
    if ICU_USD(answers) or good == 2:
        messages.append(ICU_USD_text())
        buttons.append(KeyboardButton('Подробнее о ICU UAH/USD'))

    elif ICU_UAH(answers) or good == 2:
        messages.append(ICU_UAH_text())
        buttons.append(KeyboardButton('Подробнее о ICU UAH'))

    if FID_USD(answers) or good == 2:
        messages.append(FID_USD_text())
        buttons.append(KeyboardButton('Подробнее о Freedom Finance  UAH/USD'))

    elif FID_UAH(answers) or good == 2:
        messages.append(FID_UAH_text())
        buttons.append(KeyboardButton('Подробнее о Freedom Finance UAH'))

    if UNIVER_USD(answers) or good == 2:
        messages.append(UNIVER_USD_text())
        buttons.append(KeyboardButton('Подробнее о UNIVER  UAH/USD'))

    elif UNIVER_UAH(answers) or good == 2:
        messages.append(UNIVER_UAH_text())
        buttons.append(KeyboardButton('Подробнее о UNIVER UAH'))

    if DRAGON_CAPITAL_USD(answers) or good == 2:
        messages.append(DRAGON_CAPITAL_USD_text())
        buttons.append(KeyboardButton('Подробнее о DRAGON_CAPITAL UAH/USD'))

    elif DRAGON_UAH(answers) or good == 2:
        messages.append(DRAGON_UAH_text())
        buttons.append(KeyboardButton('Подробнее о DRAGON UAH'))

    markup = ReplyKeyboardMarkup(True)
    for i in buttons:
        markup.row(i)

    markup.row(KeyboardButton('Вернутся к выбору инструментов'))

    for i in messages:
        result_string = i[1][0]
        for j in i[0]:
            result_string += j
        bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def givesPIF(message, user):
    answers = user[1]
    good = user[3]
    buttons = []
    messages = []
    if HUGS(answers) or good == 2:
        messages.append(HUGS_text())
        buttons.append(KeyboardButton('Подробнее о HUGS'))

    if UNIVER(answers) or good == 2:
        messages.append(UNIVER_text())
        buttons.append(KeyboardButton('Подробнее о UNIVER'))

    if ICU_PIF(answers) or good == 2:
        messages.append(ICU_PIF_text())
        buttons.append(KeyboardButton('Подробнее о ICU'))

    if OTP_CAPITAL_PIF(answers) or good == 2:
        messages.append(OTP_CAPITAL_PIF_text())
        buttons.append(KeyboardButton('Подробнее о OTP CAPITAL'))


    markup = ReplyKeyboardMarkup(True)
    for i in buttons:
        markup.row(i)


    markup.row(KeyboardButton('Вернутся к выбору инструментов'))
    for i in messages:
        result_string = i[1][0]
        for j in i[0]:
            result_string += j
        bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def givesNPF(message, user):
    answers = user[1]
    good = user[3]
    buttons = []
    messages = []
    if ICU_NPF(answers or good == 2):
        messages.append(ICU_NPF_text())
        buttons.append(KeyboardButton('Подробнее о ICU'))

    if LIGA_PENSIJA_NPF(answers) or good == 2:
        messages.append(LIGA_PENSIJA_NPF_text())
        buttons.append(KeyboardButton('Подробнее о Лига Пенсия'))

    if OTP_NPF(answers) or good == 2:
        messages.append(OTP_NPF_text())
        buttons.append(KeyboardButton('Подробнее о OTP'))

    if KINTO_NPF(answers) or good == 2:
        messages.append(KINTO_NPF_text())
        buttons.append(KeyboardButton('Подробнее о KINTO'))

    markup = ReplyKeyboardMarkup(True)
    for i in buttons:
        markup.row(i)

    markup.row(KeyboardButton('Вернутся к выбору инструментов'))
    for i in messages:
        result_string = i[1][0]
        for j in i[0]:
            result_string += j
        bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")




def givesIPO(message, user):
    answers = user[1]
    good = user[3]
    buttons = []
    messages = []
    if FREEDOMFINANCE(answers) or good == 2:
        messages.append(FREEDOMFINANCE_text())
        buttons.append(KeyboardButton('Подробнее о FREEDOMFINANCE'))

    markup = ReplyKeyboardMarkup(True)
    for i in buttons:
        markup.row(i)

    markup.row(KeyboardButton('Вернутся к выбору инструментов'))

    for i in messages:
        result_string = i[1][0]
        for j in i[0]:
            result_string += j
        bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")


def givesP2P(message, user):
    answers = user[1]
    good = user[3]
    result = FINHUB_text()
    markup = ReplyKeyboardMarkup(True)
    markup.row(KeyboardButton('Подробнее о FINHUB'))
    markup.row(KeyboardButton('Вернутся к выбору инструментов'))

    result_string = result[1][0]
    for j in result[0]:
        result_string += j
    bot.send_message(message.chat.id, result_string,  reply_markup=markup, parse_mode="html")


def P2P_text():
    return ["""🔗<b>P2P-кредитование</b>""",
    """<i>— это когда инвестор может дать займ другому частному лицу или бизнесу через онлайн-сервис (P2P-платформа).
Если проще, это маркетплейс, где выбираешь кому одолжить свои средства.</i>

👍 <b>Преимущества</b>:
Доходность - с правильным кредитным портфелем можно получить высокий доход в краткие сроки.
👎 <b>Риски</b>:
Неблагонадежный заемщик может перестать платить по договору.

📈<b>Доход</b> - Высокий 🥇

💸<b>Налогооблагаемость</b>:
Подоходный налог 18
Военный сбор 1,5%
(Оплачивается самостоятельно)

🛡️<b>Как уберечься от потери денег</b>:
проверяйте состояние своего кредитного портфеля, чтобы вовремя заняться возвратом просроченной задолженности.
"""]

def IPO_text():
    return ["""🎢<b>IPO</b> """,
    """<i>это первичный опыт размещения акций какой-либо компании на фондовой бирже, для привлечения новых денег в компанию.</i>
👍 <b>Преимущества</b>:
Доходность - возможность заработать большое кол-во денег за короткий период времени.
👎 <b>Риски</b>:
Невозможно предсказать результат выхода компании на фондовый рынок."

📈<b>Доход</b> - Высокий 🥇

💸<b>Налогооблагаемость</b>:
Подоходный налог 18%
Военный сбор 1,5%
(Оплачивается самостоятельно)

🛡️<b>Как уберечься от потери денег</b>: провести полноценный анализ компании, которая выходит на IPO.
"""]

def NPF_text():
    return ["""👴<b>Негосударственные пенсионные фонды (НПФ)</b> """,
    """<i>помогают копить деньги на старость. Вы делаете в них отчисления, а фонды инвестируют эти средства, чтобы они не обесценивались со временем.
Когда вы выходите на заслуженный отдых, эти сбережения начинают постепенно выплачиваться вам в виде пенсии.</i>"

👍 <b>Преимущества</b>:
Самостоятельность - вы сами определяете удобный размер и периодичность взносов / выплат
👎 <b>Риски</b>:
Строгие правила по выплатам"

📈<b>Доход</b> - Низкий 🥉

💸<b>Налогооблагаемость</b>:
Подоходный налог 18%
Военный сбор 1,5%
- на всю сумму при единоразовой выплате;
- на 60% выплату при регулярных выплатах;
- Лица старше 70 лет, инвалиды 1 группы и наследники первой степени родства освобождаются от уплаты налогов.

🛡️<b>Как уберечься от потери денег:</b> следить за состоянием НПФ.
"""]
def PIF_text():
    return ["""💰<b>ПИФ (Паевой инвестиционный фонд)</b>""",
    """<i>- управляющая компания собирает деньги у инвесторов, приобретает активы (акции, облигации и прочее) и распределяет фиксированную прибыль между участниками ПИФа.</i>

👍 <b>Преимущества</b>:
Диверсификация активов - вложения средств фонда в разные активы снижает общий риск и увеличивают доходность
👎<b>Риски</b>:
Можно получить доход меньше ожидаемого

📈<b>Доход</b> - Средний 🥈

💸<b>Налогооблагаемость</b>: Отсутствует на законодательной уровне.

🛡️<b>Как уберечься от потери денег</b>: периодически проверять, как идут дела у управляющей компании, узнавать о стратегии, планах и прогнозах.
"""]

def OVGZ_text():
    return ["""🏛️<b>ОВГЗ</b> """,
    """— <i>это долговой инструмент с фиксированной доходностью. Когда государство выпускает ОВГЗ, оно берет деньги в долг, после чего возвращает их с процентами. Сколько и когда она будет возвращать — известно заранее.Если проще, вы кредитуете правительство.</i>

👍 <b>Преимущества</b>:
Баланс - безопасные и консервативные инвестиции с предсказуемым доходом
👎 <b>Риски</b>:
Дефолт государства

📈<b>Доход</b> - Средний 🥈

💸<b>Налогооблагаемость</b>: Военный сбор 1,5%

🛡️<b>Как уберечься от потери денег</b>: Следить за политической и экономической ситуацией в государстве
"""]

def DEPOSIT_text():
    return ["""🗄<b>Депозит</b> — <i>это накопительный инструмент с фиксированной доходностью. Банк использует ваши деньги для инвестиций в другие активы и делиться с вами процентом дохода. </i>""",
    """<i>Если проще, вы кредитуете банк, а он ваши средства инвестирует.</i>

👍 <b>Преимущества</b>:
Прогнозирование - вы знаете сколько денег и через какое время вы заработаете.
Гарантии - вложения до 200 тыс. грн застрахованы фондом гарантированных вкладов.

👎 <b>Риски</b>:
Дефолт банка.
Строгие правила по досрочному погашению.

📈<b>Доход:</b> Низкий

💸<b>Налогооблагаемость</b>:
Подоходный налог 18%
Военный сбор 1,5%"

🛡️<b>Как уберечься от потери денег</b>: Следить за рейтингом банковского учреждения и его новостями.
"""]


def EndQuiz(message, answers):
    messages = []
    have = False
    buttons = []
    less = []
    analitics_good_instrument = {"Депозит":0, "ОВГЗ":0, "ПИФ":0, "P2P":0,"НПФ":0, "IPO":0}
    for i in answers:
        if i == 0:
            markup = ReplyKeyboardMarkup(True)
            markup.row(KeyboardButton('Пройти тест заново'))
            bot.send_message(message.chat.id, "Пройдите опрос ещё раз!", reply_markup = markup, parse_mode="html")
            return None

    if is_PIF(answers):
        analitics_good_instrument["ПИФ"] +=1
        messages.append(PIF_text())
        buttons.append(KeyboardButton('Компании, которые занимаются ПИФ 💰'))
        have = True
    else:
        less.append("💡ПИФ - даёшь деньги компании, а он твои средства инвестирует")

    if is_P2P(answers):
        analitics_good_instrument["P2P"] +=1
        messages.append(P2P_text())
        buttons.append(KeyboardButton('Компании, которые занимаются P2P 🔗'))
        have = True
    else:
        less.append("💡P2P - маркетплейс, где выбираешь кому одолжить собственные деньги")

    if is_IPO(answers):
        analitics_good_instrument["IPO"] +=1
        messages.append(IPO_text())
        buttons.append(KeyboardButton('Компании, которые занимаются IPO 🎢'))
        have = True
    else:
        less.append("💡IPO - размещение акций компаний на биржу")

    if is_OVGZ(answers):
        analitics_good_instrument["ОВГЗ"] +=1
        messages.append(OVGZ_text())
        buttons.append(KeyboardButton('Компании, которые занимаются ОВГЗ 🏛️'))
        have = True
    else:
        less.append("💡ОВГЗ - кредитуешь государство")

    if is_NPF(answers):
        analitics_good_instrument["НПФ"] +=1
        messages.append(NPF_text())
        buttons.append(KeyboardButton('Компании, которые занимаются НПФ 👴'))

        have = True
    else:
        less.append("💡НПФ - отчисляешь свои деньги себе на пенсию")
    messages.append(DEPOSIT_text())
    analitics_good_instrument["Депозит"] +=1
    #Тому кто проходит квиз формируем подходящее
    markup = ReplyKeyboardMarkup(True)
    markup.row(KeyboardButton('Банки, которые занимаются депозитами 🗄'))
    for i in buttons:
        markup.row(i)
    markup.row(KeyboardButton('Инструменты, которые мне не подходят✖️'))
    markup.row('Пройти тест заново')

    bot.send_message(message.chat.id, "✅Для Вас подходят такие типы инструментов:", reply_markup = markup, parse_mode="html")
    if len(messages) !=0 :
        for i in messages:
            result_string = "{} {}".format(i[0],i[1])
            bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

    bot.send_message(message.chat.id, "❌Другие инструменты менее подходящие Вам:", parse_mode="html")
    for i in less:
        bot.send_message(message.chat.id, i,  reply_markup=markup, parse_mode="html")

    '''#text_to_chat settings
    text_to_chat = "Пользователь " + message.chat.first_name + " - прошел опрос"
    text_to_chat += "-Информация о пользователе:-Имя: " + str(message.chat.first_name) + " " + str(message.chat.last_name)
    text_to_chat += "-Юзернейм: " + str(message.chat.username)
    text_to_chat += "-Результаты опроса:\n" + text_to_message
    #settings end
    bot.send_message(CHAT_ID, text_to_chat)'''
    return analitics_good_instrument


def error(call):
    bot.send_message(message.chat.id, "Не понял", parse_mode="html")

def is_OVGZ(answers):
    if ICU_UAH(answers) or ICU_USD(answers) or FID_USD(answers) or FID_UAH(answers) or UNIVER_USD(answers) or UNIVER_UAH(answers) or DRAGON_CAPITAL_USD(answers) or DRAGON_UAH(answers):
        return True
    return False

def is_PIF(answers):
    if HUGS(answers) or OTP_CAPITAL_PIF(answers) or ICU_PIF(answers) or UNIVER(answers):
        return True
    return False

def is_NPF(answers):
    if ICU_NPF(answers) or LIGA_PENSIJA_NPF(answers) or OTP_NPF(answers) or KINTO_NPF(answers):
        return True
    return False

def is_DEPOSIT(answers):
    if MONOBANK(answers) or ALPHABANK(answers) or AVAL(answers) or OTP_BANK(answers):
        return True
    return False

def is_P2P(answers):
    if FINHUB(answers):
        return True
    return False

def is_IPO(answers):
    if FREEDOMFINANCE(answers) or UNITEDTRADERS(answers):
        return True
    return False


def format_string(answers):

    result_string = ""

    if ICU_UAH(answers):
        result_string+="ICU (UAH)-ОВГЗ\n"

    if ICU_USD(answers):
        result_string+="ICU (USD)-ОВГЗ\n"

    if FID_USD(answers):
        result_string+="Freedom Finance Diller (USD)-ОВГЗ\n"

    if FID_UAH(answers):
        result_string+="Freedom Finance Diller (UAH)-ОВГЗ\n"

    if UNIVER_USD(answers):
        result_string+="UNIVER (USD)-ОВГЗ\n"

    if UNIVER_UAH(answers):
        result_string+="UNIVER (UAH)-ОВГЗ\n"

    if DRAGON_CAPITAL_USD(answers):
        result_string+="Dragon Capital (USD)-ОВГЗ\n"

    if DRAGON_UAH(answers):
        result_string+="Dragon (UAH)-ОВГЗ\n"

    if HUGS(answers):
        result_string+="HUG'S-ПИФ\n"

    if UNIVER(answers):
        result_string+="UNIVER-ПИФ\n"

    if ICU_PIF(answers):
        result_string+="ICU-ПИФ\n"

    if OTP_CAPITAL_PIF(answers):
        result_string+="OTP Capital-ПИФ\n"

    if ICU_NPF(answers):
        result_string+="ICU-НПФ\n"

    if LIGA_PENSIJA_NPF(answers):
        result_string+="Liga Pensija-НПФ\n"

    if OTP_NPF(answers):
        result_string+="OTP-НПФ\n"

    if KINTO_NPF(answers):
        result_string+="Kinto-НПФ\n"

    if MONOBANK(answers) or 0==1:
        result_string+="Монобанк (до 18%)-ДЕПОЗИТ\n"

    if ALPHABANK(answers) or 0==1:
        result_string+="Альфа Банк( до 16,75%)-ДЕПОЗИТ\n"

    if AVAL(answers) or 0==1:
        result_string+="Аваль ( до 13%)-ДЕПОЗИТ\n"

    if OTP_BANK(answers) or 0==1:
        result_string+="ОТП Банк (до 13%)-ДЕПОЗИТ\n"

    if FINHUB(answers):
        result_string+="Finhub-P2P\n"

    if FREEDOMFINANCE(answers):
        result_string+="Freedom Finance-IPO\n"

    if UNITEDTRADERS(answers):
        result_string+="United Traders-IPO\n"
    if result_string == "":
        result_string +="Монобанк (до 18%)-ДЕПОЗИТ\n"
        result_string+="Альфа Банк( до 16,75%)-ДЕПОЗИТ\n"
        result_string+="Аваль ( до 13%)-ДЕПОЗИТ\n"
        result_string+="ОТП Банк (до 13%)-ДЕПОЗИТ\n"

    return result_string


def Bad(message, answers):
    messages = []
    have = False
    buttons = []
    if not is_PIF(answers):
        messages.append(PIF_text())
        buttons.append(KeyboardButton('Компании, которые занимаются ПИФ 💰'))
        have = True

    if not is_P2P(answers):
        messages.append(P2P_text())
        buttons.append(KeyboardButton('Компании, которые занимаются P2P 🔗'))
        have = True

    if not is_IPO(answers):
        messages.append(IPO_text())
        buttons.append(KeyboardButton('Компании, которые занимаются IPO 🎢'))
        have = True

    if not is_OVGZ(answers):
        messages.append(OVGZ_text())
        buttons.append(KeyboardButton('Компании, которые занимаются ОВГЗ 🏛️'))
        have = True

    if not is_NPF(answers):
        messages.append(NPF_text())
        buttons.append(KeyboardButton('Компании, которые занимаются НПФ 👴'))
        have = True

    #Тому кто проходит квиз формируем подходящее
    markup = ReplyKeyboardMarkup(True)

    for i in buttons:
        markup.row(i)

    markup.row(KeyboardButton('Посмотреть инструменты, которые мне подходят'))
    markup.row('Пройти тест заново')

    if have:
        result_string = "Для Вас неподходят такие типы инструментов:"
        bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")
        for i in messages:
            result_string = "{} {}".format(i[0],i[1])
            bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")
    else:
        bot.send_message(message.chat.id, "Нет инструментов, чтобы вам не подходили.", reply_markup = markup, parse_mode="html")

#################################################################################################################
def CallbackICUUSDOVGZ(message):
    info = ICU_USD_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackFFDUSDOVGZ(message):
    info = FID_USD_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackFFDUAHOVGZ(message):
    info = FID_UAH_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)
    result_string = """
{}{}{}{}{}{}{}{}{}
    """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])
    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackUNIVERUSDOVGZ(message):
    info = UNIVER_USD_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackUNIVERUAHOVGZ(message):
    info = UNIVER_UAH_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackDragonCapitalUSDOVGZ(message):
    info = DRAGON_CAPITAL_USD_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackDragonCapitalUAHOVGZ(message):
    info = DRAGON_UAH_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackHUGSPIF(message):
    info = HUGS_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackUNIVERPIF(message):
    info = UNIVER_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackICUPIF(message):
    info = ICU_PIF_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackOTPCapitalPIF(message):
    info = OTP_CAPITAL_PIF_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackICUNPF(message):
    info = ICU_NPF_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackLigaPensijaNPF(message):
    info = LIGA_PENSIJA_NPF_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackOTPNPF(message):
    info = OTP_NPF_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackKINTONPF(message):
    info = KINTO_NPF_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackMonobankDeposit(message):
    info = Monobank_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackAlfaBankDeposit(message):
    info = Alphabank_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackAvalDeposit(message):
    info = Aval_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackOTPBankDeposit(message):
    info = OTP_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackFinhubP2P(message):
    info = FINHUB_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")

def CallbackFFDIPO(message):
    info = FREEDOMFINANCE_text()
    result_string = ""
    result_string = """
{}{}{}{}{}{}{}{}{}
  """.format(info[1][0], info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[1][1], info[1][2], info[1][3])

    markup = ReplyKeyboardMarkup(True)

    markup.row(KeyboardButton('Выбрать компанию ✔️'))

    markup.row('Вернутся к выбору компаний')
    bot.send_message(message.chat.id, result_string, reply_markup = markup, parse_mode="html")


def send_to_Menneger(message, client):
    for i in client[1]:
        if i == 0:
            markup = ReplyKeyboardMarkup(True)
            markup.row(KeyboardButton('Пройти тест заново'))
            bot.send_message(message.chat.id, "Пройдите опрос ещё раз!", reply_markup = markup, parse_mode="html")
            return None

    bio = "ФИО: {} \nПочта: {} \nТелефон: {} \n".format(client[7][0], client[7][1], client[7][2])
    result_string= """
ФИО: {}
Ответ на 1 вопрос: {}
Ответ на 2 вопрос: {}
Ответ на 3 вопрос: {}
Ответ на 4 вопрос: {}
Ответ на 5 вопрос: {}
Ответ на 6 вопрос: {}
Ответ на 7 вопрос: {}
Подходящие инструменты: {}
Выбраный инструмент: {}
Выбраный банк: {}
""".format(client[7][0], client[1][0], client[1][1], client[1][2], client[1][3], client[1][4], client[1][5], client[1][6], format_string(client[1]), recognize_instrument(client[4]), recognize_bank(client[5]))
    markup = ReplyKeyboardMarkup(True)
    markup.add(KeyboardButton("Да, конечно"))
    markup.add(KeyboardButton("Нет, не сейчас"))
    bot.send_message(message.chat.id, "Спасибо за решение воспользоваться нашим ботом! Надеемся, он помог! А можешь еще выделить несколько секунд, чтобы ответить на 4 вопроса? Это поможет нам улучшить бота!", reply_markup = markup, parse_mode="html")
    #Опрос в конце
    bot.send_message(CHAT_ID, bio, parse_mode="html")
    bot.send_message(CHAT_ID, result_string, parse_mode="html")

def callMeneger(message, client):
    for i in client[1]:
        if i == 0:
            markup = ReplyKeyboardMarkup(True)
            markup.row(KeyboardButton('Пройти тест заново'))
            bot.send_message(message.chat.id, "Пройдите опрос ещё раз!", reply_markup = markup, parse_mode="html")
            return False
    """client[11][1] = time.time()"""
    bot.send_message(message.chat.id, "Укажи, пожалуйста свои контактные данные. И мы передадим их менеджеру комании:", parse_mode="html")
    bot.send_message(message.chat.id, "Укажи, своё имя и фамилию:", reply_markup = ReplyKeyboardRemove(), parse_mode="html")




def recognize_instrument(num):
    if num == 1:
        return "OVGZ"
    elif num == 2:
        return "PIF"
    elif num == 3:
        return "NPF"
    elif num == 4:
        return "Deposit"
    elif num == 5:
        return "P2P"
    elif num == 6:
        return "IPO"

def recognize_bank(num):
    if num == 16:
        return "Monobank"
    if num == 17:
        return "АльфаБанк"
    if num == 18:
        return "АвальБанк"
    if num == 19:
        return "ОТП Банк"
    if num == 1:
        return "ICU UAH/USD"
    if num == 11:
        return "ICU UAH"
    if num == 3:
        return "Freedom Finance  UAH/USD"
    if num == 2:
        return "Freedom Finance UAH"
    if num == 5:
        return "UNIVER  UAH/USD"
    if num == 4:
        return "UNIVER UAH"
    if num == 7:
        return "DRAGON_CAPITAL UAH/USD"
    if num == 6:
        return "DRAGON UAH"
    if num == 9:
        return "HUGS"
    if num == 8:
        return "UNIVER"
    if num == 12:
        return "ICU"
    if num == 10:
        return "OTP CAPITAL"
    if num == 14:
        return "LIGA PENSIJA"
    if num == 13:
        return "OTP"
    if num == 15:
        return "KINTO"
    if num == 20:
        return "FREEDOMFINANCE"
    if num == 21:
        return "FINHUB"

def send_review(message, client):
    result_string = """
Имя - {}
Отзыв №1 - {}
Отзыв №2 - {}
Отзыв №3 - {}
Отзыв №4 - {}
""".format(client[7][0], client[9][0], client[9][1], client[9][2], client[9][3])
    bot.send_message(CHAT_ID, result_string, parse_mode="html")

