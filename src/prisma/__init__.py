"""
Módulo PRISMA
Responsable de: Generación de diagramas de flujo PRISMA 2020, reportes automáticos
"""

from .flow_generator import generate_prisma_flow, create_prisma_report

__all__ = ['generate_prisma_flow', 'create_prisma_report']