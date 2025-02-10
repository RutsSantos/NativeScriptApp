# 📌 Proyecto: Aplicación Móvil con FastAPI y NativeScript Vue

Este proyecto consiste en una **aplicación móvil desarrollada con NativeScript Vue** y un **backend en FastAPI** que maneja tareas en paralelo, envía notificaciones push y está dockerizado para su despliegue en la nube y CI/CD con Jenkins y Nexus.

---

## 📂 Estructura del Proyecto

```
NativeScriptApp/
│── backend/                 # 📂 Carpeta del Backend con FastAPI
│   │── firebase_credentials.json    # 🔑 Credenciales Firebase
│   │── Dockerfile                   # 📦 Contenedor Backend
│   │── docker-compose.yml            # ⚙️ Docker Config
│   │── requirements.txt              # 📜 Dependencias Python
│   │── fastapi_backend.py            # 🚀 Código principal
│   │── tasks.py                      # 🏗 Tareas de Celery
│
│── frontend/                 # 📂 Carpeta del Frontend con NativeScript Vue
│   │── app/                    # 📂 Código de la aplicación
│   │── package.json             # 📜 Dependencias de Vue
│   │── main.js                  # 🚀 Entrada principal de Vue
│   │── components/              # 📂 Componentes Vue y Vistas (Login, Facturación, etc.)
│   │── node_modules/            # 📂 Dependencias instaladas
│
│── README.md               # 📖 Documentación del Proyecto
└── .gitignore              # 📌 Ignorar archivos en Git
```

---

## 🚀 Instalación y Configuración

### 🔧 Requisitos Previos

- Tener **Node.js** y **npm** instalados
- Tener **Python 3.8+** y **pip** instalado
- Tener Docker y Docker Compose instalados

### ⚙️ Instalación

#### 1️⃣ Clonar el repositorio

```sh
git clone https://github.com/RutsSantos/nativescriptapp.git
cd nativescriptapp
```

#### 2️⃣ Configurar Backend (FastAPI)

```sh
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### 3️⃣ Configurar Frontend (NativeScript Vue)

```sh
cd ../frontend
npm install
```

---

## 🏗 Ejecución del Proyecto

### ▶️ Levantar el Backend (FastAPI)

```sh
cd backend
uvicorn fastapi_backend:app --host 0.0.0.0 --port 8000 --reload
```

### 📱 Levantar la App Móvil (NativeScript Vue)

Para **iOS**:

```sh
cd frontend
ns run ios
```
---

## 📡 Dockerización y Despliegue en la Nube

### 📦 Construir la imagen de Docker

```sh
cd backend
docker build -t nativescriptapp_backend .
```

### ▶️ Ejecutar el backend con Docker

```sh
docker run -p 8000:8000 nativescriptapp_backend
```

### ☁️ Desplegar en Google Cloud Platform (GCP)

- Crear una máquina virtual en GCP
- Instalar Docker en la máquina virtual
- Subir la imagen de Docker y ejecutarla

---

## 🔔 Integración de Notificaciones Push con Firebase

1. Configurar Firebase Cloud Messaging (FCM)
2. Agregar credenciales `firebase_credentials.json` en el backend
3. Enviar notificaciones push desde FastAPI

Ejemplo de envío de notificaciones:

```python
from firebase_admin import messaging

def send_push_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )
    response = messaging.send(message)
    return response
```

---

Desarrollado por Rut Santos | 2-17-1270
