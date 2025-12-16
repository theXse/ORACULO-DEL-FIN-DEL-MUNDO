"""
Oráculo de Voz - Datos Ambientales
===================================

Script que utiliza síntesis de voz (TTS) para recitar continuamente
datos críticos sobre la crisis climática, ambiental y social.

Autor: xdelosandes
Fecha: 2024
Licencia: MIT

Características:
- Reproducción en bucle infinito de 12 datos verificados
- Síntesis de voz en español (voz Paulina en macOS)
- Pausas configurables entre frases
- Control de velocidad y volumen

Uso:
    python oraculo_voz_loop.py
    
    Presiona Ctrl+C para detener

Datos incluidos:
1. Temperatura del Mar Mediterráneo (proyección 2040)
2. Extracción de petróleo global
3. Punto de no retorno de la Amazonía
4. Derretimiento de hielo (2024)
5. Incremento en minería de litio
6. Tasa de extinción de especies
7. Consumo de agua en centros de datos
8. Degradación del suelo global
9. Conflictos armados por recursos naturales
10. Desigualdad en emisiones de CO₂
11. Tasa de reciclaje de plástico
12. Responsabilidad corporativa en plástico de un solo uso
"""

import pyttsx3
import time

frases = [
    "El mar Mediterráneo superará los uno coma cinco grados Celsius en dos mil cuarenta.",
    "Cada segundo se extraen mil barriles de petróleo en el mundo.",
    "La Amazonía puede alcanzar su punto de no retorno antes de dos mil cuarenta y cinco.",
    "En dos mil veinticuatro se derritieron seiscientos mil millones de toneladas de hielo.",
    "La minería de litio aumentó cuatrocientos por ciento en los últimos diez años.",
    "Cada veinte minutos desaparece una especie del planeta.",
    "Un centro de datos puede consumir hasta cinco millones de litros de agua por día.",
    "El setenta y cinco por ciento del suelo global está degradado.",
    "Más de cincuenta conflictos armados activos están vinculados a recursos naturales.",
    "El diez por ciento más rico del planeta genera la mitad de las emisiones de dióxido de carbono.",
    "Solo el nueve por ciento del plástico producido se recicla.",
    "Veinte empresas son responsables de más del cincuenta por ciento del plástico de un solo uso."
]

engine = pyttsx3.init()

# Forzar voz Paulina (mexicana)
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.paulina')
engine.setProperty('rate', 135)
engine.setProperty('volume', 1.0)

print("🧠 Oráculo en bucle secuencial activado. Ctrl+C para detener.\n")

try:
    while True:
        for frase in frases:
            print(f"🗣️ {frase}")
            engine.say(frase)
            engine.runAndWait()
            time.sleep(2)
except KeyboardInterrupt:
    print("\n⛔ Oráculo detenido.")
