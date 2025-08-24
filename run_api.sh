#!/bin/bash

echo "🚀 Iniciando Repair System API..."
echo "=================================="

# Verificar si conda está disponible
if ! command -v conda &> /dev/null; then
    echo "❌ Conda no está instalado o no está en el PATH"
    echo "💡 Ejecuta primero: ./setup_and_run.sh"
    exit 1
fi

# Activar el entorno conda - Corregido para Windows
echo "🔌 Activando entorno conda..."
# En Windows, usar la ruta correcta para Git Bash
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows con Git Bash
    CONDA_BASE=$(conda info --base)
    if [[ -f "$CONDA_BASE/etc/profile.d/conda.sh" ]]; then
        source "$CONDA_BASE/etc/profile.d/conda.sh"
    else
        # Intentar con la ruta típica de Anaconda en Windows
        source "/c/Users/HP/Anaconda3/etc/profile.d/conda.sh"
    fi
else
    # Linux/Mac
    source $(conda info --base)/etc/profile.d/conda.sh
fi

conda activate repair-system-api

if [ $? -ne 0 ]; then
    echo "❌ Error al activar el entorno conda"
    echo "💡 Intentando activar manualmente..."
    echo "   Ejecuta: conda activate repair-system-api"
    exit 1
fi

echo "✅ Entorno activado: $(conda info --envs | grep '*')"
echo ""

# Verificar que la API esté disponible
if [ ! -f "app.py" ]; then
    echo "❌ No se encontró app.py"
    exit 1
fi

echo "📡 Endpoints disponibles:"
echo "   GET  /status      - Obtener sistema averiado"
echo "   GET  /repair-bay  - Generar página de reparación"
echo "   POST /teapot      - Retornar código 418"
echo "   GET  /            - Página de inicio"
echo ""
echo "🌐 La API estará disponible en: http://localhost:5000"
echo "🔧 Para hacer pública, usa ngrok en otra terminal: ngrok http 5000"
echo ""
echo "🧪 Para probar, abre otra terminal y ejecuta: python test_api.py"
echo ""
echo "🔧 Presiona Ctrl+C para detener la API"
echo ""
echo "=================================="
echo "🚀 Iniciando..."
echo ""

# Ejecutar la API
python app.py
