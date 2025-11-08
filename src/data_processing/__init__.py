"""
Módulo de procesamiento de datos
Responsable de: Parseo de artículos, limpieza de datos, preprocesamiento
"""

from .pubmed_parser import PubMedParser, process_pubmed_nbib

__all__ = ['PubMedParser', 'process_pubmed_nbib']