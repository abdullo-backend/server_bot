import telebot


bot = telebot.TeleBot("8263911520:AAEhiSH4TnjI1l3bu980oCSVE-qVEo7iEoA")

@bot.message_handler(content_types=['text'])
def javob_ba_matn(message):
    name_user = message.from_user.first_name
    matni_omada = message.text
    if matni_omada == "чи хел?":
        bot.send_message(message.chat.id, f"Ман нағз, раҳмат {name_user}!")
    elif matni_omada == "соат чанд?":
        import datetime
        vaqt = datetime.datetime.now().strftime("%H:%M")
        bot.send_message(message.chat.id, f"Соат ҳозир: {vaqt}")
    else:
        bot.send_message(message.chat.id, f"Шумо навиштед: {message.text}")

@bot.message_handler(content_types=['photo', 'voice', 'video'])
def javob_ba_aks(message):
    if message.content_type == "photo":
        bot.reply_to(message, "Ваҳ, чӣ хел акси зебо!")
        
    elif message.content_type == 'voice':
        bot.reply_to(message, "this is a voice")



bot.infinity_polling()



# from module import *
# Вазифаи хонагӣ (5 супориш):
# Барои он ки мавзӯъро нағз ёд гиред, ин 5 супоришро иҷро кунед:

# Супориши 1 (Номи корбар): Ботро тавре созед, ки вақте корбар фармони /start-ро пахш мекунад, бот гӯяд: "Салом, [Номи корбар]! Хуш омадед." (аз message.from_user.first_name истифода баред).

# Супориши 2 (Эхо-бот): Вақте корбар ба бот ягон Акс (Photo) мефиристад, бот бояд дар ҷавоб нависад: "Ман ин аксро захира кардам!".

# Супориши 3 (Шарти матнӣ): Агар корбар калимаи "хайр"-ро нависад, бот бояд ҷавоб диҳад: "То боздид, дӯстам!".

# Супориши 4 (Маълумоти ID): Фармони нави /myid илова кунед. Вақте корбар инро мефиристад, бот бояд ID-и худи ҳамон корбарро ба худаш нишон диҳад.

# Супориши 5 (Стикер): Ба message_handler намуди content_types=['sticker']-ро илова кунед ва вақте корбар стикер мефиристад, бот бояд бо стикери худаш ё бо матни "Зебо аст!" ҷавоб диҳад.