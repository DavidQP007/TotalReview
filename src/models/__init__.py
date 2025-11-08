"""
Módulo de modelos de IA
Responsable de: Screening automático, clasificación, extracción de características
"""

from .bert_classifier import PubMedBERTClassifier, SciBERTClassifier

__all__ = ['PubMedBERTClassifier', 'SciBERTClassifier']