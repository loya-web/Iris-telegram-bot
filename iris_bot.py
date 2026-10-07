import os
import telebot
from google import genai
from google.genai import types
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

bot = telebot.TeleBot(TOKEN)

# Inicializar el cliente de Gemini con la nueva librería
client = genai.Client(api_key=GEMINI_KEY)

# Instrucciones base para moldear la personalidad de I.R.I.S.
instrucciones_sistema = (
    "Eres I.R.I.S. (Intelligent Responsive Information System), una IA asistente personal avanzada. "
    "Tu tono es femenino, tecnológico, eficiente y directo, inspirado en las IAs de Iron Man. "
    "Tu usuario es un estudiante del Tec de Monterrey Campus CDMX, por lo que debes entender "
    "contexto universitario, cálculo diferencial, física electromagnética y ayudarle en sus proyectos. "
    "Responde siempre de forma clara y sin rodeos."
)

# Configuración del modelo con las instrucciones
configuracion = types.GenerateContentConfig(
    system_instruction=instrucciones_sistema,
)

# Diccionario para guardar la memoria de la conversación por usuario
sesiones_chat = {}

@bot.message_handler(commands=['start'])
def cmd_start(message):
    """Comando de inicio con panel de botones"""
    # CORREGIDO: Se actualiza el nombre del modelo a una versión actual compatible
    sesiones_chat[message.chat.id] = client.chats.create(
        model='gemini-2.5-flash',
        config=configuracion
    )
    
    saludo = "👋 **Sistemas en línea.** Soy I.R.I.S. ¿En qué protocolo trabajaremos hoy?"
    markup = InlineKeyboardMarkup()
    btn_agenda = InlineKeyboardButton("📅 Mi Agenda", callback_data="modulo_agenda")
    btn_notas = InlineKeyboardButton("📝 Registro al Vuelo", callback_data="modulo_notas")
    btn_status = InlineKeyboardButton("🟢 Estado", callback_data="modulo_status")
    
    markup.add(btn_agenda, btn_notas)
    markup.add(btn_status)
    
    bot.reply_to(message, saludo, parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def manejar_botones(call):
    """Maneja las acciones de los botones"""
    bot.answer_callback_query(call.id)
    if call.data == "modulo_agenda":
        bot.send_message(call.message.chat.id, "📅 **Módulo de Agenda:** Pendiente de conexión con Google Calendar.", parse_mode="Markdown")
    elif call.data == "modulo_notas":
        bot.send_message(call.message.chat.id, "📝 **Registro:** Dime qué quieres anotar.", parse_mode="Markdown")
    elif call.data == "modulo_status":
        bot.send_message(call.message.chat.id, "⚙️ **Diagnóstico:** LLM Gemini (Nueva API) Conectado. Memoria conversacional activa.", parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def conversar_con_gemini(message):
    """Procesa el lenguaje natural usando Gemini manteniendo el contexto"""
    chat_id = message.chat.id
    
    if chat_id not in sesiones_chat:
        # CORREGIDO: Se actualiza el nombre del modelo aquí también
        sesiones_chat[chat_id] = client.chats.create(
            model='gemini-2.5-flash',
            config=configuracion
        )
    
    bot.send_chat_action(chat_id, 'typing')
    
    try:
        respuesta = sesiones_chat[chat_id].send_message(message.text)
        bot.reply_to(message, respuesta.text, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, "⚠️ Error en la matriz de procesamiento. Intenta de nuevo.")
        print(f"Error con Gemini: {e}")

if __name__ == "__main__":
    print("🤖 I.R.I.S. conectada a la red neuronal (Nueva API). Escuchando...")
    bot.infinity_polling()