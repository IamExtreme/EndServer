from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

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
    print(f"Datos recibidos del sensor MQ135 {data.sensor_id}:")
    print(f"Concentración de CO2: {data.co2_ppm} ppm")

    return data

# Endpoint para obtener todos los datos almacenados del sensor MQ135
@app.get("/sensor/mq135/data/all/", response_model=List[MQ135Data])
def get_all_mq135_data():
    return mq135_data_storage

# Endpoint raíz para verificar el estado del servidor
@app.get("/")
def read_root():
    return {"message": "Servidor FastAPI funcionando correctamente"}
