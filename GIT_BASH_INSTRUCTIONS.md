# 🚀 Repair System API - Instrucciones para Git Bash

## 📋 Prerrequisitos

### 1. Instalar Git Bash
- Descarga desde: https://git-scm.com/download/win
- Instala con opciones por defecto
- Asegúrate de que Git Bash esté en el PATH

### 2. Instalar Miniconda o Anaconda
- **Miniconda** (recomendado): https://docs.conda.io/en/latest/miniconda.html
- **Anaconda**: https://www.anaconda.com/products/distribution
- Instala con opciones por defecto
- **IMPORTANTE**: Durante la instalación, marca la opción "Add to PATH"

## 🚀 Configuración y Ejecución

### Paso 1: Abrir Git Bash
- Busca "Git Bash" en el menú de inicio
- Haz clic derecho → "Ejecutar como administrador" (recomendado)
- Navega al directorio del proyecto:
```bash
cd /c/Users/HP/api-repair-system
```

### Paso 2: Configurar el entorno conda
```bash
# Dar permisos de ejecución a los scripts
chmod +x *.sh

# Configurar el entorno conda
./setup_and_run.sh
```

### Paso 3: Ejecutar la API
```bash
# En una terminal de Git Bash
./run_api.sh
```

### Paso 4: Probar la API
```bash
# En otra terminal de Git Bash
./test_api.sh
```

## 🔧 Comandos manuales (alternativa)

Si prefieres ejecutar los comandos manualmente:

### 1. Crear y activar entorno conda
```bash
conda env create -f environment.yml
conda activate repair-system-api
```

### 2. Instalar dependencias adicionales
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la API
```bash
python app.py
```

### 4. Probar la API
```bash
python test_api.py
```

## 📱 Hacer la API pública

### Opción 1: ngrok (Recomendado)
```bash
# Instalar ngrok
# Descargar desde: https://ngrok.com/

# Ejecutar ngrok
ngrok http 5000
```

### Opción 2: Cambiar puerto si es necesario
Si el puerto 5000 está ocupado, edita `app.py`:
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

## 🧪 Pruebas con Postman

1. **Importa la colección**: `Repair_System_API.postman_collection.json`
2. **Cambia la URL base** si usas ngrok o puerto diferente
3. **Ejecuta las pruebas** en orden:
   - GET /status
   - GET /repair-bay
   - POST /teapot

## 🐛 Solución de Problemas

### Error: "conda no se reconoce"
- Reinstala Miniconda/Anaconda
- Marca "Add to PATH" durante la instalación
- Reinicia Git Bash

### Error: "Permission denied"
```bash
chmod +x *.sh
```

### Error: Puerto ocupado
- Cambia el puerto en `app.py`
- O mata el proceso que usa el puerto 5000

### Error: Entorno conda no se activa
```bash
source $(conda info --base)/etc/profile.d/conda.sh
conda activate repair-system-api
```

## 📁 Estructura del Proyecto

```
api-repair-system/
├── app.py                          # API principal
├── environment.yml                 # Entorno conda
├── requirements.txt                # Dependencias pip
├── setup_and_run.sh               # Script de configuración
├── run_api.sh                     # Script para ejecutar API
├── test_api.sh                    # Script para probar API
├── test_api.py                    # Pruebas de la API
├── Repair_System_API.postman_collection.json  # Colección Postman
├── ngrok.yml                      # Configuración ngrok
├── README.md                      # Documentación general
└── GIT_BASH_INSTRUCTIONS.md      # Este archivo
```

## 🎯 Flujo de Uso

1. **Configurar**: `./setup_and_run.sh`
2. **Ejecutar**: `./run_api.sh` (en una terminal)
3. **Probar**: `./test_api.sh` (en otra terminal)
4. **Hacer pública**: `ngrok http 5000`
5. **Usar en Postman**: Importar colección y probar endpoints

## 📞 Soporte

- Verifica que conda esté en el PATH
- Asegúrate de usar Git Bash (no PowerShell)
- Ejecuta los scripts con permisos de administrador si es necesario
