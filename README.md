# 🚀 Soft.json – Publish Automation Backend

## 📌 Descripción general

Este proyecto corresponde al **backend del sistema de automatización de publicaciones** de **Soft.json**. Su objetivo es generar contenido para redes sociales usando **IA**, almacenarlo de forma estructurada y, progresivamente, **programar y publicar automáticamente** dicho contenido en distintas plataformas.

El backend está construido con **FastAPI**, **SQLAlchemy** y **PostgreSQL**, siguiendo una arquitectura modular y escalable pensada para evolucionar hacia un producto comercial.

---

## 🧠 Estado actual del proyecto

Actualmente el sistema:

✅ Genera contenido usando IA (Gemini)
✅ Guarda los posts generados en base de datos
✅ Permite consultar el historial de publicaciones generadas

Pendiente / en desarrollo:

❌ Programación de publicaciones (Scheduler)
❌ Publicación automática en redes sociales
❌ Manejo de usuarios y autenticación
❌ Planes pagos y control de acceso

---

## 🎯 Visión del proyecto

Este backend está pensado como la base de un **sistema de automatización de marketing de contenidos**, con enfoque en:

* Creadores de contenido
* Emprendedores
* Empresas
* Agencias de marketing

La estrategia de crecimiento del proyecto sigue este orden:

1. **Generación de valor** (automatización y publicación)
2. **Integraciones con redes sociales**
3. **Autenticación y monetización**

---

## 🧱 Stack tecnológico

* **Python** 3.11+ (recomendado 3.12)
* **FastAPI** – Framework web
* **Uvicorn** – ASGI server
* **SQLAlchemy** – ORM
* **PostgreSQL** – Base de datos
* **Alembic** – Migraciones (previsto)
* **Gemini API** – Generación de contenido con IA

---

## 📂 Estructura del proyecto

```text
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── routes/
│   │           └── generator.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   └── generated_post.py
│   ├── schemas/
│   │   └── post.py
│   ├── services/
│   │   └── ai.py
│   └── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto asegúrate de tener instalado:

### 1️⃣ Python

* Versión recomendada: **Python 3.11 o superior**

Verificar versión:

```bash
python --version
```

---

### 2️⃣ PostgreSQL

* PostgreSQL instalado y corriendo localmente

Verificar conexión:

```bash
psql --version
```

---

## 🐍 Entorno virtual (MUY IMPORTANTE)

Se recomienda **SIEMPRE** usar un entorno virtual.

### Crear el entorno virtual

```bash
python -m venv .venv
```

### Activar el entorno virtual

**Windows (PowerShell):**

```bash
.venv\Scripts\Activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

---

## 📦 Instalación de dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

Archivo `requirements.txt`:

```text
fastapi
uvicorn[standard]
pydantic-settings
sqlalchemy
psycopg2-binary
alembic
python-dotenv
```

---

## 🔐 Variables de entorno (.env)

Debes crear un archivo **`.env`** en la raíz del backend.

### Ejemplo de `.env`

```env
ENV=development

DATABASE_URL=postgresql://usuario:password@localhost:5432/softjson_publish

GEMINI_API_KEY=tu_api_key_de_gemini

SECRET_KEY=una_clave_secreta_segura
```

⚠️ **IMPORTANTE:**

* El archivo `.env` NO debe subirse al repositorio
* Asegúrate de que `DATABASE_URL` sea correcta

---

### Desactivar el entorno virtual

**Windows (PowerShell):**

```bash
deactivate
```


## 🗄️ Configuración de la base de datos

### 1️⃣ Crear la base de datos

Desde psql:

```sql
CREATE DATABASE softjson_ai;
```

### 2️⃣ Verificar permisos del usuario

El usuario debe tener permisos sobre el esquema `public`:

```sql
GRANT ALL PRIVILEGES ON DATABASE softjson_ai TO softuser;
GRANT ALL ON SCHEMA public TO softuser;
```

---

## ▶️ Ejecutar el servidor

Desde la carpeta `backend/`:

```bash
uvicorn app.main:app --reload
```

Servidor disponible en:

```
http://127.0.0.1:8000
```

---

## 📘 Documentación automática (Swagger)

FastAPI genera documentación automática:

* Swagger UI:

  ```
  http://127.0.0.1:8000/docs
  ```

* OpenAPI JSON:

  ```
  http://127.0.0.1:8000/openapi.json
  ```

---

## 🔌 Endpoints disponibles

### 🔹 Health check

```http
GET /api/v1/generator/ping
```

### 🔹 Generar publicación

```http
POST /api/v1/generator/
```

Body:

```json
{
  "topic": "automatización",
  "style": "Profesional y creativo"
}
```

### 🔹 Historial de publicaciones

```http
GET /api/v1/generator/history?limit=20
```

---

## 🛣️ Roadmap (próximos pasos)

* 🟡 Scheduler de publicaciones (B)
* 🟡 Workers / tareas en segundo plano
* 🟡 Integración con Instagram y LinkedIn
* 🟡 Autenticación y usuarios
* 🟡 Planes pagos y monetización

---

## 🤝 Notas finales

Este proyecto está en **fase temprana**, pero ya cuenta con una base sólida y profesional.

La arquitectura está pensada para:

* Escalar
* Integrarse fácilmente con otros servicios
* Evolucionar hacia un producto comercial

---

💡 **Soft.json** – Automatizando contenido, escalando impacto.


# 📌 Proyecto: Plataforma de Generación y Publicación de Contenido con IA

## 🧠 Contexto general del proyecto

Este proyecto es la base de una **plataforma inteligente para la generación, gestión y futura publicación automática de contenido**, enfocada principalmente en redes sociales.

Actualmente, el sistema se encuentra en una **fase funcional inicial**, con una base sólida sobre la cual se seguirá iterando y agregando nuevas capacidades (planificadas en fases posteriores como Plan B.1, B.2, etc.).

El objetivo a largo plazo es evolucionar hacia un **sistema autónomo** que no solo genere contenido con IA, sino que **decida cuándo publicarlo, lo publique automáticamente y optimice el rendimiento del contenido**.

---

## ✅ Estado actual del sistema (lo que YA funciona)

Actualmente el sistema permite:

* ✅ **Generar contenido usando IA** (posts)
* ✅ **Guardar los posts generados en una base de datos**
* ✅ **Consultar historial de contenido generado** mediante el endpoint `/history`

### ❌ Lo que aún NO hace (pero está planeado)

* ❌ No decide **cuándo** publicar el contenido
* ❌ No ejecuta **publicaciones automáticas**
* ❌ No integra aún APIs de redes sociales
* ❌ No tiene sistema de métricas ni feedback

---

## 🛣️ Enfoque y roadmap del proyecto

Este proyecto está pensado para crecer por **etapas claramente definidas**, manteniendo siempre una base estable:

1. **Base (actual)**

   * Generación de contenido
   * Persistencia en base de datos
   * Historial consultable

2. **Plan B.1 (siguiente fase)**

   * Programación de publicaciones
   * Sistema de estados del post (draft, scheduled, published)

3. **Fases futuras**

   * Publicación automática
   * Integración con redes sociales
   * Análisis de métricas
   * Optimización por IA

Este README documenta **exclusivamente la base actual**, para facilitar la continuidad del proyecto desde cualquier entorno.

---

## 🧱 Arquitectura general (simplificada)

* **Backend**: Python
* **IA**: Integración con modelo de lenguaje
* **Persistencia**: Base de datos local
* **Configuración**: Variables de entorno (`.env`)

---

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

### 🔹 Software necesario

* **Python 3.10 o superior**
* **Git**
* **pip** (incluido con Python)
* (Opcional pero recomendado) **Virtualenv** o **venv**

Para verificar:

```bash
python --version
git --version
pip --version
```

---

## 📥 Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

---

## 🧪 Crear entorno virtual (MUY recomendado)

### En Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### En Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

> ⚠️ **Importante**: siempre activa el entorno virtual antes de ejecutar el proyecto.

---

## 📦 Instalación de dependencias

Asegúrate de tener un archivo `requirements.txt` en el proyecto.

```bash
pip install -r requirements.txt
```

Ejemplo de librerías que normalmente incluye:

* fastapi / flask
* sqlalchemy
* pydantic
* python-dotenv
* openai (o SDK equivalente)
* uvicorn

---

## 🔐 Variables de entorno (.env)

El proyecto **NO funcionará correctamente sin un archivo `.env`**.

### 1️⃣ Crear el archivo `.env`

En la raíz del proyecto:

```bash
.env
```

### 2️⃣ Ejemplo de `.env`

```env
# API Keys
OPENAI_API_KEY=tu_api_key_aqui

# Base de datos
DATABASE_URL=postgresql+psycopg2://softuser:raat@localhost:5432/softjson_ai

# Configuración general
ENV=development

SECRET_KEY=una_clave_larga_y_segura
```

> ⚠️ **Nunca subir el archivo `.env` al repositorio**

Asegúrate de que esté incluido en `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.db
```

---

## 🗄️ Base de datos local

### Tipo de base de datos

Actualmente se usa una **base de datos local (SQLite)** para facilitar el desarrollo.

### Creación automática

* La base de datos se crea automáticamente al ejecutar el backend por primera vez
* El archivo típico es:

```text
database.db
```

### Estructura básica (conceptual)

* Tabla `posts`

  * id
  * content
  * created_at
  * status (opcional para futuras fases)

---

## ▶️ Ejecutar el proyecto

### FastAPI

```bash
uvicorn main:app --reload
```

---

## 🔎 Endpoints disponibles

### 📄 Generar contenido

```http
POST /generate
```

* Genera contenido usando IA
* Guarda automáticamente el resultado en la base de datos

---

### 📜 Historial de contenido

```http
GET /history
```

* Devuelve todos los posts generados
* Ordenados por fecha

---

## 🧯 Errores comunes y soluciones

### ❌ Error: falta variable de entorno

* Verifica que el archivo `.env` exista
* Confirma que esté siendo cargado con `python-dotenv`

---

### ❌ Error: módulo no encontrado

```bash
ModuleNotFoundError
```

* Asegúrate de haber activado el entorno virtual
* Reinstala dependencias:

```bash
pip install -r requirements.txt
```

---

## 🧠 Notas importantes

* Este README está pensado para que **cualquier persona que haga solo un `git clone` pueda levantar el proyecto sin contexto previo**.
* No asume conocimiento interno del desarrollo.
* Sirve como **punto de retorno** en caso de pausar el proyecto.

---

## 🚀 Próximos pasos (documentados pero NO implementados aún)

* Sistema de scheduling
* Estados de publicación
* Workers / tareas en background
* Integración con redes sociales
* Métricas y optimización

---

📌 **Este README será actualizado conforme el proyecto evolucione.**
