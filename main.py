import telebot
import wikipedia

bot = telebot.TeleBot("5672162831:AAGRpAFTkr0JPCD8kopSx702bsZNNf-sBb8")
wikipedia.set_lang("ru")


@bot.message_handler(content_types=["text"])
def get_response_from_wikipedia(message):
    reqst = message.text
    response = wikipedia.summary(reqst)
    bot.send_message(message.chat.id, response)


bot.polling(none_stop=True)
