# 📦 INSTRUCCIONES PARA EL ZIP

## ✅ Contenido del archivo: oraculos-github.zip

Este ZIP contiene **10 archivos** listos para subir a GitHub:

### 📄 Archivos incluidos:
1. README.md
2. QUICKSTART.md
3. GITHUB_UPLOAD.md
4. CHANGELOG.md
5. RESUMEN.md
6. oraculo_voz_loop.py
7. oraculo_sismos_PULSO_EXPO.py
8. requirements.txt
9. LICENSE
10. gitignore.txt (debes renombrarlo a .gitignore)

---

## 🚀 Pasos para usar el ZIP:

### 1. Descargar y extraer
```
1. Descarga el archivo: oraculos-github.zip
2. Extrae el contenido a una carpeta (ej: "oraculos")
3. Renombra "gitignore.txt" a ".gitignore"
```

### 2. Personalizar (IMPORTANTE - 5 minutos)

#### A. Edita LICENSE
Abre `LICENSE` y reemplaza:
```
Copyright (c) 2024 [Tu Nombre]
```
Por tu nombre real:
```
Copyright (c) 2024 Juan Pérez
```

#### B. Edita README.md
Busca al final del archivo y actualiza:
```markdown
**Autor**: [Tu Nombre]
**Email**: tu-email@example.com
**Website**: [tu-website.com]
```

#### C. Edita los scripts (opcional pero recomendado)
En ambos archivos .py, busca:
```python
Autor: [Tu nombre]
```
Y pon tu nombre real.

### 3. Subir a GitHub (elige UN método)

---

## 📤 MÉTODO 1: Arrastrar y Soltar (MÁS FÁCIL - 5 minutos)

1. Ve a https://github.com
2. Inicia sesión
3. Haz clic en "+" (arriba derecha) → "New repository"
4. Nombre: `oraculos`
5. Descripción: "Instalaciones sonoras interactivas con datos en tiempo real"
6. Marca como **Public**
7. ⚠️ NO marques "Initialize with README"
8. Click "Create repository"
9. En la página que aparece, haz clic en "uploading an existing file"
10. Arrastra TODOS los archivos de la carpeta extraída
11. Mensaje: "Primer commit: Oráculos de voz y sísmico"
12. Click "Commit changes"
13. ¡LISTO! 🎉

---

## 💻 MÉTODO 2: Usando Git (Terminal/CMD - 10 minutos)

### Paso A: Instalar Git (si no lo tienes)
- **Windows**: https://git-scm.com/download/win
- **Mac**: Ya viene instalado (o: `brew install git`)
- **Linux**: `sudo apt-get install git`

### Paso B: Crear repositorio en GitHub
1. Ve a https://github.com → "+" → "New repository"
2. Nombre: `oraculos`
3. ⚠️ NO marques "Initialize with README"
4. Click "Create repository"
5. **COPIA** la URL que aparece (ej: https://github.com/TU-USUARIO/oraculos.git)

### Paso C: Subir desde terminal
Abre Terminal (Mac/Linux) o CMD (Windows):

```bash
# Ve a la carpeta donde extrajiste el ZIP
cd /ruta/a/la/carpeta/oraculos

# Renombra gitignore.txt a .gitignore
mv gitignore.txt .gitignore

# Inicializa Git
git init

# Añade todos los archivos
git add .

# Haz commit
git commit -m "Primer commit: Oráculos de voz y sísmico"

# Conecta con GitHub (reemplaza TU-USUARIO con tu usuario)
git remote add origin https://github.com/TU-USUARIO/oraculos.git

# Cambia a rama main
git branch -M main

# Sube los archivos
git push -u origin main
```

Si te pide usuario/contraseña, usa:
- **Usuario**: tu usuario de GitHub
- **Contraseña**: un Personal Access Token (no tu contraseña normal)
  - Créalo en: GitHub → Settings → Developer settings → Personal access tokens → Generate new token

---

## 🖱️ MÉTODO 3: GitHub Desktop (GUI - 8 minutos)

1. Descarga GitHub Desktop: https://desktop.github.com/
2. Instala y ábrelo
3. File → New Repository
   - Name: `oraculos`
   - Local path: Selecciona la carpeta donde extrajiste el ZIP
4. Mueve todos los archivos del ZIP a esa carpeta
5. Renombra `gitignore.txt` a `.gitignore`
6. En GitHub Desktop verás todos los archivos
7. Escribe en "Summary": "Primer commit"
8. Click "Commit to main"
9. Click "Publish repository"
10. Marca como Public
11. ¡LISTO! 🎉

---

## ⚠️ NOTA IMPORTANTE sobre .gitignore

El archivo `gitignore.txt` debe renombrarse a `.gitignore` (con punto al inicio).

**En Windows:**
```cmd
ren gitignore.txt .gitignore
```

**En Mac/Linux:**
```bash
mv gitignore.txt .gitignore
```

**Si usas el Método 1 (arrastrar y soltar):**
No importa, puedes subir `gitignore.txt` y luego crear un archivo `.gitignore` directamente en GitHub.

---

## ✅ Verificación

Después de subir, verifica que en GitHub veas:
- README.md se muestra automáticamente
- 10 archivos en total
- Emojis funcionando 🎨
- Sintaxis de código con colores

---

## 🆘 Problemas comunes

### "No puedo renombrar a .gitignore"
En Windows, abre CMD y usa: `ren gitignore.txt .gitignore`

### "Git no está instalado"
Usa el Método 1 (arrastrar y soltar) - no necesita Git

### "Permission denied"
En el Método 2, usa un Personal Access Token en vez de tu contraseña

### "El nombre 'oraculos' ya existe"
Usa otro nombre o borra el repo existente

---

## 📞 ¿Dudas?

Si algo no funciona, revisa el archivo `GITHUB_UPLOAD.md` dentro del ZIP,
tiene instrucciones más detalladas.

---

## 🎉 ¡Éxito!

Una vez subido, comparte el link:
`https://github.com/TU-USUARIO/oraculos`

¡Tu proyecto ya está en GitHub! 🚀
