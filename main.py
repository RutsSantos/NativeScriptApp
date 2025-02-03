from fastapi import FastAPI, BackgroundTasks
from celery import Celery
import firebase_admin
from firebase_admin import messaging, credentials
import time

# Configuración de Celery
celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

app = FastAPI()

# Configuración de Firebase
cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)

@celery_app.task
def process_invoice_task(invoice_data):
    time.sleep(5)  # Simulación de procesamiento
    send_push_notification(invoice_data["user_token"], "Factura procesada", "Tu factura ha sido procesada con éxito.")
    return {"status": "completed", "invoice": invoice_data}

@app.post("/process-invoice")
def process_invoice(invoice_data: dict, background_tasks: BackgroundTasks):
    task = process_invoice_task.delay(invoice_data)
    return {"task_id": task.id, "message": "Factura en proceso"}

@app.get("/task-status/{task_id}")
def get_task_status(task_id: str):
    task = process_invoice_task.AsyncResult(task_id)
    return {"task_id": task.id, "status": task.status}

# Enviar notificación push
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
