# 📤 Cómo subir a GitHub

## Opción 1: Crear repositorio desde GitHub.com (Recomendado)

### Paso 1: Crear repositorio en GitHub

1. Ve a [github.com](https://github.com)
2. Inicia sesión en tu cuenta
3. Haz clic en el botón **"+"** (esquina superior derecha) → **"New repository"**
4. Configura el repositorio:
   - **Repository name**: `oraculos` (o el nombre que prefieras)
   - **Description**: "Instalaciones sonoras interactivas con datos en tiempo real"
   - **Public** o **Private**: Elige según tu preferencia
   - ⚠️ **NO** marques "Initialize with README" (ya tenemos uno)
5. Haz clic en **"Create repository"**

### Paso 2: Subir archivos desde tu computadora

#### Opción A: Usando Git (Terminal/CMD)

```bash
# Navega a la carpeta donde están tus archivos
cd /ruta/a/tus/archivos

# Inicializa Git
git init

# Añade todos los archivos
git add .

# Haz el primer commit
git commit -m "Primer commit: Oráculos de voz y sísmico"

# Conecta con tu repositorio de GitHub (reemplaza TU-USUARIO)
git remote add origin https://github.com/TU-USUARIO/oraculos.git

# Sube los archivos
git push -u origin main
```

Si te pide credenciales, usa tu **Personal Access Token** (no tu contraseña):
- Ve a GitHub → Settings → Developer settings → Personal access tokens → Generate new token

#### Opción B: Usando GitHub Desktop (GUI)

1. Descarga [GitHub Desktop](https://desktop.github.com/)
2. Abre GitHub Desktop
3. File → Add Local Repository → Selecciona tu carpeta
4. Commit to main: "Primer commit"
5. Publish repository

#### Opción C: Arrastrar y soltar (Más simple)

1. En la página de tu repositorio recién creado en GitHub
2. Haz clic en **"uploading an existing file"**
3. Arrastra todos los archivos a la ventana
4. Escribe un mensaje de commit: "Primer commit"
5. Haz clic en **"Commit changes"**

---

## Opción 2: Crear repositorio desde la terminal (Avanzado)

### Requisitos previos
- Git instalado
- GitHub CLI (opcional pero recomendado)

### Usando GitHub CLI (gh)

```bash
# Instala GitHub CLI si no lo tienes
# macOS: brew install gh
# Windows: winget install GitHub.cli
# Linux: Ver https://github.com/cli/cli#installation

# Autentícate
gh auth login

# Crea el repositorio (en la carpeta de tu proyecto)
cd /ruta/a/tus/archivos
git init
git add .
git commit -m "Primer commit: Oráculos de voz y sísmico"

# Crea el repositorio en GitHub y sube los archivos
gh repo create oraculos --public --source=. --push
```

---

## Estructura de archivos a subir

Asegúrate de que tu carpeta contenga:

```
oraculos/
├── oraculo_voz_loop.py              ✅ Script principal #1
├── oraculo_sismos_PULSO_EXPO.py     ✅ Script principal #2
├── README.md                         ✅ Documentación principal
├── QUICKSTART.md                     ✅ Guía rápida
├── CHANGELOG.md                      ✅ Historial de cambios
├── requirements.txt                  ✅ Dependencias
├── LICENSE                          ✅ Licencia MIT
├── .gitignore                       ✅ Archivos a ignorar
└── GITHUB_UPLOAD.md                 ✅ Este archivo
```

---

## Personalización antes de subir

### 1. Edita LICENSE
Reemplaza `[Tu Nombre]` con tu nombre real:
```
Copyright (c) 2024 Tu Nombre Real
```

### 2. Edita README.md
Actualiza las secciones de contacto:
```markdown
**Autor**: Tu Nombre
**Email**: tu-email@example.com
**Website**: [tu-website.com]
```

### 3. Edita los scripts
Añade tu nombre en los docstrings:
```python
"""
Autor: Tu Nombre
Fecha: 2024
"""
```

---

## Verificación post-upload

Después de subir, verifica en GitHub:

✅ Todos los archivos están presentes  
✅ El README.md se muestra correctamente  
✅ La sintaxis de código se ve bien  
✅ Los emojis se muestran correctamente  

---

## Comandos Git útiles

```bash
# Ver estado de archivos
git status

# Ver diferencias
git diff

# Añadir archivos específicos
git add archivo.py

# Hacer commit
git commit -m "Descripción del cambio"

# Subir cambios
git push

# Ver historial
git log

# Crear rama nueva
git checkout -b nueva-funcionalidad

# Volver a rama principal
git checkout main
```

---

## Opciones adicionales en GitHub

### Configurar GitHub Pages (opcional)
Si quieres documentación web:
1. Ve a Settings → Pages
2. Source: Deploy from a branch
3. Branch: main / (root)
4. Save

### Añadir Topics (etiquetas)
En la página principal del repo, haz clic en el ⚙️ junto a "About":
- `python`
- `art-installation`
- `osc`
- `climate-change`
- `real-time-data`
- `text-to-speech`
- `seismic-data`

### Crear Release (versión)
1. Ve a Releases → Create a new release
2. Tag: `v1.0.0`
3. Title: "Primera versión estable"
4. Describe los cambios
5. Publish release

---

## Próximos pasos después de subir

1. 📝 Actualiza el README con el link correcto del repositorio
2. 🌟 Pide a colaboradores que le den "Star"
3. 📢 Comparte el link en redes sociales
4. 🤝 Acepta contribuciones de la comunidad
5. 🔄 Mantén el proyecto actualizado

---

## Problemas comunes

### "Permission denied (publickey)"
Configura SSH keys: https://docs.github.com/es/authentication/connecting-to-github-with-ssh

### "Repository already exists"
El nombre ya está en uso, elige otro nombre o elimina el repo existente.

### "Git is not recognized"
Instala Git: https://git-scm.com/downloads

---

## Recursos adicionales

- [GitHub Docs (español)](https://docs.github.com/es)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Learning Lab](https://lab.github.com/)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

---

¡Éxito con tu proyecto! 🚀
