# -*- coding: utf-8 -*- p
#import
from telebot import TeleBot
import config
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import time
import datetime
import os
import json

userinfo = ""
import pandas as pd
clients = [[123,[0,0,0,0,0,0,0], 0, 0, 0, 0, 0, ["Имя Фамилия", "Емейл", "Номер телефона"], 0, ["bot","instrument","bank","budushee","ne hvatilo"],[1,2,3,4,5,6,7], [1,2]]]
#[0] - id
#[1]- answers
#[2] - #question
#[3] - good/bad 1- good 2 - bad
#[4] - instrument
#[5] - bank
#[6] - call the meneger 1 - contact 2 - Имя/Фамилия 3 - Емейл 4 - Телефон
#[7] - [name/surname, email, telephone]
#[10] - time for answers
#[11] - [start/callMeneger]
question_time = {}


questions = [['До 25 👶','25-30 👦','30-45 👨','Больше 45 🧔'],
['Меньше 1000$ 💵','1000-3000$ 💸','3000-5000$ 💰','Больше 5000$ 🧾'],
['меньше 10% 🌑','10-25% 🌒','25-50% 🌓','больше 50% 🌔'],
['Да 🐣', 'Нет 🍾'],
['Баланс доходности и риска ⚖️','Большая покупка 🚗','Сохранение капитала🗄','Безбедная старость 🛀🏻 '],
['Да 🎢', 'Нет 🎠'],
['менее 1 года 🕯','1-3 года ⏱','3-5 лет ⏰','более 5 лет ⏳']]

'''

analitics = {
    "n_starts": 141,
    "n_callMeneger": 1,
    "analitics_feedback":1,
    "instruments":{
        "Депозит":[7,103],
        "ОВГЗ":[8,103],
        "ПИФ":[10,103],
        "P2P":[15,75],
        "НПФ":[1,41],
        "IPO":[7,63]
    }
}
with open("analitics.json", "w", encoding="utf-8") as file:
    json.dump(analitics, file)
'''

'''
banks_analitics = {
"АльфаБанк":0,"АвальБанк":0,"ОТП Банк":0,"ICU UAH/USD":0,"ICU UAH":0,
"Freedom Finance UAH/USD":1,"Freedom Finance UAH":1,"UNIVER UAH/USD":1,"UNIVER UAH":0,
"Dragon Capital UAH/USD":0,"Dragon UAH":0,"HUGS":4,"Univer":1,"ICU":0,"OTP Capital":1,
"Лига Пенсия":0,"OTP":0,"Kinto":0,"Freedom Finance":1,"FinHub":8, "Monobank":1
}

with open("banks_analitics.json", "w", encoding="utf-8") as file:
    json.dump(banks_analitics, file)
'''

'''

qts = {
    "qt1":[0,0,0,0],
    "qt2":[0,0,0,0],
    "qt3":[0,0,0,0],
    "qt4":[0,0],
    "qt5":[0,0,0,0],
    "qt6":[0,0],
    "qt7":[0,0,0,0]
}

with open("questions.json", "w", encoding="utf-8") as file:
    json.dump(qts, file, ensure_ascii=False)
'''
with open('analitics.json') as json_file:
    analitics = json.load(json_file, encoding='utf-8')
    print(analitics)
with open('banks_analitics.json') as json_file:
    banks_analitics = json.load(json_file,  encoding='utf-8')
    print(banks_analitics)
with open('questions.json') as json_file:
    qts = json.load(json_file)
    print(qts)

question_time_analitics = [[],[],[],[],[],[],[]]
#print(question_time_analitics)
#print("####",question_time_analitics['qt1'])
"""= {
"АльфаБанк":[0],"АвальБанк":[0],"ОТП Банк":[0],"ICU UAH/USD":[0],"ICU UAH":[0],
"Freedom Finance UAH/USD":[0],"Freedom Finance UAH":[0],"UNIVER UAH/USD":[0],"UNIVER UAH":[0],
"Dragon Capital UAH/USD":[0],"Dragon UAH":[0],"HUGS":[0],"Univer":[0],"ICU":[0],"OTP Capital":[0],
"Лига Пенсия":[0],"OTP":[0],"Kinto":[0],"Freedom Finance":[0],"FinHub":[0], "Monobank":[0]
}"""
#instrument_analitics = {"Депозит":[0], "ОВГЗ":[0], "ПИФ":[0], "P2P":[0],"НПФ":[0], "IPO":[0]}


callback_analitics = [{}, {}, {}, {}]




#bot creating
TOKEN = "1061044668:AAG9GvEyVTgXcrKsl927zzrr1Zmzg6WMca8"

bot = TeleBot(TOKEN)

def send_every24():
    result_string = "Колво запусков бота: {}\n".format(n_starts)
    result_string += "Колво отправленых заявок обраной связи: {}\n".format(analitics["n_callMeneger"])
    bot.send_message(message.chat.id, result_string)


def edit_good(answers):
    analitics["instruments"]["Депозит"][1] += answers["Депозит"]
    analitics["instruments"]["ОВГЗ"][1] += answers["ОВГЗ"]
    analitics["instruments"]["ПИФ"][1] += answers["ПИФ"]
    analitics["instruments"]["P2P"][1] += answers["P2P"]
    analitics["instruments"]["НПФ"][1] += answers["НПФ"]
    analitics["instruments"]["IPO"][1] += answers["IPO"]


#bot handlers/settings
@bot.message_handler(commands=['start', 'info', 'analitics'])
def commands(message):
    msg = message.json["text"]
    found = False
    call = message
    client = [message.chat.id, [msg,0,0,0,0,0,0], 0, 0, 0, 0, 0, ["Имя Фамилия", "Емейл", "Номер телефона"], 0, ["bot","instrument","bank","budushee","ne hvatilo"], [1,2,3,4,5,6,7]]
    client_id = None
    if message.json['text'] == '/info':
        text = """Бот, который поможет подобрать нужный инвестиционный инструмент 🤑
Сейчас бот находится в разработке, если у тебя есть предложение, как можно улучшить продукт или ты обнаружишь какие-то баги, смело пиши на @Franklin_faq ❗️\nДля начала опроса нажми /start!"""
        bot.send_message(message.chat.id, text)

    for j,i in enumerate(clients):

        if i[0] == message.chat.id:
            found = True
            client = i
            client_id = j
            break

    if not found:
        analitics["n_starts"] += 1
        client_id = len(clients)
        clients.append(client)
        clients[client_id][1] = client[1]
        clients[client_id][2] = client[2]
    #Если клиент заполняет заявку
    if message.json['text'] == "/start":
        if not found:
            analitics["n_starts"] += 1
            #clients[client_id][11][0] = time.time()"""
        clients[client_id][8] = 0
        clients[client_id][6] = 0
        clients[client_id][5] = 0
        clients[client_id][4] = 0
        clients[client_id][3] = 0
        clients[client_id][2] = 1
        clients[client_id][1] = [0,0,0,0,0,0,0]
        question_time[message.chat.id] = int(time.time())
        config.StartQuiz(message)


    elif message.json["text"] == "/analitics":
        result_string = "Колво запусков бота: {}\n".format(analitics["n_starts"])
        result_string += "Колво отправленых заявок обраной связи: {}\n".format(analitics["n_callMeneger"])
        result_string += "Статистика ответов по вопросам:\n"
        result_string += "Сколько Вам лет?\n"
        result_string += "   Среднее время: {} секунд\n".format(sum(question_time_analitics[0])/len(question_time_analitics[0]))

        for j, i in enumerate(qts['qt1']):
            result_string+= "    Ответ {} : {}\n".format(questions[0][j], i)

        result_string += "Какую сумму Вы готовы проинвестировать?\n"
        result_string += "   Среднее время: {} секунд\n".format(sum(question_time_analitics[1])/len(question_time_analitics[1]))
        for j, i in enumerate(qts['qt2']):
            result_string+= "    Ответ {} : {}\n".format(questions[1][j], i)

        result_string += "Какую часть от своего дохода Вы откладываете?\n"
        result_string += "   Среднее время: {} секунд\n".format(sum(question_time_analitics[2])/len(question_time_analitics[2]))
        for j, i in enumerate(qts['qt3']):
            result_string+= "    Ответ {} : {}\n".format(questions[2][j], i)

        result_string += "Есть ли у вас Дети?:\n"
        result_string += "   Среднее время: {} секунд\n".format(sum(question_time_analitics[3])/len(question_time_analitics[3]))
        for j, i in enumerate(qts['qt4']):
            result_string+= "    Ответ {} : {}\n".format(questions[3][j], i)

        result_string += "Какая основная цель Ваших инвестиций?\n"
        result_string += "   Среднее время: {} секунд\n".format(sum(question_time_analitics[4])/len(question_time_analitics[4]))
        for j, i in enumerate(qts['qt5']):
            result_string+= "    Ответ {} : {}\n".format(questions[4][j], i)

        result_string += "Готовы ли Вы инвестировать в рисковые инструменты?\n"
        result_string += "   Среднее время: {} секунд\n".format(sum(question_time_analitics[5])/len(question_time_analitics[5]))
        for j, i in enumerate(qts['qt6']):
            result_string+= "    Ответ {} : {}\n".format(questions[5][j], i)

        result_string += "На какое количество времени Вы готовы инвестировать:\n"
        result_string += "   Среднее время: {} секунд\n".format(sum(question_time_analitics[6])/len(question_time_analitics[6]))
        for j, i in enumerate(qts['qt7']):
            result_string+= "    Ответ {} : {}\n".format(questions[6][j], i)
        bot.send_message(message.chat.id, result_string)

        result_string = "Результаты по инструментам:\n"
        for i in analitics["instruments"]:
            result_string += "   {}   выбрано раз: {}\n".format(i, analitics["instruments"][i][0])
            result_string += "   Предложено раз: {}\n".format(analitics["instruments"][i][1])

        bot.send_message(message.chat.id, result_string)

        result_string = "Результаты по компаниям:\n"
        for i in banks_analitics:
            result_string += "   {}   выбрано раз: {}\n".format(i, banks_analitics[i])

        bot.send_message(message.chat.id, result_string)

        result_string = "Ответы на вопросы после тестирования:\n"

        result_string += "Достаточно ли было информации об инструментах?\n"
        for j in callback_analitics[0]:
                result_string += "{}  выбрано раз: {}\n".format(j, callback_analitics[0][j])

        result_string += "Достаточно ли было информации об команиях?\n"
        for j in callback_analitics[0]:
                result_string += "{}  выбрано раз: {}\n".format(j, callback_analitics[0][j])

        result_string += "Воспользовался/воспользуешься услугами одной из компаний, которые были описаны выше?\n"
        for j in callback_analitics[0]:
                result_string += "{}  выбрано раз: {}\n".format(j, callback_analitics[0][j])

        bot.send_message(message.chat.id, result_string)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    pass



@bot.message_handler(content_types=['text'])
def echo_id(message):
    if message.chat.type == "group":
        pass

    elif message.chat.type == "private":
        process(message)

        with open("analitics.json", "w", encoding="utf-8") as file:
            json.dump(analitics, file)
        with open("banks_analitics.json", "w", encoding="utf-8") as file:
            json.dump(banks_analitics, file)
        with open("questions.json", "w", encoding="utf-8") as file:
            json.dump(qts, file, ensure_ascii=False)
def process(message):
    msg = message.json["text"]
    found = False
    call = message
    client = [message.chat.id, [msg,0,0,0,0,0,0], 0, 0, 0, 0, 0, ["Имя Фамилия", "Емейл", "Номер телефона"], 0, ["bot","instrument","bank","budushee","ne hvatilo"]]
    client_id = None

    for j,i in enumerate(clients):

        if i[0] == message.chat.id:
            found = True
            client = i
            client_id = j
            break

    if not found:
        analitics["n_starts"] += 1
        client_id = len(clients)
        clients.append(client)
        clients[client_id][1] = client[1]
        clients[client_id][2] = client[2]
    #Если клиент заполняет заявку
    if msg == "Пройти опрос":
        clients[client_id][8] = 0
        clients[client_id][6] = 0
        clients[client_id][5] = 0
        clients[client_id][4] = 0
        clients[client_id][3] = 0
        clients[client_id][2] = 1
        clients[client_id][1] = [0,0,0,0,0,0,0]
        question_time[message.chat.id] = int(time.time())
        config.StartQuiz(message)

    elif msg == 'Пройти тест заново':
        clients[client_id][8] = 0
        clients[client_id][6] = 0
        clients[client_id][5] = 0
        clients[client_id][4] = 0
        clients[client_id][2] = 1
        clients[client_id][3] = 0
        clients[client_id][1] = [0,0,0,0,0,0,0]
        question_time[message.chat.id] = int(time.time())
        config.StartQuiz(message)

    elif msg == 'Выбрать компанию ✔️':
        clients[client_id][6] = 1
        config.callMeneger(message, clients[client_id])

    elif msg == 'Банки, которые занимаются депозитами 🗄':
        clients[client_id][4] = 4
        analitics["instruments"]['Депозит'][0] +=1
        config.givesDeposit(message)
    elif msg == 'Компании, которые занимаются ОВГЗ 🏛️':
        clients[client_id][4] = 1
        analitics["instruments"]['ОВГЗ'][0] +=1
        config.givesOVGZ(message, clients[client_id])
    elif msg == 'Компании, которые занимаются ПИФ 💰':
        clients[client_id][4] = 2
        analitics["instruments"]['ПИФ'][0] +=1
        config.givesPIF(message, clients[client_id])
    elif msg == 'Компании, которые занимаются P2P 🔗':
        clients[client_id][4] = 5
        analitics["instruments"]['P2P'][0] +=1
        config.givesP2P(message, clients[client_id])
    elif msg == 'Компании, которые занимаются НПФ 👴':
        clients[client_id][4] = 3
        analitics["instruments"]['НПФ'][0] +=1
        config.givesNPF(message, clients[client_id])
    elif msg == 'Компании, которые занимаются IPO 🎢':
        clients[client_id][4] = 6
        analitics["instruments"]['IPO'][0] +=1
        config.givesIPO(message, clients[client_id])

    elif msg == 'Инструменты, которые мне не подходят✖️':
        clients[client_id][4] = 0
        clients[client_id][3] = 2 #Человек выбирает Плохое
        config.Bad(message, clients[client_id][1])

    elif msg == 'Посмотреть инструменты, которые мне подходят':
        clients[client_id][4] = 0
        clients[client_id][3] = 1 #Человек выбирает Хорошее
        a = config.EndQuiz(message, clients[client_id][1])
        if a is not None:
            edit_good(a)

    elif msg == 'Вернутся к выбору инструментов':
        clients[client_id][4] = 0
        if clients[client_id][3] == 1 or clients[client_id][3] == 0:
            a = config.EndQuiz(message, clients[client_id][1])
            if a is not None:
                edit_good(a)

        elif clients[client_id][3] == 2:
            config.Bad(message, clients[client_id][1])


    elif msg == 'Вернутся к выбору компаний':
        clients[client_id][5] = 0
        if clients[client_id][4] == 1:
            config.givesOVGZ(message, clients[client_id])

        elif clients[client_id][4] == 2:
            config.givesPIF(message, clients[client_id])

        elif clients[client_id][4] == 3:
            config.givesNPF(message, clients[client_id])

        elif clients[client_id][4] == 4:
            config.givesDeposit(message)

        elif clients[client_id][4] == 5:
            config.givesP2P(message, clients[client_id])

        elif clients[client_id][4] == 6:
            config.givesIPO(message, clients[client_id])

        else:
            bot.send_message(message.chat.id, "Пройдите опрос ещё раз!", parse_mode="html")
            clients[client_id][8] = 0
            clients[client_id][6] = 0
            clients[client_id][5] = 0
            clients[client_id][4] = 0
            clients[client_id][3] = 0
            clients[client_id][2] = 1
            clients[client_id][1] = [0,0,0,0,0,0,0]
            question_time[message.chat.id] = int(time.time())
            config.StartQuiz(message)

    elif msg == "Подробнее о Monobank":
        clients[client_id][5] = 16
        banks_analitics["Monobank"] += 1
        config.CallbackMonobankDeposit(message)

    elif msg == "Подробнее о АльфаБанк":
        clients[client_id][5] = 17
        banks_analitics["АльфаБанк"] += 1
        config.CallbackAlfaBankDeposit(message)

    elif msg == "Подробнее о АвальБанк":
        clients[client_id][5] = 18
        banks_analitics["АвальБанк"] += 1
        config.CallbackAvalDeposit(message)

    elif msg == "Подробнее о ОТП Банк":
        clients[client_id][5] = 19
        banks_analitics["ОТП Банк"] += 1
        config.CallbackOTPBankDeposit(message)

    elif msg == "Подробнее о ICU UAH/USD":
        clients[client_id][5] = 1
        banks_analitics["ICU UAH/USD"] += 1
        config.CallbackICUUSDOVGZ(message)

    elif msg == "Подробнее о ICU UAH":
        clients[client_id][5] = 11
        banks_analitics["ICU UAH"] += 1
        config.CallbackICUPIF(message)

    elif msg == "Подробнее о Freedom Finance  UAH/USD":
        clients[client_id][5] = 3
        banks_analitics["Freedom Finance UAH/USD"] += 1
        config.CallbackFFDUSDOVGZ(message)

    elif msg == "Подробнее о Freedom Finance UAH":
        clients[client_id][5] = 2
        banks_analitics["Freedom Finance UAH"] += 1
        config.CallbackFFDUAHOVGZ(message)

    elif msg == "Подробнее о UNIVER  UAH/USD":
        clients[client_id][5] = 5
        banks_analitics["UNIVER UAH/USD"] += 1
        config.CallbackUNIVERUSDOVGZ(message)

    elif msg == "Подробнее о UNIVER UAH":
        clients[client_id][5] = 4
        banks_analitics["UNIVER UAH"] += 1
        config.CallbackUNIVERUAHOVGZ(message)

    elif msg == "Подробнее о DRAGON_CAPITAL UAH/USD":
        banks_analitics["Dragon Capital UAH/USD"] += 1
        clients[client_id][5] = 7
        config.CallbackDragonCapitalUSDOVGZ(message)

    elif msg == "Подробнее о DRAGON UAH":
        clients[client_id][5] = 6
        banks_analitics["Dragon UAH"] += 1
        config.CallbackDragonCapitalUAHOVGZ(message)

    elif msg == "Подробнее о HUGS":
        clients[client_id][5] = 9
        banks_analitics["HUGS"] += 1
        config.CallbackHUGSPIF(message)

    elif msg == "Подробнее о UNIVER":
        clients[client_id][5] = 8
        banks_analitics["Univer"] += 1
        config.CallbackUNIVERPIF(message)

    elif msg == "Подробнее о ICU":
        banks_analitics["ICU"] += 1
        clients[client_id][5] = 12
        config.CallbackICUNPF(message)

    elif msg == "Подробнее о OTP CAPITAL":
        clients[client_id][5] = 10
        banks_analitics["OTP Capital"] += 1
        config.CallbackOTPCapitalPIF(message)

    elif msg == "Подробнее о Лига Пенсия":
        banks_analitics["Лига Пенсия"] += 1
        clients[client_id][5] = 14
        config.CallbackLigaPensijaNPF(message)

    elif msg == "Подробнее о OTP":
        banks_analitics["OTP"] += 1
        clients[client_id][5] = 13
        config.CallbackOTPNPF(message)

    elif msg == "Подробнее о KINTO":
        banks_analitics["Kinto"] += 1
        clients[client_id][5] = 15
        config.CallbackKINTONPF(message)

    elif msg == "Подробнее о FREEDOMFINANCE":
        banks_analitics["Freedom Finance"] += 1
        clients[client_id][5] = 20
        config.CallbackFFDIPO(message)

    elif msg == "Подробнее о FINHUB":
        banks_analitics["FinHub"] += 1
        clients[client_id][5] = 21
        config.CallbackFinhubP2P(message)

    elif clients[client_id][6] != 0:
        if clients[client_id][6] == 1:
            clients[client_id][6] = 2
            clients[client_id][7][0] = msg

            bot.send_message(message.chat.id, "Укажи свой Email", parse_mode="html")
            #Name/Surname
        elif clients[client_id][6] == 2:
            clients[client_id][6] = 3
            clients[client_id][7][1] = msg
            bot.send_message(message.chat.id, "Укажи свой номер телефона", parse_mode="html")
            #Email
        elif clients[client_id][6] == 3:
            clients[client_id][6] = 4
            clients[client_id][7][2] = msg
            analitics["n_callMeneger"] += 1
            analitics["analitics_feedback"] += 1
            config.send_to_Menneger(message, clients[client_id])
            #telephone
        elif clients[client_id][6] == 4 and clients[client_id][8] != 2:
            if msg == "Да, конечно":
                clients[client_id][8] = 1
                clients[client_id][6] = 5
                markup = ReplyKeyboardMarkup(True)
                markup.row(KeyboardButton("Да, достаточно ✅"))
                markup.row(KeyboardButton("Нет, хотелось бы больше ❌ "))
                bot.send_message(message.chat.id, "Достаточно ли тебе было информации об инструментах, которые были предложены❓", reply_markup = markup, parse_mode="html")
            elif msg == "Нет, не сейчас":
                clients[client_id][8] = 2
                markup = ReplyKeyboardMarkup(True)
                bot.send_message(message.chat.id, "Спасибо! <b>May the dollar bill be with you!</b>", reply_markup = ReplyKeyboardRemove(), parse_mode="html")
            #Первый вопрос последнего опроса

        elif clients[client_id][6] == 5 and clients[client_id][8] == 1:
            clients[client_id][9][0] = msg
            if msg not in callback_analitics:
                callback_analitics[0][msg] = 1
            else:
                callback_analitics[0][msg] += 1
            clients[client_id][6] = 6
            markup = ReplyKeyboardMarkup(True)
            markup.row(KeyboardButton("Да, достаточно ✅"))
            markup.row(KeyboardButton("Нет, хотелось бы больше ❌"))
            bot.send_message(message.chat.id, "Достаточно ли тебе было информации о компаниях, которые были предложены❓", reply_markup = markup, parse_mode="html")

        elif clients[client_id][6] == 6 and clients[client_id][8] == 1:
            clients[client_id][6] = 7
            clients[client_id][9][1] = msg
            if msg not in callback_analitics:
                callback_analitics[1][msg] = 1
            else:
                callback_analitics[1][msg] += 1
            markup = ReplyKeyboardMarkup(True)
            markup.row(KeyboardButton("Да ✅"))
            markup.row(KeyboardButton("Нет ❌"))
            bot.send_message(message.chat.id, "Воспользовался/воспользуешься услугами одной из компаний, которые были описаны выше❓", reply_markup = markup, parse_mode="html")

        elif clients[client_id][6] == 7 and clients[client_id][8] == 1:
            clients[client_id][9][2] = msg
            if msg not in callback_analitics:
                callback_analitics[2][msg] = 1
            else:
                callback_analitics[2][msg] += 1
            clients[client_id][6] = 8
            bot.send_message(message.chat.id, "Подскажи нам, пожалуйста, какой информации о команиях / инструментах тебе не хватило❓", reply_markup = ReplyKeyboardRemove(), parse_mode="html")

        elif clients[client_id][6] == 8 and clients[client_id][8] == 1:
            clients[client_id][6] = 9
            clients[client_id][9][3] = msg
            if msg not in callback_analitics:
                callback_analitics[3][msg] = 1
            else:
                callback_analitics[3][msg] += 1
            bot.send_message(message.chat.id, "Вау, спасибо! Это мне очень поможет в будущем! 😼Если хочешь поделиться еще какой-нибудь обратной связью и предложениями – пиши @Franklin_faq, он будет рад все выслушать :)", parse_mode="html")
            config.send_review(message, clients[client_id])

            pd.DataFrame(callback_analitics)
        else:
            clients[client_id][8] = 0
            clients[client_id][6] = 0
            clients[client_id][5] = 0
            clients[client_id][4] = 0
            clients[client_id][3] = 0
            clients[client_id][2] = 1
            clients[client_id][1] = [0,0,0,0,0,0,0]
            question_time[message.chat.id] = int(time.time())
            config.StartQuiz(message)


    elif clients[client_id][3] == 0:

        if msg == 'Назад🔙':
            clients[client_id][2] += -1
        else:
            #Выводим варианты ответов в соответствии с его прошлым вопросом.
            #Добавляем ответ в список
            clients[client_id][2] += 1
        if clients[client_id][2] <= 1:
            clients[client_id][8] = 0
            clients[client_id][6] = 0
            clients[client_id][5] = 0
            clients[client_id][4] = 0
            clients[client_id][3] = 0
            clients[client_id][2] = 1
            clients[client_id][1] = [0,0,0,0,0,0,0]
            question_time[message.chat.id] = int(time.time())
            config.StartQuiz(message)

        elif clients[client_id][2] == 2:
            question_time_analitics[0].append(int(time.time()) - question_time[message.chat.id])
            clients[client_id][1][0] = msg
            print(qts)
            if msg == questions[0][0]:
                qts['qt1'][0] += 1
            elif msg == questions[0][1]:
                qts['qt1'][1] += 1
            elif msg == questions[0][2]:
                qts['qt1'][2] += 1
            else:
                qts['qt1'][3] += 1
            question_time[message.chat.id] = int(time.time())
            config.secondQuestion(message)

        elif clients[client_id][2] == 3:
            question_time_analitics[1].append(int(time.time()) - question_time[message.chat.id])
            clients[client_id][1][1] = msg
            if msg == questions[1][0]:
                qts['qt2'][0] += 1
            elif msg == questions[1][1]:
                qts['qt2'][1] += 1
            elif msg == questions[1][2]:
                qts['qt2'][2] += 1
            else:
                qts['qt2'][3] += 1
            question_time[message.chat.id] = int(time.time())
            config.thirdQuestion(message)

        elif clients[client_id][2] == 4:
            question_time_analitics[2].append(int(time.time()) - question_time[message.chat.id])
            clients[client_id][1][2] = msg
            if msg == questions[2][0]:
                qts['qt3'][0] += 1
            elif msg == questions[2][1]:
                qts['qt3'][1] += 1
            elif msg == questions[2][2]:
                qts['qt3'][2] += 1
            else:
                qts['qt3'][3] += 1
            question_time[message.chat.id] = int(time.time())
            config.fourthQuestion(message)

        elif clients[client_id][2] == 5:
            question_time_analitics[3].append(int(time.time()) - question_time[message.chat.id])
            clients[client_id][1][3] = msg
            if msg == questions[3][0]:
                qts['qt4'][0] += 1
            else:
                qts['qt4'][1] += 1
            question_time[message.chat.id] = int(time.time())
            config.fifthQuestion(message)

        elif clients[client_id][2] == 6:
            question_time_analitics[4].append(int(time.time()) - question_time[message.chat.id])
            clients[client_id][1][4] = msg
            if msg == questions[4][0]:
                qts['qt5'][0] += 1
            elif msg == questions[4][1]:
                qts['qt5'][1] += 1
            elif msg == questions[4][2]:
                qts['qt5'][2] += 1
            else:
                qts['qt5'][3] += 1
            question_time[message.chat.id] = int(time.time())
            config.sixthQuestion(message)

        elif clients[client_id][2] == 7:
            question_time_analitics[5].append(int(time.time()) - question_time[message.chat.id])
            clients[client_id][1][5] = msg
            if msg == questions[5][0]:
                qts['qt6'][0] += 1
            else:
                qts['qt6'][1] += 1
            question_time[message.chat.id] = int(time.time())
            config.seventhQuestion(message)

        elif clients[client_id][2] > 7:
            question_time_analitics[6].append(int(time.time()) - question_time[message.chat.id])
            clients[client_id][2] = 0
            clients[client_id][1][6] = msg
            clients[client_id][3] = 1 #Человек выбирает Хорошее
            if msg == questions[6][0]:
                qts['qt7'][0] += 1
            elif msg == questions[6][1]:
                qts['qt7'][1] += 1
            elif msg == questions[6][2]:
                qts['qt7'][2] += 1
            else:
                qts['qt7'][3] += 1
            question_time[message.chat.id] = int(time.time())
            a = config.EndQuiz(message, clients[client_id][1])
            if a is not None:
                edit_good(a)

    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode="html")

    if message.json['text'] == 'get_id':
        text_to_message = "User ID - " + str(message.from_user.id) + "\nChat ID - " + str(message.chat.id)
        bot.reply_to(message, text_to_message)




def start():
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        bot.polling(none_stop=True)
    finally:
        bot.polling(none_stop=True)

while True:
    print("Bot running")
    start()

