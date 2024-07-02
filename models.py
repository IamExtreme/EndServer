from pydantic import BaseModel
from typing import List

# Modelo de datos para la lectura del sensor MQ135
class MQ135Data(BaseModel):
    sensor_id: str
    co2_ppm: float
