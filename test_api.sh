#!/bin/bash

echo "🧪 Probando Repair System API..."
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

# Verificar que el script de prueba esté disponible
if [ ! -f "test_api.py" ]; then
    echo "❌ No se encontró test_api.py"
    exit 1
fi

echo "🔍 Verificando que la API esté ejecutándose..."
echo "💡 Asegúrate de ejecutar './run_api.sh' en otra terminal"
echo ""

# Ejecutar las pruebas
echo "🧪 Ejecutando pruebas..."
python test_api.py

echo ""
echo "=================================="
echo "🎉 Pruebas completadas!"
echo ""
echo "💡 Para probar manualmente:"
echo "   🌐 Abre tu navegador en: http://localhost:5000"
echo "   📱 Usa Postman o similar para probar los endpoints"
echo "   🔧 Verifica que cada llamada funcione según lo esperado"
