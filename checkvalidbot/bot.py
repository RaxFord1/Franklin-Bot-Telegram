import telebot
from telebot import types
from telebot.types import Message

TOKEN = "725121974:AAHZMVMJbSh7GuqSTM4hZ1RMRL7Q6X1EbWk"

START_MESSAGE = "Привет, я представляю интересы Дмитрия!\n Что-бы узнать список команд, введи /help."
HELP_MESSAGE = "Ну короче кто-то слишком ленивый что бы это заполнять!"
ERROR_MESSAGE = "Что-то пошло не так... Попробуй по другому"
LANG_MESSAGE = "Choose your language/Выберите свой язык/Виберіть свою мову:"
START_MESSAGE = "Ещё не придумал"

bot = telebot.TeleBot(TOKEN)

def check_message(message):
	if message=="":
		return True
	else:
		return False


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    is_registered(message)
    bot.reply_to(message, START_MESSAGE)#, reply_markup=lang_quest)
    
@bot.edited_message_handler(commands=['start'])
def send_welcome_edited(message: Message):
    bot.send_message(message.chat.id, START_MESSAGE) #reply_markup=lang_quest)

@bot.edited_message_handler(content_types=['text'])
def echo_digits_edited(message: Message):
    #print(message,"---------------")
    markup = types.ReplyKeyboardRemove(selective=False)
    #bot.reply_to(message, f"Редачишь, значит {message.message_id}")

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
	check_message()
    print(message,"---------------")
    try_ans = try_Answer(message.from_user.id, message.json['text'])
    text = try_ans['text']
    markup = try_ans['markup']
    #bot.reply_to(message, text, reply_markup=markup)

bot.polling()