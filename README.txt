Objetivo del Proyecto
El objetivo de este proyecto es desarrollar un chatbot inteligente que pueda interpretar y simular una profesión a elección del usuario. El usuario podrá seleccionar una profesión (por ejemplo, profesor, traductor, programador o asistente) y el chatbot responderá preguntas o interactuará como si fuera un profesional de esa área, utilizando inteligencia artificial para generar respuestas coherentes y especializadas.

Instalación de Dependencias
Para que el proyecto funcione correctamente, es necesario instalar las siguientes dependencias de Python:

google-generativeai: Permite interactuar con modelos de IA generativa de Google.
python-dotenv: Permite cargar variables de entorno desde un archivo .env, útil para gestionar claves API y configuraciones sensibles.
Puedes instalar ambas dependencias ejecutando el siguiente comando en la terminal:

pip install requeriments.txt
tambien recordar que es recomendable instalar e iniciar un entorno virtual, el mismo se puede realizar con los siguientes comandos:
python -m venv venv (para crear el entorno)
.\venv\Scripts\activate (para activarlo)

Ejecución del Programa
Asegúrate de tener Python instalado en tu sistema.
Instala las dependencias como se indicó anteriormente.
Crea un archivo .env en la raíz del proyecto y agrega tus claves necesarias (por ejemplo, la API Key de Google Generative AI).
GEMINI_API_KEY=AIzaSyD************tu_clave
MODEL=gemini-2.5-flash
Ejecuta el programa principal (por ejemplo, main.py) con el siguiente comando:

python main.py

El chatbot te pedirá que elijas una profesión y luego podrás interactuar con él como si fuera un profesional de esa área.
