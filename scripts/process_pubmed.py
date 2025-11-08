#!/usr/bin/env python3
"""
Script para procesar archivos .nbib de PubMed
Uso: python scripts/process_pubmed.py --input data/raw/ejemplo.nbib --output data/processed/
"""

import argparse
import os
from pathlib import Path
from totalreview.data_processing import PubMedParser

def main():
    parser = argparse.ArgumentParser(description="Procesa archivos .nbib de PubMed para revisiones sistemáticas")
    parser.add_argument('--input', type=str, required=True, help="Ruta al archivo .nbib de entrada")
    parser.add_argument('--output', type=str, required=True, help="Ruta al directorio de salida o archivo CSV")
    parser.add_argument('--debug', action='store_true', help="Modo debug con más información")
    
    args = parser.parse_args()
    
    # Configurar logging
    import logging
    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Verificar que el archivo de entrada existe
    if not os.path.exists(args.input):
        logging.error(f"  El archivo de entrada no existe: {args.input}")
        return
    
    # Determinar ruta de salida
    output_path = Path(args.output)
    if output_path.is_dir():
        # Si es directorio, crear nombre de archivo automático
        input_name = Path(args.input).stem
        output_file = str(output_path / f"{input_name}_processed.csv")
    else:
        output_file = str(output_path)
    
    # Crear directorios de salida si no existen
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    logging.info(f"  Iniciando procesamiento de PubMed")
    logging.info(f"  Archivo de entrada: {args.input}")
    logging.info(f"  Archivo de salida: {output_file}")
    
    try:
        # Procesar el archivo
        parser = PubMedParser()
        df = parser.process_pubmed_nbib(args.input, output_file)
        
        # Mostrar estadísticas
        logging.info(f"   Procesamiento completado exitosamente")
        logging.info(f"   Estadísticas:")
        logging.info(f"   • Total de artículos: {len(df)}")
        logging.info(f"   • Artículos con DOI: {df['DOI'].notna().sum()}")
        logging.info(f"   • Artículos retractados: {df['Retracted'].sum()}")
        logging.info(f"   • Artículos de revista: {df['IsJournalArticle'].sum()}")
        
        print("\n📋 Ejemplo de los primeros 2 artículos:")
        print(df.head(2).to_string(index=False))
        
    except Exception as e:
        logging.error(f"  Error durante el procesamiento: {str(e)}")
        raise

if __name__ == "__main__":
    main()