"""
TotalReview - Orquestador de IA para revisiones sistemáticas y metaanálisis
Licencia: MIT License (open source)
Autor: David Quispe Ppacco
Versión: 0.1.0 (alpha)
"""

# Importar versiones de los componentes principales
__version__ = "0.1.0"
__author__ = "David Quispe Ppacco"
__license__ = "MIT"
__description__ = "Sistema open source para automatizar revisiones sistemáticas y metaanálisis"

# Importar módulos principales para facilitar su uso
from .data_processing.pubmed_parser import PubMedParser
from .models.bert_classifier import PubMedBERTClassifier
from .prisma.flow_generator import generate_prisma_flow

# Variables de configuración globales
DEFAULT_THRESHOLD = 0.75  # Umbral por defecto para screening
SUPPORTED_DATABASES = ['pubmed', 'arxiv', 'core', 'semantic_scholar']
SUPPORTED_MODELS = ['pubmedbert', 'scibert', 'biobert', 'clinicalbert']

def get_version():
    """Devuelve la versión actual del paquete"""
    return __version__

def get_supported_models():
    """Devuelve lista de modelos soportados"""
    return SUPPORTED_MODELS

def get_supported_databases():
    """Devuelve lista de bases de datos soportadas"""
    return SUPPORTED_DATABASES

# Configuración de logging básica
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger('TotalReview')
logger.info(f"TotalReview v{__version__} inicializado")
logger.info(f"Modelos soportados: {', '.join(SUPPORTED_MODELS)}")
logger.info(f"Bases de datos soportadas: {', '.join(SUPPORTED_DATABASES)}")