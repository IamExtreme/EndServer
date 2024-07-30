from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de datos para la lectura del sensor MQ135
class MQ135Data(BaseModel):
    sensor_id: str
    co2_ppm: float

# Endpoint para recibir datos del sensor MQ135
@app.post("/sensor/mq135/data/", response_model=MQ135Data)
def receive_mq135_data(data: MQ135Data):
    # Imprimir los datos recibidos en la consola del servidor
    print(f"Datos recibidos del sensor MQ135 {data.sensor_id}:")
    print(f"Concentración de CO2: {data.co2_ppm} ppm")

    # Devolver los datos recibidos como respuesta
    return data

# Endpoint raíz para verificar el estado del servidor
@app.get("/")
def read_root():
    return {"message": "Servidor FastAPI funcionando correctamente"}

