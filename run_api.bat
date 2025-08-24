@echo off
echo 🚀 Iniciando Repair System API...
echo.
echo 📋 Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python no está instalado o no está en el PATH
    echo 💡 Instala Python desde https://python.org
    pause
    exit /b 1
)

echo.
echo 📦 Instalando dependencias...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Error al instalar dependencias
    pause
    exit /b 1
)

echo.
echo 🎯 Dependencias instaladas correctamente
echo.
echo 🌐 La API se iniciará en: http://localhost:5000
echo 📱 Para hacer pública, usa ngrok en otra terminal
echo.
echo 🔧 Presiona Ctrl+C para detener la API
echo.
echo 🚀 Iniciando...
python app.py

pause
