# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [1.0.0] - 2024-12-16

### Añadido
- 🗣️ Oráculo de Voz: Script de síntesis de voz con 12 datos ambientales
- 🌍 Oráculo Sísmico: Monitoreo en tiempo real con integración OSC
- 📖 Documentación completa en README.md
- 🚀 Guía de inicio rápido (QUICKSTART.md)
- 📦 Archivo requirements.txt con dependencias
- 📄 Licencia MIT
- 🙈 Archivo .gitignore para Python
- ✨ Emojis y formateo visual en consola
- 🔧 Configuración personalizable en ambos scripts
- 📝 Documentación inline en código

### Características - Oráculo de Voz
- Reproducción continua en bucle
- Voz Paulina (español mexicano) en macOS
- Control de velocidad y volumen
- Pausa configurable entre frases
- Manejo de interrupción con Ctrl+C

### Características - Oráculo Sísmico
- Integración con API de USGS
- Envío de mensajes OSC
- Curva exponencial para dramatismo
- Transición descendente (decay)
- Logging con timestamp y ubicación
- Filtro de eventos duplicados

## [Unreleased]

### Planeado para futuras versiones
- [ ] Soporte para múltiples idiomas en Oráculo de Voz
- [ ] Dashboard web para visualización de sismos
- [ ] Modo "silencioso" solo con visualización
- [ ] Integración con otras APIs climáticas
- [ ] Configuración vía archivo JSON
- [ ] Tests unitarios
- [ ] Docker container
- [ ] Documentación de instalaciones realizadas
- [ ] Ejemplos de patches para Max/MSP y TouchDesigner

---

## Tipos de cambios

- **Añadido**: para nuevas funcionalidades
- **Cambiado**: para cambios en funcionalidades existentes
- **Deprecado**: para funcionalidades que serán eliminadas
- **Eliminado**: para funcionalidades eliminadas
- **Corregido**: para corrección de bugs
- **Seguridad**: para vulnerabilidades
