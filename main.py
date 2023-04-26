from telebot import TeleBot
import wikipedia


bot = TeleBot("5672162831:AAGRpAFTkr0JPCD8kopSx702bsZNNf-sBb8")
wikipedia.set_lang("ru")


@bot.message_handler(content_types=["text"])
def get(message):
    try:
        resp = wikipedia.summary(message.text)
        bot.send_message(message.chat.id, resp)
    except wikipedia.DisambiguationError:
        bot.send_message(message.chat.id, "Попробуйте более конкретный запрос")
    except wikipedia.PageError:
        bot.send_message(
            message.chat.id, f"Старница с названием '{message.text} не найдена'")


if __name__ == "__main__":
    bot.polling(none_stop=True)
