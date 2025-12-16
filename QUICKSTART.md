# 🚀 Guía de Inicio Rápido

## Instalación en 3 pasos

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/oraculos.git
cd oraculos
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar

#### Oráculo de Voz
```bash
python oraculo_voz_loop.py
```

#### Oráculo Sísmico
```bash
python oraculo_sismos_PULSO_EXPO.py
```

---

## Primeros pasos - Oráculo de Voz

El script comenzará a recitar datos ambientales automáticamente:

```
🧠 Oráculo en bucle secuencial activado. Ctrl+C para detener.

🗣️ El mar Mediterráneo superará los uno coma cinco grados Celsius en dos mil cuarenta.
🗣️ Cada segundo se extraen mil barriles de petróleo en el mundo.
...
```

**Para detener**: Presiona `Ctrl+C`

### Personalizar

Abre `oraculo_voz_loop.py` y modifica:

```python
engine.setProperty('rate', 135)      # Velocidad (100-200)
engine.setProperty('volume', 1.0)    # Volumen (0.0-1.0)
time.sleep(2)                        # Pausa entre frases (segundos)
```

---

## Primeros pasos - Oráculo Sísmico

### Antes de ejecutar

1. **Asegúrate de tener conexión a internet** (consulta API de USGS)
2. **Configura el receptor OSC** (Max/MSP, TouchDesigner, etc.)

### Ejecutar

```bash
python oraculo_sismos_PULSO_EXPO.py
```

Verás:

```
🌍 Oráculo sísmico: curva exponencial activa...
[14:32:15] ⚡ Sismo 4.2M – 23 km NE of Tokyo, Japan
[14:32:45] ...sin actividad sísmica...
```

### Configurar receptor OSC

**En Max/MSP:**
```max
[udpreceive 7101]
|
[OSC-route /mag]
|
[print sismo]
```

**En TouchDesigner:**
- Añade un OSC In CHOP
- Network Address: `127.0.0.1`
- Network Port: `7101`
- OSC Address: `/mag`

**En Pure Data:**
```pd
[netreceive -u -b 7101]
|
[oscparse]
|
[route /mag]
|
[print]
```

### Personalizar

Abre `oraculo_sismos_PULSO_EXPO.py` y modifica:

```python
# Cambiar IP/puerto del receptor
client = SimpleUDPClient("192.168.1.100", 8000)

# Cambiar curva exponencial (más dramático = valor mayor)
EXPONENT = 3.0

# Cambiar tiempo de decay
DECAY_TIME = 8.0
```

---

## Troubleshooting común

### Oráculo de Voz

❌ **"No module named 'pyttsx3'"**
```bash
pip install pyttsx3
```

❌ **No se escucha audio (Linux)**
```bash
sudo apt-get install espeak
```

### Oráculo Sísmico

❌ **"Connection refused"**
- Verifica que el receptor OSC esté corriendo
- Confirma el puerto (default: 7101)

❌ **"No module named 'pythonosc'"**
```bash
pip install python-osc
```

❌ **No detecta sismos**
- Es normal, espera 1-2 minutos
- La API devuelve sismos de la última hora solamente
- Verifica tu conexión a internet

---

## Próximos pasos

📖 Lee el [README.md](README.md) completo para más detalles

🎨 Revisa casos de uso y ejemplos de integración

🤝 Contribuye con mejoras o nuevas funcionalidades

---

## Soporte

¿Problemas? Abre un issue en GitHub o contacta al autor.
