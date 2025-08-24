#!/bin/bash

echo "🚀 Configurando Repair System API con Conda..."
echo "================================================"

# Verificar si conda está disponible
if ! command -v conda &> /dev/null; then
    echo "❌ Conda no está instalado o no está en el PATH"
    echo "💡 Instala Miniconda desde: https://docs.conda.io/en/latest/miniconda.html"
    echo "   O Anaconda desde: https://www.anaconda.com/products/distribution"
    exit 1
fi

echo "✅ Conda encontrado: $(conda --version)"
echo ""

# Crear el entorno conda
echo "🔧 Creando entorno conda 'repair-system-api'..."
if conda env list | grep -q "repair-system-api"; then
    echo "⚠️  El entorno ya existe, actualizando..."
    conda env update -f environment.yml
else
    echo "🆕 Creando nuevo entorno..."
    conda env create -f environment.yml
fi

if [ $? -ne 0 ]; then
    echo "❌ Error al crear/actualizar el entorno conda"
    exit 1
fi

echo "✅ Entorno conda configurado correctamente"
echo ""

# Activar el entorno - Corregido para Windows
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

# Verificar Python
echo "🐍 Verificando Python..."
python --version
if [ $? -ne 0 ]; then
    echo "❌ Error con Python"
    exit 1
fi

echo ""

# Verificar Flask
echo "🍵 Verificando Flask..."
python -c "import flask; print(f'Flask version: {flask.__version__}')"
if [ $? -ne 0 ]; then
    echo "❌ Error con Flask"
    exit 1
fi

echo ""

# Instalar dependencias adicionales si es necesario
echo "📦 Instalando dependencias adicionales..."
pip install -r requirements.txt

echo ""
echo "🎉 Configuración completada!"
echo "================================================"
echo ""
echo "🌐 Para ejecutar la API:"
echo "   conda activate repair-system-api"
echo "   python app.py"
echo ""
echo "🔧 O ejecuta directamente:"
echo "   ./run_api.sh"
echo ""
echo "📱 Para hacer pública la API:"
echo "   ngrok http 5000"
echo ""
echo "🧪 Para probar la API:"
echo "   python test_api.py"
echo ""
echo "================================================"
