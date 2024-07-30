import requests  # Asegúrate de que esta línea esté presente
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# URL de tu Google Apps Script
APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbxHlrp-TgQttqGAYhwx6CIho7sDFnodmedw7V7e1DXWkqyOJlrOPg2yWwVMvCfmjmq5VQ/exec'

# Modelo de datos para la lectura del sensor MQ135
class MQ135Data(BaseModel):
    sensor_id: str
    co2_ppm: float

# Lista para almacenar los datos temporales (simulando una base de datos en memoria)
mq135_data_storage = []

# Endpoint para recibir datos del sensor MQ135
@app.post("/sensor/mq135/data/", response_model=MQ135Data)
def receive_mq135_data(data: MQ135Data):
    # Almacenar los datos recibidos en la lista
    mq135_data_storage.append(data)
    
    # Crear el payload para Google Apps Script
    payload = {
        "sensor_id": data.sensor_id,
        "co2_ppm": data.co2_ppm
    }
    
    # Enviar los datos a Google Apps Script
    try:
        response = requests.post(APPS_SCRIPT_URL, json=payload)
        response.raise_for_status()  # Lanza una excepción si la solicitud falló
        print('Datos enviados correctamente')
    except requests.exceptions.RequestException as e:
        print(f'Error al enviar datos: {e}')
    
    return data

# Endpoint para obtener todos los datos almacenados del sensor MQ135
@app.get("/sensor/mq135/data/all/", response_model=List[MQ135Data])
def get_all_mq135_data():
    return mq135_data_storage

# Endpoint raíz para verificar el estado del servidor
@app.get("/")
def read_root():
    return {"message": "Servidor FastAPI funcionando correctamente"}


