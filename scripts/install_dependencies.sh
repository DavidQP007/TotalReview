#!/bin/bash
# =========================================
# Instalador Simplificado de TotalReview
# =========================================

echo "🚀 Instalador TotalReview v0.2.0"
echo "========================================"

# 1. Verificar si conda está instalado
if ! command -v conda &> /dev/null; then
    echo "❌ Conda no encontrado. Por favor, instálalo primero."
    exit 1
fi

# 2. Definir la ruta al archivo de entorno de forma robusta
# Esto asegura que el script se puede ejecutar desde cualquier ubicación
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
ENV_FILE="$SCRIPT_DIR/../environment.yml"

if [ ! -f "$ENV_FILE" ]; then
    echo "❌ No se encontró el archivo environment.yml en la ruta: $ENV_FILE"
    exit 1
fi

echo "🧹 Eliminando el entorno 'TotalReview' previo (si existe) para una instalación limpia..."
conda remove -n TotalReview --all -y

echo "🆕 Creando el nuevo entorno Conda 'TotalReview'. Esto puede tardar varios minutos..."
# 3. Crear el entorno usando únicamente el archivo yml.
# Esta es la única fuente de verdad y el método más fiable.
if conda env create -f "$ENV_FILE"; then
    echo "✅ ¡Entorno 'TotalReview' creado exitosamente!"
    echo "========================================"
    echo "🚀 Para activar tu entorno, ejecuta:"
    echo "conda activate TotalReview"
else
    echo "❌ Error al crear el entorno Conda. Revisa los mensajes de error de arriba."
    exit 1
fi
