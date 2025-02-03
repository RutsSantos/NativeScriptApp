from fastapi import FastAPI, BackgroundTasks
from celery import Celery
import firebase_admin
from firebase_admin import messaging, credentials
import time

app = FastAPI()

# Configuración de Celery con Redis como broker
celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# Cargar credenciales de Firebase
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)

# 🔹 Función para procesar facturación en segundo plano
@celery_app.task
def process_invoice_task(invoice_data):
    time.sleep(5)  # Simulación de procesamiento
    send_push_notification(invoice_data["user_token"], "Factura procesada", "Tu factura ha sido procesada con éxito.")
    return {"status": "completed", "invoice": invoice_data}

# 🔹 Endpoint para procesar una factura
@app.post("/process-invoice")
def process_invoice(invoice_data: dict, background_tasks: BackgroundTasks):
    task = process_invoice_task.delay(invoice_data)
    return {"task_id": task.id, "message": "Factura en proceso"}

# 🔹 Ver estado de una tarea en Celery
@app.get("/task-status/{task_id}")
def get_task_status(task_id: str):
    task = process_invoice_task.AsyncResult(task_id)
    return {"task_id": task.id, "status": task.status}

# 🔹 Enviar notificación push a un dispositivo con Firebase Cloud Messaging (FCM)
def send_push_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )
    response = messaging.send(message)
    print(f"Notificación enviada a {token}: {response}")
    return response

# 🔹 Endpoint para registrar tokens de dispositivos móviles
@app.post("/register-token")
def register_token(data: dict):
    token = data.get("token")
    if token:
        print(f"Token registrado: {token}")
        return {"message": "Token registrado correctamente"}
    return {"error": "Token no válido"}

# 🔹 Endpoint para enviar notificaciones manualmente
@app.post("/send-notification")
def send_notification(data: dict):
    token = data.get("token")
    title = data.get("title", "Notificación")
    body = data.get("body", "Mensaje recibido")
    
    if not token:
        return {"error": "Se requiere un token"}
    
    response = send_push_notification(token, title, body)
    return {"message": "Notificación enviada", "response": response}
