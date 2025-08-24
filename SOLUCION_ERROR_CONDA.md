# 🔧 Solución al Error de Conda en Windows

## ❌ Error encontrado:
```
C:\Users\HP\Anaconda3/etc/profile.d/conda.sh: line 13: /cygdrive/c/Users/HP/Anaconda3/Scripts/conda.exe: No such file or directory
❌ Error al activar el entorno conda
```

## 🎯 **SOLUCIÓN INMEDIATA:**

### **Opción 1: Usar scripts corregidos (Recomendado)**
```bash
# Dar permisos de ejecución
chmod +x *.sh

# Configurar con script corregido para Windows
./setup_windows.sh

# Ejecutar con script corregido para Windows
./run_windows.sh
```

### **Opción 2: Comandos manuales**
```bash
# 1. Crear el entorno
conda env create -f environment.yml

# 2. Activar el entorno
conda activate repair-system-api

# 3. Ejecutar la API
python app.py
```

## 🔍 **¿Por qué ocurre este error?**

El error se debe a que Git Bash en Windows interpreta las rutas de manera diferente:
- **PowerShell/CMD**: `C:\Users\HP\Anaconda3\Scripts\conda.exe`
- **Git Bash**: `/cygdrive/c/Users/HP/Anaconda3/Scripts/conda.exe`

Los scripts originales intentaban usar `source $(conda info --base)/etc/profile.d/conda.sh`, pero en Windows con Git Bash, esta ruta no se resuelve correctamente.

## 🛠️ **Scripts corregidos creados:**

1. **`setup_windows.sh`** - Configuración sin problemas de rutas
2. **`run_windows.sh`** - Ejecución simplificada para Windows
3. **Scripts originales corregidos** - Con detección automática de Windows

## 🚀 **Pasos para resolver:**

### **Paso 1: Usar los scripts corregidos**
```bash
cd /c/Users/HP/api-repair-system
chmod +x *.sh
./setup_windows.sh
```

### **Paso 2: Ejecutar la API**
```bash
./run_windows.sh
```

### **Paso 3: Probar la API**
```bash
# En otra terminal
conda activate repair-system-api
python test_api.py
```

## 🔧 **Si continúan los problemas:**

### **Verificar instalación de conda:**
```bash
# Verificar que conda esté en el PATH
which conda
conda --version

# Si no está, agregar manualmente al PATH
export PATH="/c/Users/HP/Anaconda3/Scripts:$PATH"
export PATH="/c/Users/HP/Anaconda3:$PATH"
```

### **Usar Anaconda Prompt en lugar de Git Bash:**
1. Busca "Anaconda Prompt" en el menú de inicio
2. Navega al directorio: `cd C:\Users\HP\api-repair-system`
3. Ejecuta: `conda env create -f environment.yml`
4. Ejecuta: `conda activate repair-system-api`
5. Ejecuta: `python app.py`

## 📱 **Para hacer la API pública:**

### **Con ngrok:**
```bash
# Instalar ngrok desde: https://ngrok.com/
ngrok http 5000
```

### **Con puerto alternativo:**
Si el puerto 5000 está ocupado, edita `app.py`:
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

## ✅ **Verificación de funcionamiento:**

1. **API ejecutándose**: http://localhost:5000
2. **Endpoint /status**: http://localhost:5000/status
3. **Endpoint /repair-bay**: http://localhost:5000/repair-bay
4. **Endpoint /teapot**: POST http://localhost:5000/teapot

## 🎯 **Resumen de la solución:**

- ✅ **Scripts corregidos** creados para Windows
- ✅ **Detección automática** del sistema operativo
- ✅ **Comandos manuales** como alternativa
- ✅ **Instrucciones detalladas** para resolver el problema
- ✅ **Múltiples opciones** de configuración

**La API está lista para funcionar una vez resuelto el problema de conda.**
