🚀 Soft.json – Publish Automation Backend

📖 Qué cubre este README
Este documento sirve como guía de arranque y alineación técnica. Está diseñado para que cualquier desarrollador (o tú mismo en el futuro) pueda clonar el repositorio y entender exactamente qué hace el sistema, cómo configurarlo desde cero y hacia dónde se dirige el desarrollo sin perderse en detalles de implementación futura.

🧠 Contexto y Objetivo Real
Soft.json es un motor de automatización de marketing de contenidos. El objetivo real de este backend es cerrar la brecha entre la generación de ideas y la publicación final.
El sistema utiliza IA (Gemini) para transformar conceptos en posts estructurados, los almacena de forma inteligente y prepara el terreno para que, en fases posteriores, el software decida autónomamente cuándo y dónde publicar.

✅ Estado Actual (Qué hace / Qué no hace)
Lo que ya funciona:
Generación con IA: Conexión funcional con Gemini API para crear contenido basado en temas y estilos.
Persistencia: Guardado automático de posts generados en base de datos relacional.
Consulta de Historial: Endpoints operativos para revisar todo el contenido creado.
Arquitectura Base: Estructura modular usando FastAPI, SQLAlchemy y Pydantic.
Lo que aún NO hace:
Programación (Scheduling): No hay un reloj que dispare publicaciones automáticamente.
Publicación Real: No está conectado aún con las APIs de Instagram, LinkedIn o X (Twitter).
Gestión de Usuarios: Actualmente es un sistema monopuesto (sin login/registro).
Feedback Loop: No analiza métricas de posts anteriores para mejorar la generación.

🛣️ Roadmap Conceptual (Fases)
El crecimiento del proyecto se divide en hitos de valor:
Fase 1 (Actual): Consolidación de la generación y almacenamiento.
Fase 2 (Próxima): Implementación de un Scheduler (tareas en segundo plano) y estados del post (borrador, programado, publicado).
Fase 3: Integración de conectores externos (OAuth y publicación en redes).
Fase 4: Capa de usuario, suscripciones y analítica.

⚙️ Requisitos Previos
Antes de empezar, necesitas tener instalado:
Python 3.11+: Descargar aquí
PostgreSQL: Base de datos relacional activa localmente.
Git: Para el control de versiones.
Verifica tus versiones en la terminal:
code
Bash
python --version
psql --version

🐍 Uso de Entorno Virtual
Para evitar conflictos entre las librerías de tu computadora y el proyecto, usaremos un entorno virtual. Es una "caja aislada" donde solo vivirán las dependencias de Soft.json.
Crear el entorno:
code
Bash
python -m venv .venv
Activar el entorno:
En Windows (PowerShell):
code
Bash
.venv\Scripts\Activate
En Linux / macOS:
code
Bash
source .venv/bin/activate
(Sabrás que está activo porque aparecerá (.venv) al inicio de tu línea de comandos).

📦 Instalación de Dependencias
Una vez activado el entorno virtual, instala los paquetes necesarios:
code
Bash
pip install -r requirements.txt

🔐 Configuración del .env
El proyecto utiliza variables de entorno para proteger datos sensibles. Debes crear un archivo llamado .env en la raíz de la carpeta backend/.
Ejemplo de contenido para .env:
code
Env
ENV=development
DATABASE_URL=postgresql+psycopg2://tu_usuario:tu_password@localhost:5432/softjson_ai
GEMINI_API_KEY=tu_api_key_aqui
SECRET_KEY=una_clave_aleatoria_muy_segura
[!CAUTION]
ADVERTENCIA IMPORTANTE: Nunca subas el archivo .env a GitHub. Este archivo contiene tus llaves secretas y accesos a la base de datos. Ya está incluido en el .gitignore para tu seguridad.

🗄️ Creación y Uso de la Base de Datos Local
Accede a tu terminal de PostgreSQL e ingresa:
code
SQL
CREATE DATABASE softjson_ai;
Permisos: Asegúrate de que el usuario definido en tu .env tenga permisos totales sobre esa base de datos.
Tablas: Actualmente, SQLAlchemy creará las tablas automáticamente al iniciar la aplicación (o mediante migraciones con Alembic si están configuradas).

▶️ Comandos para ejecutar el proyecto
Desde la carpeta raíz del backend, ejecuta:
code
Bash
uvicorn app.main:app --reload
El flag --reload permite que el servidor se reinicie automáticamente cada vez que hagas un cambio en el código.

🔌 Endpoints Actuales
Una vez encendido el servidor, puedes probar la API en http://127.0.0.1:8000/docs (Swagger UI) o usar estos endpoints:
Método	Endpoint	Descripción
GET	/api/v1/generator/ping	Verifica si el servicio está online.
POST	/api/v1/generator/	Genera un post con IA y lo guarda.
GET	/api/v1/generator/history	Lista los posts creados anteriormente.

🧯 Errores Comunes
ModuleNotFoundError: El entorno virtual no está activo o no ejecutaste pip install.
ConnectionRefusedError (DB): PostgreSQL no está corriendo o las credenciales en el .env son incorrectas.
401 Unauthorized (IA): Tu GEMINI_API_KEY es inválida o ha expirado.
Error 422 Unprocessable Entity: El JSON que estás enviando en el POST no coincide con el esquema esperado (revisa el modelo en /docs).

📝 Notas de Continuidad
Este proyecto está diseñado bajo una arquitectura modular en app/services, app/models y app/schemas.
Si deseas cambiar de IA (ej. pasar de Gemini a OpenAI), solo debes modificar el servicio en app/services/ai.py.
Si vas a retomar el proyecto después de un tiempo, empieza siempre verificando que el .env esté actualizado con las nuevas API Keys.

💡 Soft.json – Automatizando contenido, escalando impacto.