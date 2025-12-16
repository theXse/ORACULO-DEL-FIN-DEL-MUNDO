"""
Oráculo Sísmico - Pulso Expo
=============================

Script que monitorea en tiempo real la actividad sísmica global mediante 
la API de USGS (United States Geological Survey) y envía señales OSC 
(Open Sound Control) para controlar parámetros audiovisuales.

Autor: xdelosandes
Fecha: 2024
Licencia: MIT

Funcionamiento:
- Consulta la API de USGS cada 30 segundos
- Detecta nuevos sismos de la última hora
- Normaliza la magnitud (0-10) a un rango (0.1-1.0) con curva exponencial
- Envía el valor vía OSC a software receptor (Max/MSP, TouchDesigner, etc.)
- Aplica una transición descendente (decay) de 5 segundos

Configuración OSC:
- IP: 127.0.0.1 (localhost)
- Puerto: 7101
- Mensaje: /mag
"""

import requests
import time
from datetime import datetime
from pythonosc.udp_client import SimpleUDPClient

# Configuración
client = SimpleUDPClient("127.0.0.1", 7101)
osc_address = "/mag"

# Parámetros
MAG_MAX = 10.0
VOL_MIN = 0.1
DECAY_TIME = 5.0  # segundos para volver al mínimo
DECAY_STEPS = 10
EXPONENT = 2.5  # curva agresiva para exagerar saltos pequeños

# API
USGS_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
ultimos_ids = set()

print("🌍 Oráculo sísmico: curva exponencial activa...")

def enviar_volumen(valor):
    client.send_message(osc_address, valor)

def transicion_descendente(desde):
    paso = (desde - VOL_MIN) / DECAY_STEPS
    for i in range(DECAY_STEPS):
        nuevo = max(VOL_MIN, desde - paso * (i + 1))
        enviar_volumen(nuevo)
        time.sleep(DECAY_TIME / DECAY_STEPS)

while True:
    try:
        response = requests.get(USGS_URL, timeout=10)
        data = response.json()
        eventos = data["features"]

        nuevos = []
        for evento in eventos:
            sid = evento["id"]
            mag = evento["properties"]["mag"]

            if sid not in ultimos_ids and mag is not None:
                nuevos.append((sid, mag))

        if nuevos:
            sid, mag = nuevos[0]
            ultimos_ids.add(sid)
            mag_norm = min((mag / MAG_MAX) ** EXPONENT, 1.0)
            lugar = eventos[0]["properties"]["place"]
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚡ Sismo {mag:.1f}M – {lugar}")

            enviar_volumen(mag_norm)
            transicion_descendente(mag_norm)
        else:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ...sin actividad sísmica...")

    except Exception as e:
        print(f"[ERROR] {e}")

    time.sleep(30)
