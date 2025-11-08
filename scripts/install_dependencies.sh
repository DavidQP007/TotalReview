#!/bin/bash
# =========================================
# Instalador TotalReview - 100% Open Source
# =========================================

echo "🚀 Instalador TotalReview v0.1.0"
echo "🌍 Sistema open source para revisiones sistemáticas y metaanálisis"
echo "========================================"

# Verificar si conda está instalado
if ! command -v conda &> /dev/null; then
    echo "❌ Conda no encontrado. Por favor instala Miniconda/Anaconda primero:"
    echo "   https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

echo "🧹 Eliminando entorno previo (si existe)..."
conda remove -n TotalReview --all -y 2>/dev/null || true

echo "🆕 Creando entorno Conda desde environment.yml..."
conda env create -f ../environment.yml

# Activar entorno
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate TotalReview

echo "🧠 Detectando hardware para PyTorch..."
if command -v nvidia-smi &> /dev/null; then
    echo "🎮 GPU NVIDIA detectada. Instalando versión con CUDA 13.0..."
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
else
    echo "💻 No se detectó GPU. Instalando versión CPU..."
    pip install torch torchvision torchaudio cpuonly
fi

echo "🛠️ Instalando dependencias adicionales..."
pip install transformers datasets huggingface_hub accelerate sentence-transformers
pip install pymed bertopic networkx pyvis pybliometrics rapidfuzz

echo "🔧 Instalando TotalReview como paquete editable..."
pip install -e .

echo "✅ ¡Instalación completada correctamente!"
echo "========================================"
echo "🚀 Para activar tu entorno:"
echo "conda activate TotalReview"
echo ""
echo "🧪 Para probar la instalación:"
echo "python -c \"import totalreview; print('Versión:', totalreview.__version__)\""
echo ""
echo "📚 Documentación: https://github.com/DavidQP007/TotalReview"