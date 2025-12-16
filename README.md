# 🧠 Oráculos - Instalaciones Sonoras Interactivas

Colección de scripts de Python para instalaciones artísticas que utilizan datos en tiempo real y síntesis de voz para generar experiencias inmersivas sobre crisis climática y actividad sísmica global.

## 📦 Proyectos incluidos

### 1. 🗣️ Oráculo de Voz - Datos Ambientales
Script que reproduce continuamente datos críticos sobre cambio climático y crisis ambiental usando síntesis de voz.

### 2. 🌍 Oráculo Sísmico - Pulso Expo
Sistema en tiempo real que monitorea sismos globales y traduce su magnitud a señales OSC para instalaciones audiovisuales.

---

## 🎯 Propósito General

Estos proyectos buscan:
- Generar conciencia sobre la crisis climática y ambiental
- Crear experiencias artísticas inmersivas basadas en datos reales
- Explorar la relación entre datos científicos y experiencia sensorial
- Facilitar instalaciones interactivas en espacios expositivos

---

## 🚀 Instalación

### Requisitos previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/oraculos.git
cd oraculos
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🗣️ Oráculo de Voz - Datos Ambientales

### Descripción
Script que utiliza síntesis de voz (TTS) para recitar en bucle 12 datos alarmantes sobre la crisis climática, ambiental y social.

### Características
- ✅ Reproducción continua en bucle
- ✅ Voz en español (Paulina - mexicana en macOS)
- ✅ 12 datos verificables sobre crisis ambiental
- ✅ Pausas configurables entre frases
- ✅ Control de velocidad y volumen

### Datos incluidos

1. **Temperatura del Mediterráneo**: Proyección +1.5°C para 2040
2. **Extracción de petróleo**: 1,000 barriles por segundo
3. **Amazonía**: Punto de no retorno antes de 2045
4. **Derretimiento de hielo**: 600,000 millones de toneladas en 2024
5. **Minería de litio**: Aumento del 400% en 10 años
6. **Extinción de especies**: Una cada 20 minutos
7. **Consumo de agua**: 5 millones de litros/día en centros de datos
8. **Degradación del suelo**: 75% del suelo global
9. **Conflictos armados**: Más de 50 vinculados a recursos naturales
10. **Desigualdad CO₂**: El 10% más rico genera el 50% de emisiones
11. **Reciclaje**: Solo 9% del plástico se recicla
12. **Responsabilidad corporativa**: 20 empresas = 50% del plástico de un solo uso

### Uso

```bash
python oraculo_voz_loop.py
```

**Detener**: Presiona `Ctrl+C`

### Configuración

Edita estas líneas en `oraculo_voz_loop.py`:

```python
engine.setProperty('rate', 135)      # Velocidad (palabras/minuto)
engine.setProperty('volume', 1.0)    # Volumen (0.0 - 1.0)
time.sleep(2)                        # Pausa entre frases (segundos)
```

### Casos de uso
- 🎨 Instalaciones artísticas en galerías
- 📚 Educación ambiental en museos
- 🎭 Performance y teatro documental
- 🏛️ Espacios públicos de concientización

---

## 🌍 Oráculo Sísmico - Pulso Expo

### Descripción
Sistema que monitorea en tiempo real la actividad sísmica global mediante la API de USGS y envía señales OSC (Open Sound Control) para controlar parámetros audiovisuales en instalaciones.

### Características
- ✅ Monitoreo en tiempo real de sismos globales
- ✅ Traducción de magnitud a señales OSC
- ✅ Curva exponencial para mayor dramatismo
- ✅ Transición suave (decay) después de cada evento
- ✅ Registro en consola con timestamp y ubicación

### Funcionamiento

1. **Consulta**: Cada 30 segundos verifica sismos en USGS
2. **Detección**: Identifica nuevos eventos
3. **Normalización**: Convierte magnitud (0-10) a rango (0.1-1.0)
4. **Envío OSC**: Transmite valor a software receptor (Max/MSP, TouchDesigner, etc.)
5. **Decay**: Reduce gradualmente el valor en 5 segundos

### Uso

```bash
python oraculo_sismos_PULSO_EXPO.py
```

### Configuración OSC

Edita estos parámetros en `oraculo_sismos_PULSO_EXPO.py`:

```python
# Dirección IP y puerto del receptor OSC
client = SimpleUDPClient("127.0.0.1", 7101)

# Ruta del mensaje OSC
osc_address = "/mag"

# Parámetros de mapeo
MAG_MAX = 10.0        # Magnitud máxima esperada
VOL_MIN = 0.1         # Valor mínimo de salida
DECAY_TIME = 5.0      # Tiempo de decay en segundos
EXPONENT = 2.5        # Curva exponencial (mayor = más dramático)
```

### Flujo de datos

```
USGS API → Python Script → OSC Message → Software Receptor
(Sismos)   (Normalización)  (/mag value)  (Max/MSP/TD/etc.)
```

### Ejemplo de salida

```
🌍 Oráculo sísmico: curva exponencial activa...
[14:32:15] ⚡ Sismo 4.2M — 23 km NE of Tokyo, Japan
[14:32:45] ...sin actividad sísmica...
[14:33:15] ⚡ Sismo 5.7M — 45 km W of Santiago, Chile
```

### Integración con software

#### Max/MSP
```max
[udpreceive 7101]
|
[OSC-route /mag]
|
[scale 0.1 1. 0. 127]  # Escalar a MIDI
```

#### TouchDesigner
```python
# En un OSC In CHOP, configura:
# Network Address: 127.0.0.1
# Network Port: 7101
# OSC Address: /mag
```

#### Pure Data
```pd
[netreceive -u -b 7101]
|
[oscparse]
|
[route /mag]
```

### Casos de uso
- 🎵 Control de volumen/intensidad en piezas sonoras
- 💡 Modulación de iluminación en instalaciones
- 🎬 Triggers para contenido visual
- 📊 Visualización de datos sísmicos en tiempo real

---

## 📦 Estructura del Repositorio

```
oraculos/
│
├── oraculo_voz_loop.py              # Script de voz ambiental
├── oraculo_sismos_PULSO_EXPO.py     # Script de sismos OSC
├── README.md                         # Este archivo
├── requirements.txt                  # Dependencias Python
├── LICENSE                          # Licencia MIT
└── .gitignore                       # Archivos ignorados
```

---

## 🛠️ Dependencias

### Oráculo de Voz
- `pyttsx3` - Síntesis de voz multiplataforma

### Oráculo Sísmico
- `requests` - Consultas HTTP a USGS API
- `python-osc` - Comunicación OSC

Ver archivo `requirements.txt` para versiones específicas.

---

## 🔧 Troubleshooting

### Oráculo de Voz

**Error: "No module named 'pyttsx3'"**
```bash
pip install pyttsx3
```

**No se escucha audio (Linux)**
```bash
sudo apt-get install espeak
# Verifica que funcione:
espeak "Hola mundo"
```

**Voz incorrecta**
```python
# Lista voces disponibles:
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id)
```

### Oráculo Sísmico

**Error: "Connection refused"**
- Verifica que el software receptor OSC esté corriendo
- Confirma el puerto (default: 7101)
- Prueba con `127.0.0.1` (localhost)

**No recibe sismos**
- Verifica conexión a internet
- La API de USGS devuelve sismos de la última hora
- Espera al menos 1-2 minutos para ver actividad

**Valores OSC no cambian**
- Revisa la configuración de `EXPONENT` y `MAG_MAX`
- Verifica que el receptor esté escuchando en `/mag`

---

## 🤝 Contribución

Las contribuciones son bienvenidas! Por favor:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

### Ideas para contribuir
- Agregar más voces/idiomas
- Integrar otras APIs de datos ambientales
- Ejemplos de integración con otros softwares
- Documentación de instalaciones realizadas
- Optimización de código

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 📚 Referencias

### Datos ambientales (Oráculo de Voz)
- [IPCC Report 2023](https://www.ipcc.ch/)
- [NASA Climate Change](https://climate.nasa.gov/)
- [UN Environment Programme](https://www.unep.org/)

### API Sísmica (Oráculo Sísmico)
- [USGS Earthquake API](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
- [OSC Protocol Specification](http://opensoundcontrol.org/)

---

**⚠️ Nota**: Estos scripts están diseñados para fines artísticos y educativos. Los datos presentados son aproximaciones basadas en fuentes científicas y pueden requerir verificación adicional para uso académico formal.
