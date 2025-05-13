# Traductor con estilo (LangChain + OpenAI)

Este proyecto permite traducir un texto al idioma que elijas y aplicar un estilo personalizado (formal, divertido, técnico, etc.) usando LangChain y la API de OpenAI.

---

## 🔧 Requisitos

Antes de empezar, asegúrate de tener instalado:

- Python 3.10 o superior
- Git (opcional para clonar el repositorio)

---

## 📁 Instalación paso a paso

### 1. Clona el repositorio

2. Crea un entorno virtual
python -m venv venv

Activa el entorno:

En Windows:
.\venv\Scripts\activate
En Mac/Linux:
source venv/bin/activate


3. Instala las dependencias
pip install -r requirements.txt
Si no tienes el archivo requirements.txt, puedes instalarlo directamente con:
pip install langchain openai python-dotenv langchain-community


4. Añade tu clave de API de OpenAI
Crea un archivo llamado .env con este contenido:
OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Sustituye xxxxx por tu clave real que obtienes en https://platform.openai.com/account/api-keys

5. Ejecuta el programa
python traductor.py
El programa te pedirá:

El texto a traducir

El idioma destino

El estilo deseado

Y luego te devolverá la traducción ajustada al estilo.

📂 Archivos incluidos
traductor.py → el script principal

.env.example → plantilla del archivo .env

requirements.txt → librerías necesarias

README.md → esta guía
