# I.R.I.S. - Intelligent Responsive Information System

**I.R.I.S.** es un asistente personal conversacional e interactivo para Telegram, desarrollado en Python e impulsado por los modelos de lenguaje de **Google Gemini**. El sistema está diseñado bajo una arquitectura híbrida que combina atajos mediante *Inline Keyboards* con un canal de procesamiento de lenguaje natural con memoria conversacional.

---

## Características Principales

- **Procesamiento de Lenguaje Natural (LLM):** Conexión con la API oficial de Google Gemini (`google-genai`) para mantener conversaciones contextuales y fluidas.
- **Personalidad y Contexto Técnico:** Configuración de *System Instructions* orientadas a la resolución de problemas de ingeniería, matemáticas, física y programación.
- **Interfaz Híbrida en Telegram:** Botones interactivos para accesos rápidos (*Morning Briefing*, notas, estado del sistema) y chat de texto libre.
- **Seguridad de Credenciales:** Aislamiento estricto de claves API y tokens mediante variables de entorno (`python-dotenv`).
- **Arquitectura Escalable:** Estructura desacoplada preparada para la integración con servicios externos (Google Calendar API) y futura migración a un backend REST (FastAPI / Android).

---

## Tecnologías Utilizadas

- **Lenguaje:** Python 3.9+
- **Framework de Bot:** `pyTelegramBotAPI` (`telebot`)
- **IA / LLM SDK:** `google-genai` (Google GenAI SDK)
- **Gestión de Entorno:** `python-dotenv`
- **IDE:** Thonny / VS Code

---

## Requisitos Previos

1. **Python 3.9+** instalado.
2. Token de bot de Telegram obtenido desde [@BotFather](https://t.me/BotFather).
3. API Key de Google Gemini obtenida en [Google AI Studio](https://aistudio.google.com/).

---

## Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/loya-web/Iris-telegram-bot.git](https://github.com/loya-web/Iris-telegram-bot.git)
   cd Iris-telegram-bot