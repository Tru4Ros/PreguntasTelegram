import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Definimos el token del bot
TOKEN = '6288297385:AAG1dUr3aFiwodKo9v7fMD9UwBqXBhJVq5g'

# Creamos una instancia del bot
bot = telegram.Bot(token=TOKEN)

# Creamos una instancia del updater para recibir actualizaciones del bot
updater = Updater(token=TOKEN, use_context=True)

# Definimos una función para manejar el comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! Soy un bot de preguntas y respuestas. ¿En qué puedo ayudarte?")

# Definimos una función para manejar las preguntas y respuestas
def echo(update, context):
    pregunta = update.message.text
    respuesta = "Lo siento, no tengo una respuesta para esa pregunta."
    
    # Aquí iría tu lógica para responder preguntas
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=respuesta)

# Creamos los manejadores para los comandos y mensajes
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(filters.text & (~filters.command), echo)

# Añadimos los manejadores al updater
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(echo_handler)

# Iniciamos el bot
updater.start_polling()

# Mantenemos el bot en ejecución hasta que se interrumpa
updater.idle()
